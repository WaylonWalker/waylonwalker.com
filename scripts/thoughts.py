#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
#     "typer",
# ]
# ///

import os
import re
from urllib.parse import urlsplit, urlunsplit

import requests
import typer
from datetime import datetime

THOUGHTS_API_URL = (
    "https://thoughts.waylonwalker.com/posts/waylonwalker/?page_size=9999999999"
)
POSTS_DIR = "pages/thoughts"
CANONICAL_DROPPER_HOST = "dropper.waylonwalker.com"


def clean_title(title: str) -> str:
    title = title.replace("💭", "")
    title = re.sub(r"\(\d+[^)]*\)", "", title)
    title = title.strip()
    if len(title) > 65:
        title = title[:62] + "..."
    return title


def format_date(date_str: str) -> str:
    dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def canonicalize_dropper_url(url: str) -> str:
    parts = urlsplit(url)
    host = parts.hostname
    if host not in {"dropper.wayl.one", CANONICAL_DROPPER_HOST}:
        return url

    netloc = CANONICAL_DROPPER_HOST
    if parts.port is not None:
        netloc = f"{netloc}:{parts.port}"
    scheme = "https"
    return urlunsplit((scheme, netloc, parts.path, parts.query, parts.fragment))


def normalize_dropper_urls(text: str) -> str:
    return re.sub(
        r"https?://(?:dropper\.wayl\.one|dropper\.waylonwalker\.com)[^\s)\]>\"']*",
        lambda match: canonicalize_dropper_url(match.group(0)),
        text,
    )


def generate_post(post: dict) -> str:
    cleaned_title = clean_title(post["title"])
    title = cleaned_title.replace("'", "''")
    tags = [tag.strip() for tag in post["tags"].split(",")]
    # tags.append("thoughts")
    tags.append("thought")
    # tags.append("link")
    link = (
        post.get("link") or f"https://waylonwalker.com/thoughts/thought-{post['id']}/"
    )
    link = normalize_dropper_urls(link)
    date = format_date(post["date"])
    message = normalize_dropper_urls(post["message"])

    tags_yaml = "\n".join(f"  - {tag}" for tag in tags)

    content = f"""---
title: '{title}'
date: {date}
template: link
link: {link}
tags:
{tags_yaml}
published: true

---

![[{link}]]

{message}
"""
    return content


def save_post(post_id: int, content: str):
    post_path = os.path.join(POSTS_DIR, f"thought-{post_id}.md")
    os.makedirs(os.path.dirname(post_path), exist_ok=True)
    with open(post_path, "w") as f:
        f.write(content)
    print(f"Processed: {post_path}")


def main():
    response = requests.get(THOUGHTS_API_URL)
    response.raise_for_status()
    posts = response.json()

    for post in posts:
        post_content = generate_post(post)
        save_post(post["id"], post_content)


if __name__ == "__main__":
    typer.run(main)
