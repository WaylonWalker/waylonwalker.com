"""manifest plugin"""
import json
from pathlib import Path
from typing import TYPE_CHECKING, List

from bs4 import BeautifulSoup
from markata import Markata, __version__
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    import frontmatter
    from bs4.element import Tag

from http.client import InvalidURL
from urllib import request as ulreq
from urllib.error import HTTPError

from PIL import ImageFile


def getsizes(uri, default_height=500, default_width=500):
    # get file size *and* image size (None if not known)
    # https://stackoverflow.com/questions/7460218/get-image-size-without-downloading-it-in-python

    try:
        with ulreq.urlopen(uri) as file:
            p = ImageFile.Parser()
            while True:
                data = file.read(1024)
                if not data:
                    break
                p.feed(data)
                if p.image:
                    return p.image.size
    except BaseException:
        return (
            default_width,
            default_height,
        )


def _create_seo(
    markata: Markata, soup: BeautifulSoup, article: "frontmatter.Post"
) -> List:
    if article.metadata["description"] == "" or None:
        article.metadata["description"] = " ".join(
            [p.text for p in soup.find(id="post-body").find_all("p")]
        ).strip()[:120]

    seo = [
        *markata.seo,
        {
            "name": "og:author",
            "property": "og:author",
            "content": markata.config["author_name"],
        },
        {
            "name": "og:author_email",
            "property": "og:author_email",
            "content": markata.config["author_email"],
        },
        {
            "name": "og:type",
            "property": "og:type",
            "content": "website",
        },
        {
            "name": "description",
            "property": "description",
            "content": article.metadata["description"],
        },
        {
            "name": "og:description",
            "property": "og:description",
            "content": article.metadata["description"],
        },
        {
            "name": "twitter:description",
            "property": "twitter:description",
            "content": article.metadata["description"],
        },
        {
            "name": "og:title",
            "property": "og:title",
            "content": f'{article.metadata["title"]} | {markata.config["site_name"]}'[
                :60
            ],
        },
        {
            "name": "twitter:title",
            "property": "twitter:title",
            "content": f'{article.metadata["title"]} | {markata.config["site_name"]}'[
                :60
            ],
        },
        {
            "name": "og:image",
            "property": "og:image",
            "content": f'{markata.config["images_url"]}/{article.metadata["slug"]}-og.png',
        },
        {
            "name": "twitter:image",
            "property": "twitter:image",
            "content": f'{markata.config["images_url"]}/{article.metadata["slug"]}-og.png',
        },
        {
            "name": "og:image:width",
            "property": "og:image:width",
            "content": "1600",
        },
        {
            "name": "og:image:width",
            "property": "og:image:width",
            "content": "900",
        },
        {
            "name": "twitter:card",
            "property": "twitter:card",
            "content": markata.config["twitter_card"],
        },
        {
            "name": "og:site_name",
            "property": "og:site_name",
            "content": markata.config["site_name"],
        },
        {
            "name": "twitter:creator",
            "property": "twitter:creator",
            "content": markata.config["twitter_creator"],
        },
        {
            "name": "title",
            "property": "title",
            "content": article.metadata["title"],
        },
        {
            "name": "generator",
            "property": "generator",
            "content": f"markata {__version__}",
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


def _clean_amp(soup: BeautifulSoup) -> None:
    """modifies soup as a side effect"""
    for script in soup.find_all("script"):
        script.decompose()
    script = soup.new_tag(
        "script", attrs={"src": "https://cdn.ampproject.org/v0.js", "async": True}
    )
    soup.head.append(script)

    for button in soup.find_all("button"):
        button.decompose()

    body = soup.find("body")

    for style in body.find_all("style"):
        style.decompose()

    for button in soup.find_all("button"):
        button.decompose()

    for img in soup.find_all("img"):
        img_size = getsizes(img.attrs["src"])
        try:
            amp_img = soup.new_tag(
                "amp-img",
                attrs={
                    # causes amp failure if not a valid amp attribute
                    # **img.attrs,
                    "src": img.attrs["src"],
                    "layout": "responsive",
                    "width": img_size[0],
                    "height": img_size[1],
                },
            )
        except TypeError:
            # img_size is sometimes returning None
            amp_img = soup.new_tag(
                "amp-img",
                attrs={
                    # causes amp failure if not a valid amp attribute
                    # **img.attrs,
                    "src": img.attrs["src"],
                    "layout": "responsive",
                    "width": 500,
                    "height": 500,
                },
            )
        img.parent.insert(img.parent.contents.index(img), amp_img)
        img.decompose()


@hook_impl
def render(markata: Markata) -> None:
    with markata.cache as cache:
        for article in markata.iter_articles("add amp seo tags from seo.py"):
            key = markata.make_hash(
                "amp_seo",
                "render",
                article["content_hash"],
                markata.site_name,
                markata.url,
                article.metadata["slug"],
                markata.twitter_card,
                article.metadata["title"],
                markata.site_name,
                str(markata.seo),
            )
            html_from_cache = cache.get(key)

            if html_from_cache is None:
                soup = BeautifulSoup(article.amp_html, features="lxml")
                seo = _create_seo(markata, soup, article)
                _add_seo_tags(seo, article, soup)
                _clean_amp(soup)
                canonical_link = soup.new_tag("link")
                canonical_link.attrs["rel"] = "canonical"
                canonical_link.attrs[
                    "href"
                ] = f'{markata.url}/{article.metadata["slug"]}/'
                soup.head.append(canonical_link)

                meta_url = soup.new_tag("meta")
                meta_url.attrs["name"] = "og:url"
                meta_url.attrs["property"] = "og:url"
                meta_url.attrs["content"] = f'{markata.url}/{article.metadata["slug"]}/'
                soup.head.append(meta_url)

                # html = soup.prettify()
                html = str(soup)
                cache.add(key, html, expire=15 * 24 * 60)
            else:
                html = html_from_cache
            article.amp_html = html
