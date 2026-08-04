#!/usr/bin/env -S uv run --quiet --script
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _normalize(value: str) -> str:
    return value.replace("\ufeff", "").replace("\x00", "").strip().strip('"')


def _detect_encoding(report: Path) -> str:
    prefix = report.read_bytes()[:4]
    if prefix.startswith(b"\xff\xfe") or prefix.startswith(b"\xfe\xff"):
        return "utf-16"
    if prefix.startswith(b"\xef\xbb\xbf"):
        return "utf-8-sig"
    return "cp1252"


def _preview(rows: list[dict[str, str]], limit: int) -> list[str]:
    urls: list[str] = []
    for row in rows[:limit]:
        for key in (
            "URL",
            "Source URL",
            "Target URL",
            "Redirect URL",
            "Final redirect URL",
            "Address",
            "Page",
            "Link",
        ):
            value = row.get(key)
            if value:
                urls.append(value)
                break
    return urls


def _load_rows(report: Path) -> tuple[list[dict[str, str]], list[str]]:
    encoding = _detect_encoding(report)
    with report.open(newline="", encoding=encoding, errors="replace") as handle:
        sample = handle.read(4096)
        handle.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",\t;")
        except csv.Error:
            dialect = csv.excel_tab if "\t" in sample else csv.excel

        reader = csv.DictReader(handle, dialect=dialect)
        fieldnames = [_normalize(name) for name in (reader.fieldnames or []) if name]
        rows: list[dict[str, str]] = []
        for row in reader:
            normalized_row = {
                _normalize(str(key)): _normalize(value)
                for key, value in row.items()
                if key is not None and value is not None
            }
            rows.append(normalized_row)
        return rows, fieldnames


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize Ahrefs CSV exports.")
    parser.add_argument("report_dir", type=Path)
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--bucket", default=None)
    args = parser.parse_args()

    report_dir: Path = args.report_dir
    top: int = args.top
    bucket: str | None = args.bucket

    if not report_dir.exists() or not report_dir.is_dir():
        raise SystemExit(f"{report_dir} is not a directory")

    reports: list[Path] = sorted(report_dir.glob("*.csv"))
    for report in reports:
        if bucket and bucket not in report.name:
            continue

        rows, fieldnames = _load_rows(report)

        print(f"\n## {report.name}")
        print(f"rows: {len(rows)}")

        if not rows:
            continue

        print(f"columns: {', '.join(fieldnames)}")

        counts: Counter[str] = Counter()
        for row in rows:
            for key in ("Type", "Issue", "Reason", "Status", "Category"):
                value = row.get(key)
                if value:
                    counts[value] += 1
                    break

        if counts:
            print("top labels:")
            for label, count in counts.most_common(5):
                print(f"  - {label}: {count}")

        preview = _preview(rows, top)
        if preview:
            print("preview:")
            for value in preview:
                print(f"  - {value}")


if __name__ == "__main__":
    main()
