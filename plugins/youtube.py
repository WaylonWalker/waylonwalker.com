from typing import TYPE_CHECKING
from functools import lru_cache
from string import Template

from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from bs4.element import Tag
    from bs4 import BeautifulSoup


# Cache the template to avoid repeated string creation
YOUTUBE_TEMPLATE = Template("""
    <iframe class='m-auto my-8' width="800" height="450" src="https://youtube.com/embed/$id" title="YouTube video
    player" frameborder="0" allow="accelerometer; autoplay;
    clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
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
        return render_youtube(youtube.attrs["href"])
    return str(youtube)

def swap_youtubes(soup: "BeautifulSoup") -> None:
    """Finds youtubes in an article's soup and swaps for embeds"""
    # More efficient selection of relevant links
    links = soup.find_all("a", href=lambda x: x and x.startswith("https://youtu.be"))

    for link in links:
        if link.string and link["href"] == link.string.strip():
            link.replace_with(swap_youtube(link))

@hook_impl
def post_render(markata):
    "Hook to replace YouTube links with embeds"
    if not markata.filter("skip==True"):
        return

    from bs4 import BeautifulSoup
    should_prettify = markata.config.get("prettify_html", False)

    with markata.cache as cache:
        for article in markata.filter("skip==False"):
            # Quick check for potential YouTube links before parsing
            if "youtu.be" not in article.content:
                continue

            key = markata.make_hash("youtube", article.html)

            if key in cache:
                article.html = cache[key]
                continue

            # Use lxml parser for better performance
            soup = BeautifulSoup(article.html, "lxml")
            swap_youtubes(soup)

            article.html = soup.prettify() if should_prettify else str(soup)
            cache[key] = article.html


if __name__ == "__main__":
    f = __file__
