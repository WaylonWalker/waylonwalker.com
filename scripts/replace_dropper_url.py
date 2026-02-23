#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# ///

from __future__ import annotations

import argparse
from pathlib import Path

OLD_URL = b"https://dropper.wayl.one"
NEW_URL = b"https://dropper.waylonwalker.com"
SCRIPT_PATH = Path(__file__).resolve()
SKIP_DIRS = {
    ".git",
    ".markata",
    ".venv",
    "__pycache__",
    "node_modules",
    "output",
}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def preview_replacements(content: bytes, limit: int = 3) -> list[str]:
    old = OLD_URL.decode("utf-8")
    new = NEW_URL.decode("utf-8")

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        return []

    previews: list[str] = []
    for line in text.splitlines():
        if old not in line:
            continue

        previews.append(line.replace(old, f"{old} -> {new}"))
        if len(previews) >= limit:
            break

    return previews


def replace_urls(root: Path, dry_run: bool = False) -> tuple[int, int]:
    files_changed = 0
    replacements = 0

    for path in root.rglob("*"):
        if path.is_dir() or should_skip(path):
            continue
        if path.resolve() == SCRIPT_PATH:
            continue

        try:
            content = path.read_bytes()
        except OSError:
            continue

        count = content.count(OLD_URL)
        if count == 0:
            continue

        updated = content.replace(OLD_URL, NEW_URL)
        if not dry_run:
            path.write_bytes(updated)

        files_changed += 1
        replacements += count
        prefix = "would update" if dry_run else "updated"
        print(f"{prefix} {path} ({count} replacements)")

        if dry_run:
            for preview in preview_replacements(content):
                print(f"  {preview}")

    return files_changed, replacements


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Replace all https://dropper.wayl.one references with "
            "https://dropper.waylonwalker.com"
        )
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root path to scan (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show files that would be updated without writing changes",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.path).resolve()

    if not root.exists():
        print(f"error: path does not exist: {root}")
        return 1

    files_changed, replacements = replace_urls(root=root, dry_run=args.dry_run)
    action = "would update" if args.dry_run else "updated"
    print(f"{action} {files_changed} files with {replacements} replacements")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
