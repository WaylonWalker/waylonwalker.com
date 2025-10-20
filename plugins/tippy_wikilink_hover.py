"""
wikilink hover using htmx + tippy.js
"""

from typing import TYPE_CHECKING
from lxml import html
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    pass


def hover_links(doc):
    wikilinks = doc.xpath("//a[@class='wikilink']")
    hoverlinks = doc.xpath("//a[@class='hoverlink']")

    for link in wikilinks + hoverlinks:
        href = link.get("href", "").lstrip("/")
        title = link.text or href
        name = title.lower().replace(" ", "-")

        # Add tippy attributes for hover preview
        link.set("id", f"{name}-wikilink")
        link.set("data-tippy-content", f"<div id='{name}-tooltip-content'></div>")
        link.set("data-tippy-allowhtml", "true")
        link.set("data-tippy-interactive", "true")
        link.set("data-tippy-placement", "bottom-start")

        # Create a hidden template for the tooltip content.
        # htmx will load the partial HTML into this div.
        tooltip_html = f"""
<div id="{name}-tooltip-content-template" class="hidden">
  <p class="p-4 text-gray-400 text-xs">
  <a href="/{href.strip('/')}">
      {title}
  </a>
    wikilink
  </p>
  <div class="rounded-xl overflow-y-scroll w-80 sm:w-96 h-64 sm:h-96 text-lg">
    <div 
      hx-get="/{href.strip('/')}/partial/" 
      hx-trigger="load"
      hx-target="this"
      hx-swap="outerHTML"
      class="flex items-center justify-center text-gray-400 text-xs p-4">
      loading...
    </div>
    <p class="p-2 text-right text-gray-400 text-xs italic">
      ...click to see full post
    </p>
  </div>
</div>
"""

        body = doc.xpath("//body")[0]
        body.append(html.fromstring(tooltip_html))

    return doc


@hook_impl
def post_render(markata):
    """Hook to inject tippy-based hover previews for wikilinks and hoverlinks."""
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
    key = markata.make_hash("wikilink_hover_htmx_tippy", post_html)
    html_from_cache = markata.precache.get(key)

    if "wikilink" in post_html or "hoverlink" in post_html:
        if html_from_cache is None:
            doc = html.fromstring(post_html)
            hover_links(doc)

            # Inject tippy.js init script once per page
            script_tag = html.fromstring("""
<script>
document.addEventListener('DOMContentLoaded', function () {
  // Initialize all tippy tooltips
  tippy('[data-tippy-content]', {
      theme: ' waylon',
    placement: 'bottom-start',
    arrow: false,
    allowHTML: true,
    interactive: true,
    maxWidth: 'none',
    onShow(instance) {
      const id = instance.reference.id.replace('-wikilink', '-tooltip-content-template');
      const content = document.getElementById(id);
      if (content) {
        instance.setContent(content.innerHTML);
      }
    },
  });
});
</script>
""")
            style_tag = html.fromstring("""
<style>

.tippy-box[data-theme~='waylon'] {
  background-color: #0b0b0b;          /* background */
  color: #e5e7eb;                      /* text color (optional) */
  border: 2px solid #ec4899;           /* border & color */
  border-radius: 12px;                 /* border radius */
}
</style>
""")
            doc.xpath("//body")[0].append(script_tag)
            doc.xpath("//head")[0].append(style_tag)

            html_str = html.tostring(
                doc, pretty_print=should_prettify, encoding="unicode"
            )
            cache.set(key, html_str)
        else:
            html_str = html_from_cache
        return html_str
    else:
        return post_html
