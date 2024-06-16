from pathlib import Path
from typing import TYPE_CHECKING

from bs4 import BeautifulSoup
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from bs4.element import Tag


def boosted_links(soup):
    from urllib.parse import urljoin, urlparse

    from bs4 import BeautifulSoup

    base_url = "https://waylonwalker.com"

    # Parse the HTML content
    # soup = BeautifulSoup(html_content, 'html.parser')
    site_domain = urlparse(base_url).netloc

    # Find all <a> tags
    for a_tag in soup.find_all("a", href=True):
        # Resolve relative links to absolute URLs
        absolute_url = urljoin(base_url, a_tag["href"])
        parsed_url = urlparse(absolute_url)

        # Check if the link points to the site's domain
        if parsed_url.netloc == site_domain and not a_tag.has_attr("hx-boost"):
            a_tag["hx-boost"] = "true"
    # for a_tag in soup.find_all("a"):
    #     if not a_tag.has_attr("hx-boost"):
    #         a_tag["hx-boost"] = "true"
    return soup


@hook_impl
def post_render(markata):
    "Hook to replace youtubes on images.waylonwalker.com with mp4's if they exist"
    should_prettify = markata.config.get("prettify_html", False)
    with markata.cache as cache:
        for article in markata.articles:
            key = markata.make_hash("boosted_link", article.html)

            html_from_cache = markata.precache.get(key)

            if html_from_cache is None:
                soup = BeautifulSoup(article.html, "lxml")
                boosted_links(soup)
                if should_prettify:
                    html = soup.prettify()
                else:
                    html = str(soup)
                cache.add(key, html)

            else:
                html = html_from_cache
            article.html = html
