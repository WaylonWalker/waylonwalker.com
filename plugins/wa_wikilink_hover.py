"""
wikilink hover using web awesome
"""

from typing import TYPE_CHECKING

from lxml import html
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    pass

external_svg = """
<svg xmlns="https://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-4 w-4 inline align-middle">
  <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25" />
</svg>
"""


def hover_links(doc):
    wikilinks = doc.xpath("//a[@class='wikilink']")
    hoverlinks = doc.xpath("//a[@class='hoverlink']")

    for link in wikilinks + hoverlinks:
        href = link.get("href", "").lstrip("/")

        title = link.text
        name = title.lower().replace(" ", "-")

        link.set("id", f'{name}-wikilink')

        img = f"""
<wa-tooltip 
  class='w-full' 
  for="{name}-wikilink" 
  id="{name}-wikilink-tooltip" 
  distance="12" 
  trigger='hover focus'
  style="--max-width:none;"
  class="!p-0"
  >
  <div class="bg-black rounded-xl border-2 border-pink-500">
    <p class='p-4 text-gray-400 text-xs'>
    wikilink
    </p>
    <wa-include 
    class='w-80 h-64 sm:w-96 sm:h-96 overflow-y-hidden' 
    src="/{href.strip('/')}/partial"
    ></wa-include>
    <p class='p-4 text-right text-gray-400 text-xs' >
    ... click to see full post
    </p>
  </div>
</wa-tooltip>
"""

        extra_doc = html.fromstring(img)
        body = doc.xpath("//body")[0]
        body.append(extra_doc)

    return doc


@hook_impl
def post_render(markata):
    "Hook to replace youtubes on images.waylonwalker.com with mp4's if they exist"

    with markata.cache as cache:
        for post in markata.filter("not skip"):
            if post.html is None:
                continue

            if isinstance(post.html, dict):
                for key, post_html in post.html.items():
                    post.html[key] = do_hover_links(
                        cache, markata, post_html, post.slug
                    )
            else:
                post.html = do_hover_links(cache, markata, post.html, post.slug)


def do_hover_links(cache, markata, post_html, post_slug):
    should_prettify = markata.config.get("prettify_html", False)
    key = markata.make_hash("wikilink_hover", post_html)
    html_from_cache = markata.precache.get(key)
    if "wikilink" in post_html or "hoverlink" in post_html:
        if html_from_cache is None:
            doc = html.fromstring(post_html)
            hover_links(doc)
            if should_prettify:
                html_str = html.tostring(doc, pretty_print=True, encoding="unicode")
            else:
                html_str = html.tostring(doc, encoding="unicode")
            cache.set(key, html_str)
        else:
            html_str = html_from_cache
        return html_str
    else:
        return post_html
