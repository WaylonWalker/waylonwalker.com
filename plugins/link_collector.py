"""
Link Collector Plugin

Collects all hyperlinks from posts and stores them in markata.links.

# Installation

Add to your `markata.toml`:

```toml
[markata]
hooks = ["markata.plugins.link_collector"]
```

# Usage

This plugin gathers link information in the `post_render` phase and makes it
available as a list of dictionaries in `markata.links`.

Each item has:
- `source_url`: absolute URL of the post
- `target_url`: value from the `href` attribute
- `target_domain`: domain extracted from target_url (if present)
- `is_internal`: boolean flag indicating whether the link is internal to the site

# Configuration

No custom config necessary.

# Notes

Supports relative and absolute links. Invalid URLs may have `target_domain` as `None`.
"""

from more_itertools import unique_everseen
from operator import attrgetter
import pydantic
from markata.hookspec import hook_impl, register_attr
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from typing import Optional

MARKATA_PLUGIN_NAME = "Link Collector"
MARKATA_PLUGIN_PACKAGE_NAME = "link_collector"


class LinkedPost(pydantic.BaseModel):
    hrefs: Optional[list] = None
    inlinks: Optional[list] = None
    outlinks: Optional[list] = None


@hook_impl()
@register_attr("post_models")
def post_model(markata: "Markata") -> None:
    markata.post_models.append(LinkedPost)


@hook_impl
@register_attr("links")
def render(markata: "Markata") -> None:
    """
    Collect all links from posts and add to markata.links.
    """

    class Link(pydantic.BaseModel):
        source_url: Optional[str] = None
        source_post: Optional[markata.Post] = None
        target_post: Optional[markata.Post] = None
        raw_target: Optional[str] = None
        target_url: Optional[str] = None
        target_domain: Optional[str] = None
        is_internal: Optional[bool] = None
        is_self: Optional[bool] = None

    links = []
    site_domain = urlparse(str(markata.config.url)).netloc

    try:
        posts = markata.filter("not skip")
    except NameError:
        posts = markata.filter("")

    with markata.cache as cache:
        # for post in posts:
        for post in markata.filter("True"):
            key = markata.make_hash(
                __file__,
                # Path(__file__).read_text(),
                "post_render",
                post.slug,
                post.title,
                post.content,
            )
            hrefs_from_cache = cache.get(key)
            if hrefs_from_cache is not None:
                post.hrefs = hrefs_from_cache
                continue

            slug = getattr(post, "slug", "")
            base_url = urljoin(str(markata.config.url), slug)

            if post.article_html is None:
                soup = BeautifulSoup(post.output_html.read_text(), "html.parser")
                soup = soup.find(id="post-body")
            else:
                soup = BeautifulSoup(post.article_html, "html.parser")

            post.hrefs = [a["href"] for a in soup.find_all("a", href=True)]

            cache.set(key, post.hrefs, expire=markata.config["default_cache_expire"])

            "b1483d6f04c3eb1a"

    for post in markata.filter("True"):
        for href in post.hrefs:
            slug = getattr(post, "slug", "")
            base_url = urljoin(str(markata.config.url), slug)
            target_url = urljoin(base_url, href)
            domain = urlparse(target_url).netloc or None
            is_internal = domain == site_domain

            target_post = None
            is_self = False
            if is_internal:
                target_slug = urlparse(target_url).path.strip("/")

                safe_target_slug = repr(target_slug)
                possible_target_post = markata.map(
                    "post", filter=f"slug=={safe_target_slug}"
                )
                if len(possible_target_post) == 1:
                    target_post = possible_target_post[0]
                elif len(possible_target_post) > 1:
                    import warnings

                    warnings.warn(
                        f"Multiple posts with slug {target_slug} found. Using first one."
                    )
                    target_post = possible_target_post[0]
                else:
                    target_post = None
                if target_post is not None:
                    is_self = post.slug == target_post.slug
                else:
                    target_post = None

            links.append(
                Link(
                    source_url=base_url,
                    source_post=post,
                    target_post=target_post,
                    raw_target=href,
                    target_url=target_url,
                    target_domain=domain,
                    is_internal=is_internal,
                    is_self=is_self,
                )
            )

    markata.links = links

    # try:
    #     posts = markata.filter("not skip")
    # except NameError:
    #     posts = markata.filter("True")
    posts = markata.filter("True")

    for post in posts:
        post.inlinks = [
            link
            for link in links
            if link.target_post
            and link.target_post.slug == post.slug
            and not link.is_self
        ]
        post.inlinks = list(unique_everseen(post.inlinks, key=attrgetter("source_url")))
        post.outlinks = [
            link
            for link in links
            if link.source_post
            and link.source_post.slug == post.slug
            and not link.is_self
        ]
        post.outlinks = list(
            unique_everseen(post.outlinks, key=attrgetter("target_url"))
        )


from collections import Counter
from typing import List, Dict


def count_links(links: List[Dict[str, str]]) -> Counter:
    """
    Count the number of times each target_url appears in the links list.

    Parameters:
    - links: List of link dictionaries, as stored in markata.links

    Returns:
    - Counter of target_url occurrences
    """
    return Counter(link["target_url"] for link in links if "target_url" in link)


def count_domains(links: List[Dict[str, str]]) -> Counter:
    """
    Count the number of times each target_domain appears in the links list.

    Parameters:
    - links: List of link dictionaries

    Returns:
    - Counter of target_domain occurrences
    """
    return Counter(link["target_domain"] for link in links if "target_domain" in link)
