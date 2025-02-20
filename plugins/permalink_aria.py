from lxml import html
from markata.hookspec import hook_impl


def permalink_aria(doc):
    for a_tag in doc.xpath("//a[@class='header-anchor'][@href]"):
        a_tag.attrib["aria-label"] = (
            f"Permalink to Heading {a_tag.getparent().text_content()}"
        )
    return doc


def process_html_content(html_content, cache, cache_key, should_prettify):
    """Process a single HTML content with permalink_aria transformation.

    Args:
        html_content: The HTML content to process
        cache: The markata cache object
        cache_key: The cache key for this content
        should_prettify: Whether to prettify the output HTML

    Returns:
        The processed HTML string
    """
    html_from_cache = cache.get(cache_key)
    if html_from_cache is None:
        doc = html.document_fromstring(html_content)
        permalink_aria(doc)
        if should_prettify:
            html_str = html.tostring(doc, pretty_print=True, encoding="unicode", doctype='<!DOCTYPE html>')
        else:
            html_str = html.tostring(doc, encoding="unicode", doctype='<!DOCTYPE html>')
        cache.set(cache_key, html_str)
        return html_str
    return html_from_cache


@hook_impl
def post_render(markata):
    should_prettify = markata.config.get("prettify_html", False)
    with markata.cache as cache:
        for article in markata.filter("not skip"):
            if isinstance(article.html, dict):
                # Handle dictionary case
                processed_html = {}
                for key, html_content in article.html.items():
                    cache_key = markata.make_hash("permalink_aria", html_content)
                    processed_html[key] = process_html_content(
                        html_content,
                        markata.precache,
                        cache_key,
                        should_prettify
                    )
                article.html = processed_html
            else:
                # Handle string case
                cache_key = markata.make_hash("permalink_aria", article.html)
                article.html = process_html_content(
                    article.html,
                    markata.precache,
                    cache_key,
                    should_prettify
                )
