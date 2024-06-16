from typing import TYPE_CHECKING
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from markata.hookspec import hook_impl


def permalink_aria(soup):
    for a_tag in soup.find_all("a", href=True, class_="header-anchor"):
        a_tag["aria-label"] = f"Permalink to Heading {a_tag.parent.text}"
    return soup


@hook_impl
def post_render(markata):
    should_prettify = markata.config.get("prettify_html", False)
    with markata.cache as cache:
        for article in markata.articles:
            key = markata.make_hash("permalink_aria", article.html)

            html_from_cache = markata.precache.get(key)

            if html_from_cache is None:
                soup = BeautifulSoup(article.html, "lxml")
                permalink_aria(soup)
                if should_prettify:
                    html = soup.prettify()
                else:
                    html = str(soup)
                cache.add(key, html)

            else:
                html = html_from_cache
            article.html = html
