"""
Improved Markata plugin for wikilink hover previews using HTMX + Tippy.js
Fixes HTMX swap errors by deferring hx-get trigger until tooltip is visible
and ensures proper initialization order.
"""

from typing import TYPE_CHECKING
from lxml import html
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    pass


def hover_links(doc):
    wikilinks = doc.xpath("//a[@class='wikilink']")
    hoverlinks = []

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

        # Create hidden template for tooltip content
        tooltip_html = f"""
<div id="{name}-tooltip-content-template" class="hidden">
  <p class="p-4 text-gray-400 text-xs">
    <a href="/{href.strip('/')}">{title}</a> wikilink
  </p>
  <div class="rounded-xl overflow-y-scroll w-80 sm:w-96 h-64 sm:h-96 text-lg">
    <div 
      hx-get="/{href.strip('/')}/partial/"
      hx-trigger="tippy:shown once"
      hx-target="this"
      hx-swap="outerHTML"
      class="flex items-center justify-center text-gray-400 text-xs p-4">
      loading...
    </div>
    <p class="p-2 text-right text-gray-400 text-xs italic">...click to see full post</p>
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

            # Inject tippy.js initialization script (fixed order)
            script_tag = html.fromstring(
                """
<script>
document.addEventListener('DOMContentLoaded', function () {
  tippy('[data-tippy-content]', {
    theme: 'waylon',
    placement: 'bottom-start',
    arrow: false,
    allowHTML: true,
    interactive: true,
    maxWidth: 'none',
    onShown(instance) {
      const id = instance.reference.id.replace('-wikilink', '-tooltip-content-template');
      const tpl = document.getElementById(id);
      if (!tpl) return;

      // 1) Inject template HTML into tooltip
      instance.setContent(tpl.innerHTML);

      // 2) Re-process for HTMX bindings
      htmx.process(instance.popper);

      // 3) Dispatch event for hx-trigger="tippy:shown"
      const hxNode = instance.popper.querySelector('[hx-get]');
      if (hxNode) {
        hxNode.dispatchEvent(new Event('tippy:shown', { bubbles: true }));
      }

      console.log('Tippy shown + HTMX processed');
    },
  });
});
</script>
"""
            )

            style_tag = html.fromstring(
                """
<style>
.tippy-box[data-theme~='waylon'] {
  background-color: #0b0b0b;
  color: #e5e7eb;
  border: 2px solid #ec4899;
  border-radius: 12px;
}
</style>
"""
            )

            doc.xpath("//body")[0].append(script_tag)
            doc.xpath("//head")[0].append(style_tag)

            html_str = html.tostring(doc, pretty_print=should_prettify, encoding="unicode")
            cache.set(key, html_str)
        else:
            html_str = html_from_cache
        return html_str
    else:
        return post_html
