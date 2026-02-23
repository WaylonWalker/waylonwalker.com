#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
# ]
# ///

from __future__ import annotations

import argparse
import mimetypes
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import requests

DEFAULT_SOURCE_DIR = Path(
    "/run/user/1000/gvfs/smb-share:server=192.168.1.168,share=waylon/"
    "waylonwalker-gaming/SilkSong/keeb-run-1"
)
DEFAULT_BASE_URL = "https://dropper.waylonwalker.com"
DEFAULT_OUTPUT_DIR = Path("./pages/shots")
REMOVE_TOKEN = "silksong-keebrun"
CANONICAL_DROPPER_HOST = "dropper.waylonwalker.com"
MAX_UPLOAD_BYTES = 100 * 1024 * 1024
RESAMPLE_DIR_NAME = "resample"

QUALITY_ORDER = {
    "1080p": 4,
    "720p": 3,
    "480p": 2,
    "vertical": 1,
}


@dataclass
class ShotMeta:
    source_file: Path
    stem_clean: str
    slug: str
    title: str
    description: str
    date_string: str
    output_file: Path


def clean_stem(file_path: Path) -> str:
    stem = file_path.stem.lower()
    stem = re.sub(rf"^{re.escape(REMOVE_TOKEN)}[-_]*", "", stem)
    stem = re.sub(rf"[-_]*{re.escape(REMOVE_TOKEN)}[-_]*", "-", stem)
    stem = re.sub(r"-{2,}", "-", stem).strip("-")
    return stem or file_path.stem.lower()


def normalize_slug(value: str) -> str:
    slug = value.lower().strip()
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"_+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug.strip("-")


def stem_to_title(stem: str) -> str:
    titleish = stem.replace("-", " ").replace("_", " ").strip()
    titleish = re.sub(r"\s+", " ", titleish)
    return titleish.title() if titleish else "Untitled"


def file_creation_timestamp(file_path: Path) -> float:
    stat = file_path.stat()
    birth = getattr(stat, "st_birthtime", None)
    if birth is not None:
        return float(birth)
    return float(stat.st_ctime)


def build_meta(file_path: Path, output_dir: Path) -> ShotMeta:
    stem_clean = clean_stem(file_path)
    slug = normalize_slug(stem_clean)
    if not slug:
        slug = normalize_slug(file_path.stem)
    if not slug:
        slug = "untitled"
    title = stem_to_title(stem_clean)
    date_value = datetime.fromtimestamp(file_creation_timestamp(file_path)).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    output_file = output_dir / f"{slug}.md"
    return ShotMeta(
        source_file=file_path,
        stem_clean=stem_clean,
        slug=slug,
        title=title,
        description=title,
        date_string=date_value,
        output_file=output_file,
    )


def render_markdown(meta: ShotMeta, image_url: str) -> str:
    return "\n".join(
        [
            "---",
            f"date: {meta.date_string}",
            "templateKey: shots",
            f"title: {meta.title}",
            "tags:",
            "  - shots",
            "  - hollow-knight-silksong",
            "published: True",
            f"slug: shots/{meta.slug}",
            f"image: {image_url}",
            f"description: {meta.description}",
            f"original: {meta.source_file.name}",
            "---",
            "",
            f"![{meta.title}]({image_url})",
            "",
            f"> {meta.description}",
            "",
        ]
    )


def canonicalize_dropper_url(url: str) -> str:
    parts = urlsplit(url)
    host = parts.hostname
    if host != "dropper.wayl.one":
        return url

    netloc = CANONICAL_DROPPER_HOST
    if parts.port is not None:
        netloc = f"{netloc}:{parts.port}"
    return urlunsplit((parts.scheme, netloc, parts.path, parts.query, parts.fragment))


def format_bytes(size_bytes: int) -> str:
    return f"{size_bytes / 1024 / 1024:.1f} MB"


def quality_rank(file_path: Path) -> int:
    stem_lower = file_path.stem.lower()
    for label, rank in QUALITY_ORDER.items():
        if stem_lower.endswith(f"-{label}"):
            return rank
    return 0


def pick_upload_source(
    file_path: Path, max_bytes: int
) -> tuple[Path | None, str | None]:
    source_size = file_path.stat().st_size
    if source_size <= max_bytes:
        return file_path, None

    resample_dir = file_path.parent / RESAMPLE_DIR_NAME
    if not resample_dir.exists() or not resample_dir.is_dir():
        return (
            None,
            f"source is {format_bytes(source_size)} and {resample_dir} is missing",
        )

    suffix_pattern = re.escape(file_path.suffix)
    stem_pattern = re.escape(file_path.stem)
    pattern = re.compile(
        rf"^{stem_pattern}-(1080p|720p|480p|vertical){suffix_pattern}$",
        re.IGNORECASE,
    )

    candidates: list[Path] = []
    for candidate in resample_dir.iterdir():
        if not candidate.is_file():
            continue
        if not pattern.match(candidate.name):
            continue
        if candidate.stat().st_size <= max_bytes:
            candidates.append(candidate)

    if not candidates:
        return (
            None,
            f"source is {format_bytes(source_size)} and no resample under 100 MB",
        )

    best = max(
        candidates,
        key=lambda path: (quality_rank(path), path.stat().st_size, path.name.lower()),
    )
    best_size = best.stat().st_size
    note = (
        f"source is {format_bytes(source_size)}; using {best.name} "
        f"({format_bytes(best_size)})"
    )
    return best, note


