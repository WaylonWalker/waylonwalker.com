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
import requests
import typer
from datetime import datetime

THOUGHTS_API_URL = (
    "https://thoughts.waylonwalker.com/posts/waylonwalker/?page_size=9999999999"
)
POSTS_DIR = "pages/thoughts"


def clean_title(title: str) -> str:
    title = re.sub(r"\(\d+[^)]*\)", "", title)
    title = title.strip()
    if len(title) > 65:
        title = title[:62] + "..."
    return title


def format_date(date_str: str) -> str:
    dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def generate_post(post: dict) -> str:
    cleaned_title = clean_title(post["title"])
    title = "💭 " + cleaned_title.lstrip("💭 ")
    title = title.replace("'", "''")
    tags = [tag.strip() for tag in post["tags"].split(",")]
    tags.append("thoughts")
    tags.append("thought")
    tags.append("link")
    link = (
        post.get("link") or f"https://waylonwalker.com/thoughts/thought-{post['id']}/"
    )
    date = format_date(post["date"])
    message = post["message"]

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

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
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
