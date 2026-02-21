#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
#     "beautifulsoup4",
#     "typer",
#     "tomli",
# ]
# ///

import os
import re
import requests
import typer
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import tomli

POSTS_DIR = "pages/thoughts"
CONFIG_FILE = "markata-go.toml"

COMMON_FEED_PATHS = [
    "/feed",
    "/feed.xml",
    "/rss",
    "/rss.xml",
    "/atom.xml",
    "/index.xml",
    "/blog/feed",
    "/blog/rss",
    "/feeds/posts/default",
    "/blog-feed.xml",
    "/feed/rss",
    "/atom",
    "/feed/atom",
]

FEED_MIME_TYPES = [
    "application/rss+xml",
    "application/atom+xml",
    "application/xml",
    "text/xml",
]


def get_existing_feeds(config_path: str) -> set:
    """Extract existing blogroll feeds from config."""
    with open(config_path, "rb") as f:
        config = tomli.load(f)
    feeds = set()
    for feed in config.get("markata-go", {}).get("blogroll", {}).get("feeds", []):
        feeds.add(feed.get("url", "").lower())
        feeds.add(feed.get("site_url", "").lower())
    return feeds


def get_thought_links(posts_dir: str) -> list:
    """Extract unique links from thought files."""
    links = set()
    posts_path = Path(posts_dir)

    for md_file in posts_path.glob("*.md"):
        content = md_file.read_text()
        match = re.search(r"^link:\s*(.+)$", content, re.MULTILINE)
        if match:
            link = match.group(1).strip()
            if link and not link.startswith("/"):
                links.add(link)

    return sorted(links)


def get_homepage_url(url: str) -> str:
    """Get the homepage/canonical URL for a given URL."""
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}/"


def fetch_url(url: str, timeout: float = 5.0) -> requests.Response | None:
    """Fetch a URL with timeout."""
    try:
        return requests.get(
            url,
            timeout=timeout,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            },
            allow_redirects=True,
        )
    except Exception:
        return None


def is_valid_feed(content: str) -> bool:
    """Check if content is a valid RSS/Atom feed."""
    content = content.strip()
    patterns = [
        r"^<\?xml.*<\?rss",
        r"^<\?xml.*<feed\s",
        r"^<rss\s",
        r"^<feed\s",
        r"^<rdf:RDF",
    ]
    return any(re.match(p, content, re.IGNORECASE) for p in patterns)


def discover_feed_for_url(link: str) -> tuple[str, str | None] | None:
    """Discover RSS feed for a given URL."""
    homepage = get_homepage_url(link)

    response = fetch_url(homepage)
    if not response or response.status_code != 200:
        return None

    content_type = response.headers.get("Content-Type", "")

    if "xml" in content_type:
        if is_valid_feed(response.text):
            return (homepage, homepage if "xml" in content_type else None)

    if "html" in content_type:
        soup = BeautifulSoup(response.text, "html.parser")

        for feed_link in soup.find_all("link", rel="alternate"):
            feed_type = feed_link.get("type", "")
            href = feed_link.get("href", "")

            if any(t in feed_type for t in FEED_MIME_TYPES):
                feed_url = urljoin(homepage, href)
                resp = fetch_url(feed_url, timeout=3)
                if resp and is_valid_feed(resp.text):
                    return (homepage, feed_url)

        for path in COMMON_FEED_PATHS[:6]:
            feed_url = urljoin(homepage, path)
            resp = fetch_url(feed_url, timeout=3)
            if resp and is_valid_feed(resp.text):
                return (homepage, feed_url)

    return None


def get_site_info(url: str) -> tuple[str, str]:
    """Try to get the site title and description from the homepage."""
    title = ""
    description = ""

    response = fetch_url(url, timeout=3)
    if response and response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.text.strip()

        og_title = soup.find("meta", property="og:title")
        if og_title:
            title = og_title.get("content", "").strip()

        og_desc = soup.find("meta", property="og:description")
        if og_desc:
            description = og_desc.get("content", "").strip()

        if not description:
            meta_desc = soup.find("meta", attrs={"name": "description"})
            if meta_desc:
                description = meta_desc.get("content", "").strip()

        if not description:
            meta_desc = soup.find("meta", attrs={"name": "Description"})
            if meta_desc:
                description = meta_desc.get("content", "").strip()

    return title, description


def main():
    existing_feeds = get_existing_feeds(CONFIG_FILE)
    thought_links = get_thought_links(POSTS_DIR)

    print(f"Found {len(thought_links)} thought links")
    print(f"Existing blogroll feeds: {len(existing_feeds)}")
    print()

    unique_homepages = {}
    for link in thought_links:
        homepage = get_homepage_url(link)
        if homepage not in unique_homepages:
            unique_homepages[homepage] = link

    print(f"Unique homepages: {len(unique_homepages)}")

    filtered = {
        hp: lp
        for hp, lp in unique_homepages.items()
        if hp.rstrip("/") not in existing_feeds
    }
    print(f"After filtering existing: {len(filtered)}")
    print()

    suggestions = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {
            executor.submit(discover_feed_for_url, link): link
            for link in filtered.values()
        }

        for future in as_completed(futures):
            result = future.result()
            if result:
                homepage, feed_url = result
                if feed_url and feed_url.lower() not in existing_feeds:
                    suggestions.append(
                        {
                            "feed_url": feed_url,
                            "homepage": homepage,
                        }
                    )
                    print(f"Found: {homepage} -> {feed_url}")

    print()
    print("=" * 60)
    print("SUGGESTED FEEDS TO ADD TO BLOGROLL:")
    print("=" * 60)

    for s in suggestions:
        title, description = get_site_info(s["homepage"])
        print(f"""
[[markata-go.blogroll.feeds]]
url = "{s["feed_url"]}"
title = "{title or "TITLE"}"
description = "{description or "DESCRIPTION"}"
category = "development"
tags = ["written"]
site_url = "{s["homepage"]}"
""")

    print(f"\nTotal suggestions: {len(suggestions)}")


if __name__ == "__main__":
    typer.run(main)
