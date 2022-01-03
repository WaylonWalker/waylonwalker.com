import re
from pathlib import Path
from typing import TYPE_CHECKING

import requests
from bs4 import BeautifulSoup
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from bs4.element import Tag


def url_exists(url: str) -> bool:
    "Checks that a given url has 200 response code"
    r = requests.head(url)
    return r.status_code == 200


def render_mp4(gif: "Tag") -> "Tag":
    "Render a video tag given a validatated image tag."

    webm_src = re.sub(".gif$", ".webm", gif.attrs["src"])
    mp4_src = re.sub(".gif$", ".mp4", gif.attrs["src"])

    if not url_exists(webm_src):
        return gif

    if not url_exists(mp4_src):
        return gif

    html = f"""
        <video controls muted autoplay playsinline loop=true width="100%">
            <source src="{webm_src}"
                    type="video/webm">
            <source src="{mp4_src}"
                    type="video/mp4">
            Sorry, your browser doesn't support embedded videos.
        </video>

        <div class='speed-control'>
            <button onclick="change_speed(.25)" >
                speed up
            </button>
            <button onclick="change_speed(-.25)" >
                slow down
            </button>
        </div>
    """
    return BeautifulSoup(html, "html.parser")


def is_valid_gif(gif: "Tag") -> bool:
    "checks the src of the image, must be from images.waylonwalker.com and a .gif"
    src = gif.attrs["src"]
    return src.startswith("https://images.waylonwalker.com") and src.endswith(".gif")


def swap_gif(gif: "Tag") -> "Tag":
    "Swap"
    if is_valid_gif(gif):
        return render_mp4(gif)
    else:
        return gif


def swap_gifs(soup: BeautifulSoup) -> None:
    """Finds gifs in an articles soup and swaps for mp4s"""
    gifs = soup.find_all("img")
    for gif in gifs:
        gif.replace_with(swap_gif(gif))


@hook_impl
def post_render(markata):
    "Hook to replace gifs on images.waylonwalker.com with mp4's if they exist"
    with markata.cache as cache:
        for article in markata.articles:
            key = markata.make_hash(
                __file__,
                Path(__file__).read_text(),
                "post_render",
                article.html,
            )
            html_from_cache = cache.get(key)
            if html_from_cache is None:
                soup = BeautifulSoup(article.html, "html.parser")
                swap_gifs(soup)
                html = soup.prettify()
                cache.add(key, html, expire=15 * 24 * 60 * 60)

            else:
                html = html_from_cache
            article.html = html
