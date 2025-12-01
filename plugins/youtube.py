from functools import lru_cache
from string import Template
from typing import TYPE_CHECKING

from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from bs4.element import Tag
    from bs4 import BeautifulSoup


# Cache the template to avoid repeated string creation
YOUTUBE_TEMPLATE = Template("""
<div class="relative w-full aspect-video">
    <iframe class='absolute top-0 left-0 w-full h-full' src="https://youtube.com/embed/$id" title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>
""")


@lru_cache(maxsize=100)
def render_youtube(link: str) -> str:
    "Render an iframe given a YouTube link - now using string templates for better performance"
    id = link.replace("https://youtu.be/", "")
    return YOUTUBE_TEMPLATE.substitute(id=id)


def is_valid_youtube(youtube: "Tag") -> bool:
    "checks if the link is a valid YouTube link"
    href = youtube.attrs["href"]
    return href.startswith("https://youtu.be")


def swap_youtube(youtube: "Tag") -> str:
    "Convert YouTube link to embed HTML"
    if is_valid_youtube(youtube):
        from bs4 import BeautifulSoup

        iframe_html = render_youtube(youtube.attrs["href"])
        # Parse the iframe HTML to create a proper BeautifulSoup element
        iframe_soup = BeautifulSoup(iframe_html, "lxml")
        return iframe_soup.div
    return str(youtube)


def swap_youtubes(soup: "BeautifulSoup") -> None:
    """Finds youtubes in an article's soup and swaps for embeds"""
    # More efficient selection of relevant links
    links = soup.find_all("a", href=lambda x: x and x.startswith("https://youtu.be"))

    for link in links:
        if link.string and link["href"] == link.string.strip():
            link.replace_with(swap_youtube(link))


def process_html_content(
    html_content: str, cache, cache_key: str, should_prettify: bool
) -> str:
    """Process a single HTML content by replacing YouTube links with embeds.

    Args:
        html_content: The HTML content to process
        cache: The markata cache object
        cache_key: The cache key for this content
        should_prettify: Whether to prettify the output HTML

    Returns:
        The processed HTML string
    """
    # Quick check for potential YouTube links before parsing
    if "youtu.be" not in html_content:
        return html_content

    if cache_key in cache:
        return cache[cache_key]

    # Use lxml parser for better performance
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_content, "lxml")
    swap_youtubes(soup)

    result = soup.prettify() if should_prettify else str(soup)
    cache[cache_key] = result
    return result


@hook_impl
def post_render(markata):
    "Hook to replace YouTube links with embeds"
    if not markata.filter("not skip"):
        return

    should_prettify = markata.config.get("prettify_html", False)

    with markata.cache as cache:
        for article in markata.filter("not skip"):
            if isinstance(article.html, dict):
                # Handle dictionary case
                processed_html = {}
                for key, html_content in article.html.items():
                    cache_key = markata.make_hash("youtube", html_content)
                    processed_html[key] = process_html_content(
                        html_content, cache, cache_key, should_prettify
                    )
                article.html = processed_html
            else:
                # Handle string case
                cache_key = markata.make_hash("youtube", article.html)
                article.html = process_html_content(
                    article.html, cache, cache_key, should_prettify
                )


if __name__ == "__main__":
    f = __file__
