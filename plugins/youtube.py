from pathlib import Path
from typing import TYPE_CHECKING

from bs4 import BeautifulSoup
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from bs4.element import Tag


def render_youtube(youtube: "Tag") -> "Tag":
    "Render an iframe given a validated anchor tag."

    link = youtube.attrs["href"]
    id = link.replace("https://youtu.be/", "")

    html = f"""
        <iframe width="800" height="450" src="https://youtube.com/embed/{id}" title="YouTube video
        player" frameborder="0" allow="accelerometer; autoplay;
        clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen></iframe>
    """
    return BeautifulSoup(html, "html.parser")


def is_valid_youtube(youtube: "Tag") -> bool:
    "checks the src of the image, must be from images.waylonwalker.com and a .youtube"
    href = youtube.attrs["href"]
    return href.startswith("https://youtu.be")


def swap_youtube(youtube: "Tag") -> "Tag":
    "Swap"

    if is_valid_youtube(youtube):
        return render_youtube(youtube)
    else:
        return youtube


def swap_youtubes(soup: BeautifulSoup) -> None:
    """Finds youtubes in an articles soup and swaps for mp4s"""
    links = [l for l in soup.find_all("a") if l.string != None]
    onelinelinks = [l for l in links if l["href"] == l.string.strip()]

    for link in onelinelinks:
        link.replace_with(swap_youtube(link))


@hook_impl
def post_render(markata):
    "Hook to replace youtubes on images.waylonwalker.com with mp4's if they exist"
    with markata.cache as cache:
        for article in markata.articles:
            key = markata.make_hash(
                __file__,
                Path(__file__).read_text(),
                "post_render",
                article.content,
                article.html,
            )

            html_from_cache = cache.get(key)

            if html_from_cache is None:
                soup = BeautifulSoup(article.html, "html.parser")
                swap_youtubes(soup)
                html = soup.prettify()
                cache.add(key, html)

            else:
                html = html_from_cache
            article.html = html


if __name__ == "__main__":
    f = __file__
