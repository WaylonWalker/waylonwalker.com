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
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import unquote, urlparse, urlsplit, urlunsplit

import requests

DEFAULT_BASE_URL = "https://dropper.waylonwalker.com"
DEFAULT_TEMPLATE = Path.home() / ".copier-templates" / "shots"
CANONICAL_DROPPER_HOST = "dropper.waylonwalker.com"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
MIME_SUFFIXES = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/heic": ".heic",
    "image/heif": ".heif",
    "image/gif": ".gif",
}
UPLOAD_TIMEOUT = 120
METADATA_TIMEOUT = 30


@dataclass
class ClipboardImage:
    path: Path
    source_label: str
    source_kind: str


@dataclass
class UploadResult:
    url: str
    filename: str


def slugify(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug.strip("-") or "shot"


def default_title_from_path(path: Path) -> str:
    text = path.stem.replace("_", " ").replace("-", " ").strip()
    text = re.sub(r"\s+", " ", text)
    return text.title() if text else "Shot"


def run_command(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=check, text=True, capture_output=True)


def run_command_bytes(args: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(args, check=True, capture_output=True)


def command_path(name: str) -> str | None:
    return shutil.which(name)


def require_commands(*names: str) -> list[str]:
    return [name for name in names if command_path(name) is None]


def wayland_clipboard_types() -> list[str]:
    try:
        result = run_command(["wl-paste", "--list-types"])
    except subprocess.CalledProcessError:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def decode_file_uri(uri: str) -> Path | None:
    parsed = urlparse(uri)
    if parsed.scheme != "file":
        return None
    if parsed.netloc not in {"", "localhost"}:
        return None
    return Path(unquote(parsed.path))


def clipboard_file_uri() -> Path | None:
    types = set(wayland_clipboard_types())
    if "text/uri-list" not in types:
        return None
    try:
        result = run_command(["wl-paste", "--no-newline", "--type", "text/uri-list"])
    except subprocess.CalledProcessError:
        return None
    for line in result.stdout.splitlines():
        value = line.strip()
        if not value or value.startswith("#"):
            continue
        path = decode_file_uri(value)
        if path and path.is_file():
            return path
    return None


def preferred_image_type(types: list[str]) -> str | None:
    for mime in ("image/jpeg", "image/png", "image/webp", "image/heic", "image/heif", "image/gif"):
        if mime in types:
            return mime
    for mime in types:
        if mime.startswith("image/"):
            return mime
    return None


def copy_clipboard_image(tmpdir: Path) -> ClipboardImage:
    source_path = clipboard_file_uri()
    if source_path is not None:
        copied = tmpdir / source_path.name
        copied.write_bytes(source_path.read_bytes())
        return ClipboardImage(copied, str(source_path), "file")

    types = wayland_clipboard_types()
    mime_type = preferred_image_type(types)
    if mime_type is None:
        msg = "Clipboard does not contain a file URI or image data"
        raise RuntimeError(msg)

    suffix = MIME_SUFFIXES.get(mime_type) or mimetypes.guess_extension(mime_type) or ".bin"
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_path = tmpdir / f"clipboard-{timestamp}{suffix}"
    try:
        data = run_command_bytes(["wl-paste", "--no-newline", "--type", mime_type]).stdout
    except subprocess.CalledProcessError as exc:
        msg = f"Failed to read {mime_type} data from the clipboard"
        raise RuntimeError(msg) from exc
    output_path.write_bytes(data)
    return ClipboardImage(output_path, mime_type, "clipboard-image")


def exif_date(file_path: Path) -> str | None:
    if command_path("exiftool") is None:
        return None

    result = run_command(
        [
            "exiftool",
            "-s3",
            "-d",
            DATE_FORMAT,
            "-DateTimeOriginal",
            "-CreateDate",
            "-MediaCreateDate",
            "-FileModifyDate",
            str(file_path),
        ],
        check=False,
    )
    for line in result.stdout.splitlines():
        value = line.strip()
        if value:
            return value
    return None


def canonicalize_dropper_url(url: str) -> str:
    parts = urlsplit(url)
    if parts.hostname != "dropper.wayl.one":
        return url
    netloc = CANONICAL_DROPPER_HOST
    if parts.port is not None:
        netloc = f"{netloc}:{parts.port}"
    return urlunsplit((parts.scheme, netloc, parts.path, parts.query, parts.fragment))


def auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def upload_file(file_path: Path, base_url: str, token: str, timeout: int = UPLOAD_TIMEOUT) -> UploadResult:
    upload_url = f"{base_url.rstrip('/')}/api/upload?format=json"
    mime_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    headers = auth_headers(token)
    with file_path.open("rb") as handle:
        response = requests.post(
            upload_url,
            headers=headers,
            files={"file": (file_path.name, handle, mime_type)},
            timeout=timeout,
        )
    response.raise_for_status()
    payload = response.json()
    if "url" not in payload:
        msg = f"Upload succeeded but no URL returned for {file_path.name}"
        raise RuntimeError(msg)
    filename = str(payload.get("filename") or file_path.name)
    return UploadResult(url=canonicalize_dropper_url(str(payload["url"])), filename=filename)


def detect_media_kind(file_path: Path) -> str:
    mime_type = mimetypes.guess_type(file_path.name)[0] or ""
    if mime_type.startswith("video/"):
        return "video"
    if mime_type.startswith("image/"):
        return "image"
    return "file"


def resolve_dropper_media_id(
    base_url: str,
    token: str,
    *,
    candidate_filenames: list[str],
    media_kind: str,
    timeout: int = METADATA_TIMEOUT,
    attempts: int = 5,
    delay_seconds: float = 0.5,
) -> int | None:
    if media_kind not in {"image", "video", "file"}:
        return None

    wanted = {name for name in candidate_filenames if name}
    if not wanted:
        return None

    for attempt in range(attempts):
        response = requests.get(
            f"{base_url.rstrip('/')}/api/media/pending-analysis",
            headers=auth_headers(token),
            params={"media_kind": media_kind, "limit": 100},
            timeout=timeout,
        )
        if response.status_code == 503:
            return None
        response.raise_for_status()

        payload = response.json()
        items = payload.get("items") if isinstance(payload, dict) else None
        if isinstance(items, list):
            for item in items:
                if not isinstance(item, dict):
                    continue
                original_filename = str(item.get("original_filename") or item.get("filename") or "")
                storage_key = str(item.get("storage_key") or "")
                if original_filename not in wanted and storage_key not in wanted:
                    continue
                media_id = item.get("media_id")
                if isinstance(media_id, int):
                    return media_id
                if isinstance(media_id, str) and media_id.isdigit():
                    return int(media_id)
        if attempt < attempts - 1:
            time.sleep(delay_seconds)
    return None


def update_dropper_metadata(
    base_url: str,
    token: str,
    *,
    media_id: int,
    title: str,
    description: str,
    tags: list[str],
    timeout: int = METADATA_TIMEOUT,
) -> None:
    payload = {
        "analysis": {
            "type": "manual",
            "title": title,
            "description": description,
            "tags": tags,
            "status": "complete",
            "model": "clipboard-shot",
            "model_provider": "manual",
            "script_name": "clipboard_shot.py",
            "script_version": "1",
            "analysis_schema_version": "1",
            "prompt_version": "1",
        },
        "current_metadata": {
            "title": title,
            "description": description,
            "tags": tags,
            "review_status": "human_reviewed",
            "title_source": "manual",
            "description_source": "manual",
        },
    }
    response = requests.post(
        f"{base_url.rstrip('/')}/api/media/{media_id}/analysis-results",
        headers=auth_headers(token),
        json=payload,
        timeout=timeout,
    )
    response.raise_for_status()


def prompt(label: str, default: str) -> str:
    response = input(f"{label} [{default}]: ").strip()
    return response or default


def normalize_tags(tags: str) -> list[str]:
    values: list[str] = []
    seen: set[str] = set()
    for raw_tag in tags.split(","):
        tag = raw_tag.strip().lower()
        if not tag or tag in seen:
            continue
        seen.add(tag)
        values.append(tag)
    return values


def run_copier(
    template: Path,
    repo_root: Path,
    title: str,
    image: str,
    description: str,
    date: str,
    tags: str,
) -> None:
    command = [
        "uvx",
        "copier",
        "copy",
        "--trust",
        "--defaults",
        "-d",
        f"title={title}",
        "-d",
        f"image={image}",
        "-d",
        f"description={description}",
        "-d",
        f"date={date}",
        "-d",
        f"tags={tags}",
        str(template),
        str(repo_root),
    ]
    subprocess.run(command, check=True)


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Pull a shot from the Wayland clipboard, upload it to dropper, and run the shots copier template.",
    )
    parser.add_argument("--token", default=os.environ.get("DROPPER_TOKEN", ""))
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--title")
    parser.add_argument("--description")
    parser.add_argument("--tags")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.token:
        return fail("Missing DROPPER_TOKEN.")

    missing_commands = require_commands("wl-paste", "uvx")
    if missing_commands:
        missing = ", ".join(missing_commands)
        return fail(f"Missing required command(s): {missing}")

    if not args.template.exists():
        return fail(f"Missing shots copier template: {args.template}")

    try:
        with TemporaryDirectory(prefix="clipboard-shot-") as tmp:
            clipboard_image = copy_clipboard_image(Path(tmp))
            image_date = exif_date(clipboard_image.path)
            if image_date is None:
                image_date = datetime.fromtimestamp(clipboard_image.path.stat().st_mtime).strftime(DATE_FORMAT)
                if command_path("exiftool") is None:
                    print(
                        f"exiftool not found. Falling back to file time {image_date}.",
                        file=sys.stderr,
                    )
                else:
                    print(
                        f"No EXIF date found from {clipboard_image.source_label}. Falling back to {image_date}.",
                        file=sys.stderr,
                    )

            default_title = default_title_from_path(clipboard_image.path)
            title = args.title or prompt("Title", default_title)
            description = args.description or prompt("Description", title)
            extra_tags = normalize_tags(args.tags or prompt("Extra tags", ""))
            all_tags = ["shots", *extra_tags]
            tags = ", ".join(extra_tags)

            upload = upload_file(clipboard_image.path, args.base_url, args.token)
            media_kind = detect_media_kind(clipboard_image.path)
            media_id = resolve_dropper_media_id(
                args.base_url,
                args.token,
                candidate_filenames=[clipboard_image.path.name, upload.filename],
                media_kind=media_kind,
            )
            if media_id is None:
                print(
                    "Dropper metadata update skipped. Could not resolve media_id from pending-analysis.",
                    file=sys.stderr,
                )
            else:
                update_dropper_metadata(
                    args.base_url,
                    args.token,
                    media_id=media_id,
                    title=title,
                    description=description,
                    tags=all_tags,
                )

            run_copier(args.template, args.repo_root, title, upload.url, description, image_date, tags)
            print(f"Uploaded: {upload.url}")
            print(f"Date: {image_date}")
            print(f"Source: {clipboard_image.source_label}")
            print(f"Tags: shots{', ' + tags if tags else ''}")
            print(f"Slug: shots/{slugify(title)}")
    except RuntimeError as exc:
        return fail(str(exc))
    except requests.RequestException as exc:
        return fail(f"Dropper request failed: {exc}")
    except subprocess.CalledProcessError as exc:
        command = " ".join(str(part) for part in exc.cmd) if exc.cmd else "subprocess"
        return fail(f"Command failed: {command}")
    except KeyboardInterrupt:
        return fail("Cancelled.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
