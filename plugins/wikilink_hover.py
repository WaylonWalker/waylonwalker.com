from pathlib import Path
from typing import TYPE_CHECKING

from bs4 import BeautifulSoup
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from bs4.element import Tag


def hover_links(soup):
    wikilinks = soup.find_all("a", {"class": "wikilink"})
    for link in wikilinks:
        parent = link.parent
        parent["class"] = parent.get("class", []) + [
            "hover:z-20",
        ]
        href = link.attrs.get("href")
        if not href.startswith("https://"):
            href = f"https://waylonwalker.com/{href}"
        title = link.text
        img = f"""
    <span class="z-10 group group-hover:z-20 relative inline-block">
        <a class="wikilink text-pink-500 hover:underline" href="{href}" title="{title}">{title}</a>
        <button class="ml-2 text-pink-500 hover:underline focus:outline-none" aria-label="Preview">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="h-5 w-5 inline align-middle">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
            </svg>
        </button>
        <a href="{href}"
            class="hidden absolute top-6 left-0 z-20 group-hover:block ">
            <img alt="shot"
                class="rounded-xl transition-height ease-in duration-75 h-0 opacity-0 group-hover:opacity-100 group-hover:h-[500px] max-w-none "
                height="500" style=' box-shadow: rgba(0, 0, 0, 0.6) 0 0 50rem 50rem; '
                src="http://shots.wayl.one/shot/?url={href}&amp;height=1200&amp;width=1000&amp;scaled_width=1000&amp;scaled_height=800&amp;selectors="
                width="auto">
        </a>
    </span>
"""

        extra_soup = BeautifulSoup(img, "html.parser")
        link.replace_with(extra_soup)

    return soup


@hook_impl
def post_render(markata):
    "Hook to replace youtubes on images.waylonwalker.com with mp4's if they exist"
    should_prettify = markata.config.get("prettify_html", False)
    with markata.cache as cache:
        for article in markata.articles:
            key = markata.make_hash(article.html)

            html_from_cache = cache.get(key)
            html_from_cache = None

            if "wikilink" in article.html:
                if html_from_cache is None:
                    soup = BeautifulSoup(article.html, "lxml")
                    hover_links(soup)
                    if should_prettify:
                        html = soup.prettify()
                    else:
                        html = str(soup)
                    cache.add(key, html)

                else:
                    html = html_from_cache
                article.html = html
