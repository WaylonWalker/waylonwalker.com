from urllib.parse import urljoin, urlparse

from markata.hookspec import hook_impl


def boosted_links(soup):
    base_url = "https://waylonwalker.com"

    site_domain = urlparse(base_url).netloc

    for a_tag in soup.find_all("a", href=True):
        absolute_url = urljoin(base_url, a_tag["href"])
        parsed_url = urlparse(absolute_url)

        if parsed_url.netloc == site_domain and not a_tag.has_attr("hx-boost"):
            a_tag["hx-boost"] = "true"
    return soup


@hook_impl
def post_render(markata):
    if not markata.filter("not skip"):
        return
    from bs4 import BeautifulSoup

    should_prettify = markata.config.get("prettify_html", False)
    with markata.cache as cache:
        for article in markata.filter("not skip"):
            key = markata.make_hash("boosted_link", article.html)

            html_from_cache = markata.precache.get(key)

            if html_from_cache is None:
                soup = BeautifulSoup(article.html, "lxml")
                boosted_links(soup)
                if should_prettify:
                    html = soup.prettify()
                else:
                    html = str(soup)
                cache.set(key, html)

            else:
                html = html_from_cache
            article.html = html
