#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["websockets>=15"]
# ///
"""Print the most-requested content pages from GoAccess.

By default, this one-shot command parses the shared Nginx log in the GoAccess
sidecar.  Its dashboard source is quicker but capped.  Both sources keep
content-page URLs and write only the selected report to stdout.  Diagnostics
and failures use stderr.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import subprocess
import sys
from dataclasses import asdict, dataclass
from typing import Final
from urllib.parse import urlsplit

from websockets.exceptions import WebSocketException
from websockets.sync.client import connect

VERSION: Final = "1.0.0"
DEFAULT_URL: Final = "wss://goaccess.waylonwalker.com/ws"
FORMATS: Final = ("table", "markdown", "json", "csv", "wide", "list", "text")
SOURCES: Final = ("logs", "dashboard")
DEFAULT_NAMESPACE: Final = "waylonwalker-com"
DEFAULT_DEPLOYMENT: Final = "web"
DEFAULT_CONTAINER: Final = "goaccess"
DEFAULT_LOG_PATH: Final = "/var/log/nginx/access.log"
STATIC_PREFIXES: Final = ("/_", "/assets/", "/icons/", "/js/", "/vendor/")
NON_POST_PATHS: Final = ("/", "/archive/", "/garden/")


@dataclass(frozen=True)
class Post:
    """Aggregated GoAccess metrics for a single content page."""

    rank: int
    path: str
    visitors: int
    hits: int
    bandwidth_bytes: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print popular content pages from GoAccess.",
        epilog=(
            "The default logs source parses Nginx access logs in the GoAccess "
            "sidecar.  Use --source dashboard for a faster, but capped, snapshot.\n\n"
            "Examples:\n"
            "  %(prog)s\n"
            "  %(prog)s --limit 50 --format markdown\n"
            "  %(prog)s -f json > popular-posts.json\n"
            "  %(prog)s --source dashboard -f table\n"
            "  %(prog)s -f list | xargs -n1 printf 'https://waylonwalker.com%%s\\n'"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-f",
        "--format",
        choices=FORMATS,
        default="table",
        help="Output format (default: table).",
    )
    parser.add_argument(
        "--source",
        choices=SOURCES,
        default="logs",
        help="Data source: logs for complete results, dashboard for a fast snapshot (default: logs).",
    )
    parser.add_argument(
        "--limit",
        type=positive_int,
        default=50,
        help="Maximum number of posts to print (default: 50).",
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help="GoAccess WebSocket URL for --source dashboard (default: %(default)s).",
    )
    parser.add_argument(
        "--namespace",
        default=DEFAULT_NAMESPACE,
        help="Kubernetes namespace for --source logs (default: %(default)s).",
    )
    parser.add_argument(
        "--deployment",
        default=DEFAULT_DEPLOYMENT,
        help="Kubernetes deployment for --source logs (default: %(default)s).",
    )
    parser.add_argument(
        "--container",
        default=DEFAULT_CONTAINER,
        help="Kubernetes container for --source logs (default: %(default)s).",
    )
    parser.add_argument(
        "--log-path",
        default=DEFAULT_LOG_PATH,
        help="Path to the Nginx log in the GoAccess container (default: %(default)s).",
    )
    parser.add_argument(
        "--jobs",
        type=positive_int,
        default=2,
        choices=range(1, 7),
        help="GoAccess parsing workers for --source logs, from 1 to 6 (default: %(default)s).",
    )
    parser.add_argument(
        "--timeout",
        type=positive_float,
        default=15.0,
        help="WebSocket timeout for --source dashboard in seconds (default: %(default)s).",
    )
    parser.add_argument(
        "--version", action="version", version=f"goaccess-top-posts {VERSION}"
    )
    return parser.parse_args()


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def positive_float(value: str) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def is_post(path: str) -> bool:
    """Return whether a GoAccess request path represents a rendered post."""
    parsed = urlsplit(path)
    clean_path = parsed.path
    if parsed.query and "feed=" in parsed.query:
        return False
    if clean_path in NON_POST_PATHS or clean_path.startswith(STATIC_PREFIXES):
        return False
    return "." not in clean_path.rsplit("/", 1)[-1]


def load_dashboard_requests(url: str, timeout: float) -> list[dict[str, object]]:
    """Read the public dashboard's capped request snapshot."""
    try:
        with connect(
            url,
            origin="https://goaccess.waylonwalker.com",
            open_timeout=timeout,
            close_timeout=timeout,
        ) as socket:
            message = socket.recv(timeout=timeout)
    except (OSError, TimeoutError, WebSocketException) as error:
        raise RuntimeError(
            f"could not read GoAccess data from {url}: {error}"
        ) from error

    try:
        payload = json.loads(message)
        return payload["requests"]["data"]
    except (TypeError, ValueError, KeyError) as error:
        raise RuntimeError(
            "GoAccess returned an unexpected dashboard payload"
        ) from error


