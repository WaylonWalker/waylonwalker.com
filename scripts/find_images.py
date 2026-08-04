#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "typer>=0.12.5",
#   "rich>=13.7.0",
# ]
# ///
"""Search blog image metadata and find posts that reference those images."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Annotated, Any, Iterable
from urllib.parse import urlparse

import typer
from rich.console import Console
from rich.table import Table

APP_NAME = "blog-images"
DEFAULT_JSON_ENV = "IMAGE_DESCRIPTIONS_JSON"
DEFAULT_CONTENT_ENV = "BLOG_CONTENT_DIR"
DEFAULT_JSON_PATH = "image_descriptions.json"
DEFAULT_CONTENT_PATH = "."

IMAGE_EXTENSIONS = {
    ".avif",
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".webp",
}
POST_EXTENSIONS = {
    ".md",
    ".mdx",
    ".markdown",
    ".html",
    ".htm",
    ".jinja",
    ".jinja2",
    ".njk",
    ".toml",
    ".yaml",
    ".yml",
    ".json",
}
NON_IMAGE_TYPES = {"video"}

stdout = Console()
stderr = Console(stderr=True)

app = typer.Typer(
    name=APP_NAME,
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode="rich",
    help=(
        "Find images from an image_descriptions.json file, filter by tags/search text, "
        "and optionally join each image to blog posts that reference it."
    ),
    epilog=(
        "Config env vars: IMAGE_DESCRIPTIONS_JSON=/path/to/image_descriptions.json "
        "BLOG_CONTENT_DIR=/path/to/content"
    ),
)


class MatchMode(str, Enum):
    all = "all"
    any = "any"


class OutputFormat(str, Enum):
    table = "table"
    json = "json"
    jsonl = "jsonl"
    urls = "urls"
    keys = "keys"
    markdown = "markdown"


class UrlStyle(str, Enum):
    strict = "strict"
    any = "any"


@dataclass(frozen=True)
class ImageRecord:
    key: str
    url: str
    kind: str
    tags: list[str]
    description: str
    created_at: str | None
    updated_at: str | None
    raw: dict[str, Any]


@dataclass
class PostMatch:
    path: Path
    line_numbers: set[int] = field(default_factory=set)
    matched_terms: set[str] = field(default_factory=set)


@dataclass(frozen=True)
class Filters:
    tags: tuple[str, ...] = ()
    search_terms: tuple[str, ...] = ()
    match: MatchMode = MatchMode.all
    include_videos: bool = False
    limit: int = 0


JsonPathOption = Annotated[
    Path,
    typer.Option(
        "--json",
        "-j",
        envvar=DEFAULT_JSON_ENV,
        help=(
            "Path to image description JSON. "
            f"Can also be set with ${DEFAULT_JSON_ENV}."
        ),
        show_envvar=True,
        show_default=True,
    ),
]

ContentDirOption = Annotated[
    Path,
    typer.Option(
        "--content",
        "-c",
        envvar=DEFAULT_CONTENT_ENV,
        help=(
            "Blog content directory to scan for post references. "
            f"Can also be set with ${DEFAULT_CONTENT_ENV}."
        ),
        show_envvar=True,
        show_default=True,
    ),
]

TagsOption = Annotated[
    list[str] | None,
    typer.Option(
        "--tag",
        "-t",
        help="Exact tag to require. Repeatable: --tag blog --tag website",
    ),
]

SearchOption = Annotated[
    list[str] | None,
    typer.Option(
        "--search",
        "-s",
        help="Case-insensitive search across key, URL, type, tags, and description. Repeatable.",
    ),
]

MatchOption = Annotated[
    MatchMode,
    typer.Option(
        "--match",
        help="How repeated --tag and --search filters are combined.",
        case_sensitive=False,
    ),
]

FormatOption = Annotated[
    OutputFormat,
    typer.Option(
        "--format",
        "-f",
        help="Output format. Use json/jsonl for scripts and table for humans.",
        case_sensitive=False,
    ),
]

IncludeVideosOption = Annotated[
    bool,
    typer.Option(
        "--include-videos",
        help="Include video records. By default, only image-like extensions are returned.",
    ),
]

LimitOption = Annotated[
    int,
    typer.Option(
        "--limit",
        min=0,
        help="Limit result count. 0 means no limit.",
    ),
]

UrlStyleOption = Annotated[
    UrlStyle,
    typer.Option(
        "--url-style",
        help=(
            "Post matching style. 'strict' searches key + exact URL. "
            "'any' also tries http/https variants, path, and filename."
        ),
        case_sensitive=False,
    ),
]


@app.callback()
def main_callback() -> None:
    """Search blog image metadata without requiring installation."""


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().casefold())


def error(message: str, exit_code: int = 2) -> None:
    """Print errors to stderr and exit with a non-zero status."""
    stderr.print(f"[red]error:[/] {message}")
    raise typer.Exit(exit_code)


def validate_json_path(path: Path) -> Path:
    path = path.expanduser()
    if not path.exists():
        error(
            f"JSON file not found: {path}. Set ${DEFAULT_JSON_ENV} or pass --json /path/to/file.json."
        )
    if not path.is_file():
        error(f"JSON path is not a file: {path}")
    return path


def validate_content_dir(path: Path) -> Path:
    path = path.expanduser()
    if not path.exists():
        error(
            f"content directory not found: {path}. Set ${DEFAULT_CONTENT_ENV} or pass --content /path/to/content."
        )
    if not path.is_dir():
        error(f"content path is not a directory: {path}")
    return path


def load_json(path: Path) -> dict[str, Any]:
    path = validate_json_path(path)
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        error(f"invalid JSON: {path}:{e.lineno}:{e.colno} {e.msg}")

    if not isinstance(data, dict):
        error("expected top-level JSON object keyed by filename or URL")

    return data


def is_image_record(key: str, item: dict[str, Any]) -> bool:
    kind = str(item.get("type", "")).casefold()
    if kind in NON_IMAGE_TYPES:
        return False

    key_suffix = Path(key).suffix.casefold()
    url_suffix = Path(str(item.get("url", "")).split("?", 1)[0]).suffix.casefold()
    return key_suffix in IMAGE_EXTENSIONS or url_suffix in IMAGE_EXTENSIONS


def record_from_item(key: str, value: dict[str, Any]) -> ImageRecord:
    tags = value.get("tags") or []
    if not isinstance(tags, list):
        tags = []

    return ImageRecord(
        key=key,
        url=str(value.get("url") or ""),
        kind=str(value.get("type") or ""),
        tags=[str(tag) for tag in tags],
        description=str(value.get("description") or ""),
        created_at=value.get("created_at"),
        updated_at=value.get("updated_at"),
        raw=value,
    )


def iter_records(data: dict[str, Any], include_videos: bool = False) -> Iterable[ImageRecord]:
    for key, value in data.items():
        if not isinstance(value, dict):
            continue
        if not include_videos and not is_image_record(key, value):
            continue
        yield record_from_item(key, value)


def tag_matches(record: ImageRecord, wanted_tags: tuple[str, ...], match: MatchMode) -> bool:
    if not wanted_tags:
        return True

    record_tags = {normalize(tag) for tag in record.tags}
    wanted = [normalize(tag) for tag in wanted_tags]

    if match is MatchMode.all:
        return all(tag in record_tags for tag in wanted)
    return any(tag in record_tags for tag in wanted)


def search_matches(record: ImageRecord, terms: tuple[str, ...], match: MatchMode) -> bool:
    if not terms:
        return True

    haystack = normalize(
        " ".join(
            [
                record.key,
                record.url,
                record.kind,
                record.description,
                " ".join(record.tags),
            ]
        )
    )
    needles = [normalize(term) for term in terms]

    if match is MatchMode.all:
        return all(term in haystack for term in needles)
    return any(term in haystack for term in needles)


def select_records(data: dict[str, Any], filters: Filters) -> list[ImageRecord]:
    records = [
        record
        for record in iter_records(data, include_videos=filters.include_videos)
        if tag_matches(record, filters.tags, filters.match)
        and search_matches(record, filters.search_terms, filters.match)
    ]
    records.sort(key=lambda r: (r.created_at or "", r.key), reverse=True)
    if filters.limit > 0:
        return records[: filters.limit]
    return records


def url_variants(url: str) -> set[str]:
    if not url:
        return set()

    variants = {url}
    if url.startswith("http://"):
        variants.add("https://" + url.removeprefix("http://"))
    elif url.startswith("https://"):
        variants.add("http://" + url.removeprefix("https://"))

    parsed = urlparse(url)
    if parsed.path:
        variants.add(parsed.path)
        variants.add(Path(parsed.path).name)

    return {v for v in variants if v}


def image_terms(record: ImageRecord, style: UrlStyle) -> set[str]:
    terms = {record.key, Path(record.key).name}
    if record.url:
        terms.add(record.url)
    if style is UrlStyle.any:
        terms |= url_variants(record.url)
    return {term for term in terms if term}


def iter_post_files(content_dir: Path) -> Iterable[Path]:
    for path in content_dir.rglob("*"):
        if path.is_file() and path.suffix.casefold() in POST_EXTENSIONS:
            yield path


def post_globs() -> list[str]:
    return [f"*.{suffix.removeprefix('.')}" for suffix in sorted(POST_EXTENSIONS)]


def find_posts_for_records_python(
    records: list[ImageRecord],
    content_dir: Path,
    url_style: UrlStyle,
) -> dict[str, list[PostMatch]]:
    """Portable fallback. Slower than ripgrep, but has no external dependency."""
    terms_by_key = {record.key: image_terms(record, url_style) for record in records}
    matches: dict[str, dict[Path, PostMatch]] = {record.key: {} for record in records}

    for path in iter_post_files(content_dir):
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue

        for line_number, line in enumerate(lines, start=1):
            for record in records:
                for term in terms_by_key[record.key]:
                    if term in line:
                        post_match = matches[record.key].setdefault(path, PostMatch(path=path))
                        post_match.line_numbers.add(line_number)
                        post_match.matched_terms.add(term)

    return {
        key: sorted(post_matches.values(), key=lambda match: str(match.path))
        for key, post_matches in matches.items()
    }


def find_posts_for_records_rg(
    records: list[ImageRecord],
    content_dir: Path,
    url_style: UrlStyle,
) -> dict[str, list[PostMatch]]:
    """Use ripgrep to search all image terms in one pass.

    rg does the directory walking and text search in optimized Rust code. We emit JSON so
    paths, line numbers, and exact matched terms are reliable and script-friendly.
    """
    rg = shutil.which("rg")
    if rg is None:
        return find_posts_for_records_python(records, content_dir, url_style)

    term_to_keys: dict[str, set[str]] = {}
    for record in records:
        for term in image_terms(record, url_style):
            term_to_keys.setdefault(term, set()).add(record.key)

    matches: dict[str, dict[Path, PostMatch]] = {record.key: {} for record in records}
    if not term_to_keys:
        return {record.key: [] for record in records}

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as pattern_file:
        pattern_path = Path(pattern_file.name)
        for term in sorted(term_to_keys, key=len, reverse=True):
            pattern_file.write(term)
            pattern_file.write("\n")

    try:
        cmd = [
            rg,
            "--json",
            "--fixed-strings",
            "--line-number",
            "--with-filename",
            "--no-heading",
            "--ignore-case",
            "-f",
            str(pattern_path),
        ]
        for glob in post_globs():
            cmd.extend(["--glob", glob])
        cmd.append(str(content_dir))

        completed = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="ignore",
            check=False,
        )

        # rg exits 1 for no matches. That is not an error.
        if completed.returncode not in (0, 1):
            stderr.print("[yellow]warning:[/] rg failed; falling back to Python scanner. Try --no-rg to force Python intentionally.")
            if completed.stderr.strip():
                stderr.print(completed.stderr.strip())
            return find_posts_for_records_python(records, content_dir, url_style)

        for raw_line in completed.stdout.splitlines():
            try:
                event = json.loads(raw_line)
            except json.JSONDecodeError:
                continue

            if event.get("type") != "match":
                continue

            data = event.get("data", {})
            path_text = data.get("path", {}).get("text")
            line_number = data.get("line_number")
            submatches = data.get("submatches", [])
            if not path_text or not isinstance(line_number, int):
                continue

            path = Path(path_text)
            for submatch in submatches:
                term = submatch.get("match", {}).get("text")
                if not term:
                    continue
                for key in term_to_keys.get(term, set()):
                    post_match = matches[key].setdefault(path, PostMatch(path=path))
                    post_match.line_numbers.add(line_number)
                    post_match.matched_terms.add(term)

        return {
            key: sorted(post_matches.values(), key=lambda match: str(match.path))
            for key, post_matches in matches.items()
        }
    finally:
        try:
            pattern_path.unlink()
        except OSError:
            pass


def find_posts_for_records(
    records: list[ImageRecord],
    content_dir: Path,
    url_style: UrlStyle,
    use_rg: bool = True,
) -> dict[str, list[PostMatch]]:
    if use_rg:
        return find_posts_for_records_rg(records, content_dir, url_style)
    return find_posts_for_records_python(records, content_dir, url_style)


def image_to_dict(record: ImageRecord, posts: list[PostMatch] | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {
        "key": record.key,
        "url": record.url,
        "type": record.kind,
        "tags": record.tags,
        "description": record.description,
        "created_at": record.created_at,
        "updated_at": record.updated_at,
    }
    if posts is not None:
        item["posts"] = [
            {
                "path": str(match.path),
                "line_numbers": sorted(match.line_numbers),
                "matched_terms": sorted(match.matched_terms),
            }
            for match in posts
        ]
    return item


def emit_image_table(records: list[ImageRecord]) -> None:
    table = Table(title=f"Matched images: {len(records)}")
    table.add_column("Key", overflow="fold")
    table.add_column("Type", no_wrap=True)
    table.add_column("Tags", overflow="fold")
    table.add_column("Description", overflow="fold")
    table.add_column("URL", overflow="fold")

    for record in records:
        table.add_row(
            record.key,
            record.kind,
            ", ".join(record.tags),
            record.description,
            record.url,
        )

    stdout.print(table)


def emit_posts_table(records: list[ImageRecord], post_matches: dict[str, list[PostMatch]]) -> None:
    rows: list[tuple[ImageRecord, PostMatch | None]] = []
    for record in records:
        posts = post_matches.get(record.key, [])
        if posts:
            for post in posts:
                rows.append((record, post))
        else:
            rows.append((record, None))

    table = Table(title=f"Matched image/post rows: {len(rows)} | Images: {len(records)}")
    table.add_column("Image", overflow="fold")
    table.add_column("Tags", overflow="fold")
    table.add_column("Post", overflow="fold")
    table.add_column("Lines", overflow="fold")
    table.add_column("URL", overflow="fold")

    for record, post in rows:
        table.add_row(
            record.key,
            ", ".join(record.tags),
            str(post.path) if post else "not found",
            ",".join(str(n) for n in sorted(post.line_numbers)) if post else "",
            record.url,
        )

    stdout.print(table)


def emit_images(records: list[ImageRecord], output_format: OutputFormat) -> None:
    if output_format is OutputFormat.json:
        print(json.dumps([image_to_dict(record) for record in records], indent=2))
    elif output_format is OutputFormat.jsonl:
        for record in records:
            print(json.dumps(image_to_dict(record), separators=(",", ":")))
    elif output_format is OutputFormat.urls:
        for record in records:
            print(record.url)
    elif output_format is OutputFormat.keys:
        for record in records:
            print(record.key)
    elif output_format is OutputFormat.markdown:
        for record in records:
            label = record.description or record.key
            print(f"- [{label}]({record.url})")
    else:
        emit_image_table(records)


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def emit_posts_markdown(records: list[ImageRecord], post_matches: dict[str, list[PostMatch]]) -> None:
    used_count = sum(1 for record in records if post_matches.get(record.key))
    unused_count = len(records) - used_count

    print("# Blog image usage report")
    print()
    print(f"- Images: **{len(records)}**")
    print(f"- Used in posts: **{used_count}**")
    print(f"- Not found in posts: **{unused_count}**")
    print()

    for index, record in enumerate(records, start=1):
        posts = post_matches.get(record.key, [])
        title = record.description or record.key

        print(f"## {index}. {markdown_escape(title)}")
        print()
        print(f"- **Image key:** `{record.key}`")
        print(f"- **Image URL:** [{record.url}]({record.url})" if record.url else "- **Image URL:** not set")
        print(f"- **Type:** `{record.kind or 'unknown'}`")
        print(f"- **Tags:** {', '.join(f'`{markdown_escape(tag)}`' for tag in record.tags) if record.tags else 'none'}")
        if record.created_at:
            print(f"- **Created:** `{record.created_at}`")
        if record.updated_at:
            print(f"- **Updated:** `{record.updated_at}`")
        print()

        if posts:
            print("### Posts using this image")
            print()
            for post in posts:
                lines = ", ".join(str(n) for n in sorted(post.line_numbers))
                matched = ", ".join(f"`{markdown_escape(term)}`" for term in sorted(post.matched_terms))
                post_path = str(post.path)
                print(f"- [`{post_path}`]({post_path})")
                print(f"  - Lines: {lines}")
                print(f"  - Matched: {matched}")
        else:
            print("### Posts using this image")
            print()
            print("- Not found in scanned content.")

        print()


def emit_posts(
    records: list[ImageRecord],
    post_matches: dict[str, list[PostMatch]],
    output_format: OutputFormat,
) -> None:
    if output_format is OutputFormat.json:
        print(
            json.dumps(
                [image_to_dict(record, post_matches.get(record.key, [])) for record in records],
                indent=2,
            )
        )
    elif output_format is OutputFormat.jsonl:
        for record in records:
            print(json.dumps(image_to_dict(record, post_matches.get(record.key, [])), separators=(",", ":")))
    elif output_format is OutputFormat.urls:
        for record in records:
            print(record.url)
    elif output_format is OutputFormat.keys:
        for record in records:
            print(record.key)
    elif output_format is OutputFormat.markdown:
        emit_posts_markdown(records, post_matches)
    else:
        emit_posts_table(records, post_matches)


def build_filters(
    tags: list[str] | None,
    search_terms: list[str] | None,
    match: MatchMode,
    include_videos: bool,
    limit: int,
) -> Filters:
    return Filters(
        tags=tuple(tags or ()),
        search_terms=tuple(search_terms or ()),
        match=match,
        include_videos=include_videos,
        limit=limit,
    )


@app.command("images")
def images_command(
    json_path: JsonPathOption = Path(DEFAULT_JSON_PATH),
    tags: TagsOption = None,
    search_terms: SearchOption = None,
    match: MatchOption = MatchMode.all,
    output_format: FormatOption = OutputFormat.table,
    include_videos: IncludeVideosOption = False,
    limit: LimitOption = 0,
) -> None:
    """List image records from the JSON metadata file."""
    data = load_json(json_path)
    records = select_records(
        data,
        build_filters(tags, search_terms, match, include_videos, limit),
    )
    emit_images(records, output_format)
    raise typer.Exit(0 if records else 1)


@app.command("posts")
def posts_command(
    json_path: JsonPathOption = Path(DEFAULT_JSON_PATH),
    content_dir: ContentDirOption = Path(DEFAULT_CONTENT_PATH),
    tags: TagsOption = None,
    search_terms: SearchOption = None,
    match: MatchOption = MatchMode.all,
    url_style: UrlStyleOption = UrlStyle.any,
    output_format: FormatOption = OutputFormat.table,
    use_rg: Annotated[
        bool,
        typer.Option(
            "--rg/--no-rg",
            help="Use ripgrep for fast post scanning when available. Falls back to Python if rg is missing.",
        ),
    ] = True,
    include_videos: IncludeVideosOption = False,
    only_used: Annotated[
        bool,
        typer.Option("--only-used", help="Only show images found in at least one post."),
    ] = False,
    only_unused: Annotated[
        bool,
        typer.Option("--only-unused", help="Only show images not found in any post."),
    ] = False,
    limit: LimitOption = 0,
) -> None:
    """List matching images and the blog posts that reference them."""
    if only_used and only_unused:
        error("--only-used and --only-unused cannot be used together")

    data = load_json(json_path)
    records = select_records(
        data,
        build_filters(tags, search_terms, match, include_videos, limit=0),
    )
    content_dir = validate_content_dir(content_dir)
    post_matches = find_posts_for_records(records, content_dir, url_style, use_rg=use_rg)

    if only_used:
        records = [record for record in records if post_matches.get(record.key)]
    elif only_unused:
        records = [record for record in records if not post_matches.get(record.key)]

    if limit > 0:
        records = records[:limit]

    emit_posts(records, post_matches, output_format)
    raise typer.Exit(0 if records else 1)


@app.command("tags")
def tags_command(
    json_path: JsonPathOption = Path(DEFAULT_JSON_PATH),
    search_terms: SearchOption = None,
    match: MatchOption = MatchMode.all,
    output_format: Annotated[
        OutputFormat,
        typer.Option(
            "--format",
            "-f",
            help="Output format. Supported here: table, json, jsonl, markdown.",
            case_sensitive=False,
        ),
    ] = OutputFormat.table,
    include_videos: IncludeVideosOption = False,
) -> None:
    """Summarize tags available in the JSON metadata file."""
    data = load_json(json_path)
    records = select_records(
        data,
        Filters(search_terms=tuple(search_terms or ()), match=match, include_videos=include_videos),
    )

    counts: dict[str, int] = {}
    for record in records:
        for tag in record.tags:
            counts[tag] = counts.get(tag, 0) + 1

    rows = sorted(counts.items(), key=lambda item: (-item[1], item[0].casefold()))

    if output_format is OutputFormat.json:
        print(json.dumps([{"tag": tag, "count": count} for tag, count in rows], indent=2))
    elif output_format is OutputFormat.jsonl:
        for tag, count in rows:
            print(json.dumps({"tag": tag, "count": count}, separators=(",", ":")))
    elif output_format is OutputFormat.markdown:
        for tag, count in rows:
            print(f"- `{tag}`: {count}")
    else:
        table = Table(title=f"Tags: {len(rows)}")
        table.add_column("Tag")
        table.add_column("Images", justify="right")
        for tag, count in rows:
            table.add_row(tag, str(count))
        stdout.print(table)

    raise typer.Exit(0 if rows else 1)


@app.command("doctor")
def doctor_command(
    json_path: JsonPathOption = Path(DEFAULT_JSON_PATH),
    content_dir: ContentDirOption = Path(DEFAULT_CONTENT_PATH),
) -> None:
    """Validate config paths and print a short diagnostic report."""
    json_path = validate_json_path(json_path)
    content_exists = content_dir.expanduser().is_dir()
    data = load_json(json_path)
    image_count = len(list(iter_records(data)))
    total_count = len([value for value in data.values() if isinstance(value, dict)])

    report = {
        "json_path": str(json_path),
        "rg_available": shutil.which("rg") is not None,
        "json_records": total_count,
        "image_records": image_count,
        "content_dir": str(content_dir.expanduser()),
        "content_dir_exists": content_exists,
        "env": {
            DEFAULT_JSON_ENV: os.environ.get(DEFAULT_JSON_ENV),
            DEFAULT_CONTENT_ENV: os.environ.get(DEFAULT_CONTENT_ENV),
        },
    }
    print(json.dumps(report, indent=2))
    raise typer.Exit(0 if content_exists else 1)


if __name__ == "__main__":
    app()