def upload_file(file_path: Path, base_url: str, timeout: int = 120) -> str:
    upload_url = f"{base_url.rstrip('/')}/api/upload?format=json"
    mime_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    with file_path.open("rb") as handle:
        response = requests.post(
            upload_url,
            files={"file": (file_path.name, handle, mime_type)},
            timeout=timeout,
        )
    response.raise_for_status()
    payload = response.json()
    if "url" not in payload:
        msg = f"Upload succeeded but no URL returned for {file_path.name}"
        raise RuntimeError(msg)
    return canonicalize_dropper_url(str(payload["url"]))


def iter_files(source_dir: Path) -> list[Path]:
    return sorted(
        [path for path in source_dir.iterdir() if path.is_file()],
        key=lambda path: path.name.lower(),
    )


def parse_frontmatter_fields(markdown_path: Path) -> tuple[str | None, str | None]:
    try:
        content = markdown_path.read_text(encoding="utf-8")
    except Exception:
        return None, None

    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None

    original: str | None = None
    slug: str | None = None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("original:"):
            original = line.split(":", 1)[1].strip()
        if line.startswith("slug:"):
            slug = line.split(":", 1)[1].strip()
    return original, slug


def existing_index(output_dir: Path) -> tuple[set[str], set[str]]:
    originals: set[str] = set()
    slugs: set[str] = set()
    if not output_dir.exists() or not output_dir.is_dir():
        return originals, slugs

    for md_file in output_dir.glob("*.md"):
        original, slug = parse_frontmatter_fields(md_file)
        if original:
            originals.add(original)
        if slug:
            slugs.add(slug)
    return originals, slugs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Upload keeb-run files to dropper and generate pages/shots markdown files."
        )
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=DEFAULT_SOURCE_DIR,
        help="Directory containing source files to import.",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help="Dropper base URL.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory where markdown files will be written.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned uploads and markdown writes without changing anything.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-upload and overwrite markdown even when duplicates are detected.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Only process the first N files (useful for testing).",
    )
    parser.add_argument(
        "--print-post",
        action="store_true",
        help="With --dry-run, print the full markdown post that would be written.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_dir: Path = args.source_dir
    output_dir: Path = args.output_dir

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Source directory does not exist: {source_dir}", file=sys.stderr)
        return 1

    files = iter_files(source_dir)
    if args.limit is not None:
        files = files[: max(0, args.limit)]
    if not files:
        print(f"No files found in {source_dir}")
        return 0

    existing_originals, existing_slugs = existing_index(output_dir)

    if args.dry_run:
        print("DRY RUN: no uploads or file writes will happen")
    else:
        output_dir.mkdir(parents=True, exist_ok=True)

    if args.limit is not None:
        print(f"Processing limit: {args.limit}")

    for file_path in files:
        meta = build_meta(file_path, output_dir)
        slug_value = f"shots/{meta.slug}"
        upload_source, upload_note = pick_upload_source(file_path, MAX_UPLOAD_BYTES)
        if upload_source is None:
            print(f"skipping {file_path.name}: {upload_note}")
            continue

        duplicate_reasons: list[str] = []
        if file_path.name in existing_originals:
            duplicate_reasons.append("original")
        if slug_value in existing_slugs:
            duplicate_reasons.append("slug")
        if meta.output_file.exists():
            duplicate_reasons.append("output-file")

        if duplicate_reasons and not args.force:
            print(
                f"skipping {file_path.name}: duplicate detected ({', '.join(duplicate_reasons)})"
            )
            continue

        if args.dry_run:
            duplicate_note = ""
            if duplicate_reasons:
                duplicate_note = f" (duplicate: {', '.join(duplicate_reasons)})"

            if duplicate_reasons and args.force:
                print(f"- would force upload: {file_path}{duplicate_note}")
            else:
                print(f"- would upload: {upload_source}{duplicate_note}")
            print(
                f"  upload endpoint: {args.base_url.rstrip('/')}/api/upload?format=json"
            )
            print(f"  source file: {file_path.name}")
            print(f"  source size: {format_bytes(file_path.stat().st_size)}")
            if upload_source != file_path:
                print(f"  upload file: {upload_source.name}")
            if upload_note:
                print(f"  upload choice: {upload_note}")
            print(f"  title: {meta.title}")
            print(f"  date to use: {meta.date_string}")
            print(f"  expected slug: {slug_value}")
            print(f"  would write: {meta.output_file}")
            if args.print_post:
                dry_run_image_url = f"{args.base_url.rstrip('/')}/<uploaded-file-url>"
                markdown_preview = render_markdown(meta, dry_run_image_url)
                print("  markdown preview:")
                print(markdown_preview)
            continue

        try:
            image_url = upload_file(upload_source, args.base_url)
            markdown = render_markdown(meta, image_url)
            meta.output_file.write_text(markdown, encoding="utf-8")
            existing_originals.add(file_path.name)
            existing_slugs.add(slug_value)
            if upload_source != file_path:
                print(
                    f"uploaded {upload_source.name} for {file_path.name} -> {image_url}"
                )
            else:
                print(f"uploaded {file_path.name} -> {image_url}")
            print(f"wrote {meta.output_file}")
        except Exception as exc:
            print(f"failed {file_path.name}: {exc}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