def load_log_requests(args: argparse.Namespace) -> list[dict[str, object]]:
    """Run GoAccess in-cluster so its full log is never copied locally."""
    command = [
        "kubectl",
        "exec",
        "--namespace",
        args.namespace,
        f"deployment/{args.deployment}",
        "--container",
        args.container,
        "--",
        "goaccess",
        args.log_path,
        "--log-format=COMBINED",
        f"--jobs={args.jobs}",
        "--max-items=10000",
        "--no-progress",
        "--no-parsing-spinner",
        "--output=json",
    ]
    try:
        result = subprocess.run(command, capture_output=True, check=False, text=True)
    except OSError as error:
        raise RuntimeError(f"could not run kubectl: {error}") from error
    if result.returncode != 0:
        detail = (
            result.stderr.strip().splitlines()[-1]
            if result.stderr.strip()
            else "no error output"
        )
        raise RuntimeError(f"GoAccess log analysis failed: {detail}")
    try:
        payload = json.loads(result.stdout)
        return payload["requests"]["data"]
    except (TypeError, ValueError, KeyError) as error:
        raise RuntimeError("GoAccess returned an unexpected log report") from error


def to_posts(requests: list[dict[str, object]]) -> list[Post]:
    """Keep content pages and rank them by unique visitors."""
    rows = [row for row in requests if is_post(str(row.get("data", "")))]
    rows.sort(
        key=lambda row: (int(row["visitors"]["count"]), int(row["hits"]["count"])),
        reverse=True,
    )
    return [
        Post(
            rank=index,
            path=str(row["data"]),
            visitors=int(row["visitors"]["count"]),
            hits=int(row["hits"]["count"]),
            bandwidth_bytes=int(row["bytes"]["count"]),
        )
        for index, row in enumerate(rows, start=1)
    ]


def human_bytes(value: int) -> str:
    units = ("B", "KiB", "MiB", "GiB", "TiB")
    amount = float(value)
    for unit in units:
        if amount < 1024 or unit == units[-1]:
            return f"{amount:.1f} {unit}" if unit != "B" else f"{value} B"
        amount /= 1024
    raise AssertionError("unreachable")


def render_table(posts: list[Post], wide: bool = False) -> str:
    headers = ["Rank", "Path", "Visitors", "Hits"]
    rows = [
        [str(post.rank), post.path, f"{post.visitors:,}", f"{post.hits:,}"]
        for post in posts
    ]
    if wide:
        headers.append("Bandwidth")
        for row, post in zip(rows, posts, strict=True):
            row.append(human_bytes(post.bandwidth_bytes))

    widths = [len(header) for header in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def format_row(row: list[str]) -> str:
        return "  ".join(
            value.ljust(widths[index]) for index, value in enumerate(row)
        ).rstrip()

    separator = "  ".join("-" * width for width in widths)
    return "\n".join(
        [format_row(headers), separator, *(format_row(row) for row in rows)]
    )


def render_markdown(posts: list[Post]) -> str:
    lines = ["| Rank | Path | Visitors | Hits |", "| ---: | --- | ---: | ---: |"]
    lines.extend(
        f"| {post.rank} | {post.path} | {post.visitors:,} | {post.hits:,} |"
        for post in posts
    )
    return "\n".join(lines)


def render_json(posts: list[Post]) -> str:
    return json.dumps([asdict(post) for post in posts], indent=2) + "\n"


def render_csv(posts: list[Post]) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=Post.__dataclass_fields__.keys())
    writer.writeheader()
    writer.writerows(asdict(post) for post in posts)
    return output.getvalue()


def render_list(posts: list[Post]) -> str:
    return "\n".join(post.path for post in posts) + ("\n" if posts else "")


def render_text(posts: list[Post]) -> str:
    return "\n".join(
        f"{post.rank}\t{post.path}\t{post.visitors}\t{post.hits}" for post in posts
    ) + ("\n" if posts else "")


def render(posts: list[Post], output_format: str) -> str:
    if output_format == "table":
        return render_table(posts) + "\n"
    if output_format == "markdown":
        return render_markdown(posts) + "\n"
    if output_format == "json":
        return render_json(posts)
    if output_format == "csv":
        return render_csv(posts)
    if output_format == "wide":
        return render_table(posts, wide=True) + "\n"
    if output_format == "list":
        return render_list(posts)
    return render_text(posts)


def main() -> int:
    args = parse_args()
    if sys.stderr.isatty():
        source_description = (
            "Nginx access logs" if args.source == "logs" else "dashboard data"
        )
        print(f"Fetching GoAccess {source_description}...", file=sys.stderr)
    try:
        requests = (
            load_log_requests(args)
            if args.source == "logs"
            else load_dashboard_requests(args.url, args.timeout)
        )
        posts = to_posts(requests)[: args.limit]
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    sys.stdout.write(render(posts, args.format))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
