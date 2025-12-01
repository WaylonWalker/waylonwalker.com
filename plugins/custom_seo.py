"""Custom HEADER tags for waylonwalker.com"""

from typing import List, TYPE_CHECKING

from bs4 import BeautifulSoup
from markata import Markata
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    import frontmatter
    from bs4.element import Tag


def _create_seo(
    markata: Markata, soup: BeautifulSoup, article: "frontmatter.Post"
) -> List:
    if article.metadata["description"] == "" or None:
        article.metadata["description"] = " ".join(
            [p.text for p in soup.find(id="post-body").find_all("p")]
        ).strip()[:120]

    seo = [
        {
            "name": "og:sm_image",
            "property": "og:sm_image",
            "content": f'{markata.config["images_url"]}/{article.metadata["slug"]}-og_250x140.png',
        },
    ]
    return seo


def _add_seo_tags(seo: List, article: "frontmatter.Post", soup: BeautifulSoup) -> None:
    for meta in seo:
        soup.head.append(_create_seo_tag(meta, soup))


def _create_seo_tag(meta: dict, soup: BeautifulSoup) -> "Tag":
    tag = soup.new_tag("meta")
    for k in meta:
        tag.attrs[k] = meta[k]
    return tag


@hook_impl
def post_render(markata: Markata) -> None:
    config = markata.get_plugin_config(__file__)
    should_prettify = markata.config.get("prettify_html", False)
    with markata.cache as cache:
        for article in markata.iter_articles("add seo tags from seo.py"):
            key = markata.make_hash(
                __name__,
                "post_render",
                article.metadata["slug"],
                markata.config["images_url"],
                article.content,
                article.html,
            )
            html_from_cache = cache.get(key)

            if html_from_cache is None:
                soup = BeautifulSoup(article.html, features="lxml")
                seo = _create_seo(markata, soup, article)
                _add_seo_tags(seo, article, soup)
                if should_prettify:
                    html = soup.prettify()
                else:
                    html = str(soup)
                cache.set(key, html, expire=config["cache_expire"])
            else:
                html = html_from_cache
            article.html = html
