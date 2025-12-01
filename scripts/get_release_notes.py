#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.10"
# ///

import sys


def get_release_notes(version):
    with open("CHANGELOG.md", "r") as f:
        content = f.read()

    sections = content.split("\n## ")
    # First section won't start with ## since it's split on that
    sections = ["## " + s if i > 0 else s for i, s in enumerate(sections)]

    for section in sections:
        if section.startswith(f"## {version}"):
            return section.strip()

    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: get_release_notes.py VERSION", file=sys.stderr)
        sys.exit(1)

    version = sys.argv[1]
    notes = get_release_notes(version)
    if notes:
        print(notes)
    else:
        print(f"Error: No release notes found for version {version}", file=sys.stderr)
        sys.exit(1)
