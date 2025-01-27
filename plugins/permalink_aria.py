from lxml import html
from markata.hookspec import hook_impl


def permalink_aria(doc):
    for a_tag in doc.xpath("//a[@class='header-anchor'][@href]"):
        a_tag.attrib["aria-label"] = (
            f"Permalink to Heading {a_tag.getparent().text_content()}"
        )
    return doc


@hook_impl
def post_render(markata):
    should_prettify = markata.config.get("prettify_html", False)
    with markata.cache as cache:
        for article in markata.filter("skip==False"):
            key = markata.make_hash("permalink_aria", article.html)

            html_from_cache = markata.precache.get(key)

            if html_from_cache is None:
                doc = html.fromstring(article.html)
                permalink_aria(doc)
                if should_prettify:
                    html_str = html.tostring(doc, pretty_print=True, encoding="unicode")
                else:
                    html_str = html.tostring(doc, encoding="unicode")
                cache.set(key, html_str)

            else:
                html_str = html_from_cache
            article.html = html_str
