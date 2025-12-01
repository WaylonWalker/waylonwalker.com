#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
#     "typer",
#     "jinja2",
# ]
# ///

from datetime import datetime
from jinja2 import Template
import os
import re
import requests
import typer

# GitHub API URL for starred repositories
GITHUB_API_STARS = (
    "https://api.github.com/users/{username}/starred?page={page}&per_page=100"
)

# Blog post directory
POSTS_DIR = "pages/stars"

# Post templates
TEMPLATES = [
    "I like [{{ owner }}'s]({{ owner_link }}) project [{{ repo }}]({{ repo_link }}).\n\n{{ description }}",
    "Check out [{{ owner }}]({{ owner_link }}) and their project [{{ repo }}]({{ repo_link }}).\n\n{{ description }}",
    "I'm impressed by [{{ repo }}]({{ repo_link }}) from [{{ owner }}]({{ owner_link }}).\n\n{{ description }}",
    "I recently discovered [{{ repo }}]({{ repo_link }}) by [{{ owner }}]({{ owner_link }}), and it's truly impressive.\n\n{{ description }}",
    "Check out [{{ repo }}]({{ repo_link }}) by [{{ owner }}]({{ owner_link }}). It's a well-crafted project with great potential.\n\n{{ description }}",
    "I'm really excited about [{{ repo }}]({{ repo_link }}), an amazing project by [{{ owner }}]({{ owner_link }}). It's worth exploring!\n\n{{ description }}",
    "[{{ owner }}]({{ owner_link }}) has done a fantastic job with [{{ repo }}]({{ repo_link }}). Highly recommend taking a look.\n\n{{ description }}",
    "If you're into interesting projects, don't miss out on [{{ repo }}]({{ repo_link }}), created by [{{ owner }}]({{ owner_link }}).\n\n{{ description }}",
    "[{{ repo }}]({{ repo_link }}) by [{{ owner }}]({{ owner_link }}) is a game-changer in its space. Excited to see how it evolves.\n\n{{ description }}",
    "I came across [{{ repo }}]({{ repo_link }}) from [{{ owner }}]({{ owner_link }}), and it's packed with great features and ideas.\n\n{{ description }}",
    "Looking for inspiration? [{{ repo }}]({{ repo_link }}) by [{{ owner }}]({{ owner_link }}).\n\n{{ description }}",
    "Just starred [{{ repo }}]({{ repo_link }}) by [{{ owner }}]({{ owner_link }}). It's an exciting project with a lot to offer.\n\n{{ description }}",
    "The work on [{{ repo }}]({{ repo_link }}) by [{{ owner }}]({{ owner_link }}).\n\n{{ description }}",
]


def clean_string(s: str) -> str:
    """Clean string to remove special characters for file paths."""
    return re.sub(r"[^a-zA-Z0-9_-]", "-", s)


def generate_post(owner: str, repo: str, description: str, starred_at: str) -> str:
    """Generate the blog post content from a random template."""
    template_str = TEMPLATES[hash(repo) % len(TEMPLATES)]
    template = Template(template_str)
    body = template.render(
        owner=owner,
        repo=repo,
        owner_link=f"https://github.com/{owner}",
        repo_link=f"https://github.com/{owner}/{repo}",
        description=description or "No description available.",
    )

    post_content = f"""---
date: {starred_at}
templateKey: stars
title: ⭐ {owner} {repo}
tags:
  - github-stars
published: True

---

{body}
"""
    return post_content


def save_post(owner: str, repo: str, content: str):
    """Save the generated post content to the appropriate file path."""
    clean_owner = clean_string(owner)
    clean_repo = clean_string(repo)
    post_path = os.path.join(POSTS_DIR, f"{clean_owner}--{clean_repo}.md")

    if os.path.exists(post_path):
        return

    os.makedirs(os.path.dirname(post_path), exist_ok=True)
    with open(post_path, "w") as f:
        f.write(content)

    print(f"Processed: {post_path}")


def fetch_github_stars(username: str, token: str):
    """Fetch all starred repositories from GitHub with pagination."""
    headers = (
        {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3.star+json",
        }
        if token
        else {}
    )
    stars = []
    page = 1
    while True:
        response = requests.get(
            GITHUB_API_STARS.format(username=username, page=page), headers=headers
        )
        response.raise_for_status()
        page_data = response.json()
        for repo in page_data:
            if repo.get("repo", {}).get("owner") is None:
                print(
                    f"Skipping repository without owner: {repo.get('repo', {}).get('name')}"
                )
                continue
            stars.append(
                {
                    "owner": repo["repo"]["owner"]["login"],
                    "name": repo["repo"]["name"],
                    "description": repo["repo"].get("description", ""),
                    "starred_at": repo.get(
                        "starred_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    ),
                }
            )
        if not page_data:
            break
        page += 1
    return stars


def main(
    username: str,
    token: str = typer.Option(
        None, help="GitHub personal access token for authentication."
    ),
):
    """Main function to fetch stars and generate blog posts."""
    stars = fetch_github_stars(username, token)
    for repo in stars:
        post_content = generate_post(
            repo["owner"], repo["name"], repo["description"], repo["starred_at"]
        )
        save_post(repo["owner"], repo["name"], post_content)


if __name__ == "__main__":
    typer.run(main)
