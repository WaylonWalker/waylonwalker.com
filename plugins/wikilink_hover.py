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
        parent = link.getparent()
        classes = parent.get("class", "").split()
        classes.extend(["hover:z-20", "relative"])
        parent.set("class", " ".join(classes))

        # if parent of parent is an admonition with class of .admonition
        parent_parent = parent.getparent()
        if parent_parent is not None and "admonition" in (
            parent_parent.get("class", "") or ""
        ):
            pp_classes = parent_parent.get("class", "").split()
            pp_classes.append("hover:z-20")
            parent_parent.set("class", " ".join(pp_classes))

        href = link.get("href", "").lstrip("/")

        prefix = ""
        boost = ""
        if href.endswith(".webp") or href.endswith(".mp4"):
            href = f"https://obsidian-assets.waylonwalker.com/{href}"
        elif not href.startswith("https://"):
            href = f"https://waylonwalker.com/{href}"
            boost = ' hx-boost="true"'
        if link in wikilinks:
            boost = ' hx-boost="true"'
        if link in hoverlinks:
            prefix = external_svg

        title = link.text

        if href.endswith(".webp"):
            img = f"""
            <a class="obsidian-asset obsidian-asset--image" href="{href}" title="{title}">
                <img src="{href}" style="max-height:800px;" alt="{title}">
            </a>
            """
        elif href.endswith(".mp4"):
            img = f"""
            <a class="obsidian-asset obsidian-asset--video" href="{href}" title="{title}">
            <video src="{href}" class="m-auto" controls></video>
            </a>
            """

        else:
            img = f"""
    <span class="z-10 group group-hover:z-20 relative inline-block">
        <a class="wikilink text-pink-500 hover:underline" href="{href}" title="{title}"{boost}>{prefix} {title}</a>
        <button class="ml-2 text-pink-500 hover:underline focus:outline-none" aria-label="Preview">
            <svg xmlns="https://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="h-5 w-5 inline align-middle">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
            </svg>
        </button>
        <a href="{href}"
            class="hidden absolute top-6 left-0 z-20 group-hover:block ">
            <img alt="a screenshot of {href}"
                class="rounded-xl transition-height ease-in duration-75 h-0 opacity-0 group-hover:opacity-100 group-hover:h-[800px] max-w-none "
                height="800" width="600"
                style=' box-shadow: rgba(0, 0, 0, 0.6) 0 0 500rem 500rem; '
                src="https://shots.wayl.one/shot/?url={href}&amp;height=1600&amp;width=1200&amp;scaled_width=600&amp;scaled_height=800&amp;selectors="
                >
        </a>
    </span>
"""

        extra_doc = html.fromstring(img)
        if href.endswith(".webp") or href.endswith(".mp4"):
            parent = link.getparent()
            parent.clear()
            parent.append(extra_doc)
        else:
            # Get the tail text (text that comes after the link)
            tail_text = link.tail
            # Replace the link with our new hover structure
            link.getparent().replace(link, extra_doc)
            # If there was text after the link, add it back
            if tail_text:
                extra_doc.tail = tail_text

    return doc


@hook_impl
def post_render(markata):
    "Hook to replace youtubes on images.waylonwalker.com with mp4's if they exist"

    should_prettify = markata.config.get("prettify_html", False)
    with markata.cache as cache:
        for article in markata.filter("not skip"):
            key = markata.make_hash("wikilink_hover", article.html)
            html_from_cache = markata.precache.get(key)

            if "wikilink" in article.html or "hoverlink" in article.html:
                if html_from_cache is None:
                    doc = html.fromstring(article.html)
                    hover_links(doc)
                    if should_prettify:
                        html_str = html.tostring(
                            doc, pretty_print=True, encoding="unicode"
                        )
                    else:
                        html_str = html.tostring(doc, encoding="unicode")
                    cache.set(key, html_str)
                else:
                    html_str = html_from_cache
                article.html = html_str
