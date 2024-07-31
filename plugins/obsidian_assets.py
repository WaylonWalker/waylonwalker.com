from pathlib import Path
from typing import TYPE_CHECKING

from markata.hookspec import hook_impl



def replace_obsidian_asset(content: str):

    return BeautifulSoup(html, "html.parser")


def swap_youtubes(soup: BeautifulSoup) -> None:
    """Finds youtubes in an articles soup and swaps for mp4s"""
    links = [l for l in soup.find_all("a") if l.string != None]
    onelinelinks = [l for l in links if l["href"] == l.string.strip()]

    for link in onelinelinks:
        link.replace_with(swap_youtube(link))


@hook_impl
def pre_render(markata):
    "Hook to replace youtubes on images.waylonwalker.com with mp4's if they exist"
    should_prettify = markata.config.get("prettify_html", False)
    with markata.cache as cache:
        for article in markata.articles:
            key = markata.make_hash("obsidian_assets", article.content)

            content_from_cache = markata.precache.get(key)

            if content_from_cache is None:
                swap_youtubes(soup)
                if should_prettify:
                    html = soup.prettify()
                else:
                    html = str(soup)
                cache.add(key, html)

            else:
                html = html_from_cache
            article.html = html


if __name__ == "__main__":
    f = __file__
