"""
Dropper Media Wrapper Plugin

Wraps images and videos served from Dropper in links to their original source
and optionally adds a `?width=` query parameter when none is present.

# Installation

```toml
hooks = [
  "markata.plugins.load",
  "plugins.dropper",  # or the path where you place this file
]
```

# Configuration

```toml
[dropper_media_wrapper]
base_url = "https://dropper.wayl.one"  # Only media with src starting with this is touched
default_width = 500                     # When no query string exists, add ?width=500
enabled = true                          # Turn the plugin on/off
```

# Behaviour

- Finds all `<img>` tags whose `src` begins with `base_url`.
- Finds all `<video>` tags that either:
  - have a `src` beginning with `base_url`, **or**
  - contain a `<source>` child whose `src` begins with `base_url`.
- Uses the actual URL-bearing element (`<img>` or `<source>`/`<video>`) to
  apply the `?width=` query parameter.
- Wraps each `<img>` / `<video>` in an `<a>` that links to the **original**
  (unsized) URL.
- If the media URL has **no** `?` query string and `default_width` is truthy,
  it updates that URL to `src + "?width={default_width}"`.
- If the media tag is already inside an `<a>`, it reuses that anchor rather
  than nesting another one.
- Adds some `data-dropper-*` attributes for debugging/inspection.

Example result (simplified):

```html
<a href="https://dropper.wayl.one/api/file/…" data-dropper-anchor="created">
  <video
    data-dropper="processed"
    data-dropper-width="added"
    data-dropper-wrap="new-wrapper"
  >
    <source src="https://dropper.wayl.one/api/file/…?width=500" type="video/mp4" />
  </video>
</a>
```

# Notes

- This runs in `post_render`, so it works on fully rendered HTML.
- `post.html` can be either a string or a dict of variants; both are handled.
"""

from __future__ import annotations

from typing import Any, Dict, Union

import pydantic
from markata.hookspec import hook_impl, register_attr
from lxml import html as lxml_html
from lxml.etree import _Element as LxmlElement  # type: ignore[attr-defined]

MARKATA_PLUGIN_NAME = "Dropper Media Wrapper"
MARKATA_PLUGIN_PACKAGE_NAME = "dropper-media-wrapper"


class DropperMediaWrapperConfig(pydantic.BaseModel):
    """Configuration for the dropper media wrapper plugin."""

    base_url: str = "https://dropper.wayl.one"
    default_width: Union[int, str] = 500
    enabled: bool = True

    model_config = pydantic.ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True,
        extra="allow",
        str_strip_whitespace=True,
        validate_default=True,
        coerce_numbers_to_str=False,
        populate_by_name=True,
    )


class Config(pydantic.BaseModel):
    dropper_media_wrapper: DropperMediaWrapperConfig = DropperMediaWrapperConfig()


@hook_impl
@register_attr("config_models")
def config_model(markata: "Markata") -> None:  # type: ignore[name-defined]
    """Register the plugin's config model with Markata."""
    markata.config_models.append(Config)


def _find_video_media_tag_lxml(
    video: LxmlElement,
    base_url: str,
) -> tuple[str | None, LxmlElement | None]:
    """
    For an <video> element, find the effective media URL and the element
    whose src should be updated.

    Preference:
    1. First <source> child with src starting with base_url
    2. <video src="..."> if present and starting with base_url
    """
    base_url = base_url.rstrip("/")

    # 1) Prefer direct <source> children (no deep recursion)
    for source in video.xpath("./source[@src]"):
        src = source.get("src")
        if src and src.startswith(base_url):
            return src, source

    # 2) Fallback to <video src="...">
    src = video.get("src")
    if src and src.startswith(base_url):
        return src, video

    return None, None


def _wrap_dropper_media_in_links_lxml(
    html: str,
    *,
    base_url: str,
    default_width: int,
) -> str:
    """
    Faster implementation using lxml instead of BeautifulSoup.

    - Only parses if base_url is present at all.
    - Finds <img> with src starting with base_url.
    - Finds <video> that either:
      * has src starting with base_url, or
      * has a <source> child whose src starts with base_url.
    - Wraps media in <a> to original URL, adds ?width=default_width if needed.
    """

    if not html:
        return html

    # Fast skip: if no Dropper URLs, don't parse at all.
    if base_url not in html:
        return html

    base_url = base_url.rstrip("/")

    try:
        doc = lxml_html.fromstring(html)
    except Exception:
        # If parsing fails, don't kill the build – just return original.
        return html

    # --- Handle <img> elements ---
    # XPath: all img with src starting with base_url
    img_nodes: list[LxmlElement] = doc.xpath(
        f"//img[starts-with(@src, '{base_url}')]"
    )

    for img in img_nodes:
        media_url = img.get("src")
        if not media_url:
            continue

        original_href = media_url

        # Decide width handling
        if "?" in media_url:
            img.set("data-dropper-width", "existing-query")
        else:
            if default_width:
                sized_src = f"{media_url}?width={int(default_width)}"
                img.set("src", sized_src)
                img.set("data-dropper-width", "added")
            else:
                img.set("data-dropper-width", "no-default")

        img.set("data-dropper", "processed")

        # Reuse existing <a> ancestor if present
        anchor = next(
            (a for a in img.iterancestors("a")),
            None,
        )

        if anchor is not None:
            anchor.set("data-dropper-anchor", "existing")
            if not anchor.get("href"):
                anchor.set("href", original_href)
            img.set("data-dropper-wrap", "already-wrapped")
        else:
            # Wrap in new <a>
            new_anchor = lxml_html.Element("a", href=original_href)
            new_anchor.set("data-dropper-anchor", "created")
            img.set("data-dropper-wrap", "new-wrapper")

            parent = img.getparent()
            if parent is not None:
                parent.replace(img, new_anchor)
                new_anchor.append(img)

    # --- Handle <video> elements ---
    video_nodes: list[LxmlElement] = doc.xpath("//video")

    for video in video_nodes:
        media_url, media_tag = _find_video_media_tag_lxml(video, base_url)
        if not media_url or media_tag is None:
            continue

        original_href = media_url

        # Width handling on the actual tag that holds src
        if "?" in media_url:
            video.set("data-dropper-width", "existing-query")
        else:
            if default_width:
                sized_src = f"{media_url}?width={int(default_width)}"
                media_tag.set("src", sized_src)
                video.set("data-dropper-width", "added")
            else:
                video.set("data-dropper-width", "no-default")

        # Mark root <video> as processed
        video.set("data-dropper", "processed")

        # Check if video already lives inside an <a>
        anchor = next(
            (a for a in video.iterancestors("a")),
            None,
        )

        if anchor is not None:
            anchor.set("data-dropper-anchor", "existing")
            if not anchor.get("href"):
                anchor.set("href", original_href)
            video.set("data-dropper-wrap", "already-wrapped")
        else:
            # Create a new <a> and wrap the <video>
            new_anchor = lxml_html.Element("a", href=original_href)
            new_anchor.set("data-dropper-anchor", "created")
            video.set("data-dropper-wrap", "new-wrapper")

            parent = video.getparent()
            if parent is not None:
                parent.replace(video, new_anchor)
                new_anchor.append(video)

    # Serialize back to HTML string
    return lxml_html.tostring(doc, encoding="unicode")


@hook_impl
def post_render(markata: "Markata") -> None:  # type: ignore[name-defined]
    """
    After render, wrap Dropper media in anchors and add sizing.

    Handles both string and dict forms of `post.html`.
    """

    cfg: DropperMediaWrapperConfig = markata.config.dropper_media_wrapper

    if not cfg.enabled:
        return

    try:
        default_width = int(cfg.default_width)
    except (TypeError, ValueError):
        default_width = 0

    base_url = cfg.base_url

    for post in markata.posts:
        html: Union[str, Dict[str, str], None] = getattr(post, "html", None)
        if not html:
            continue

        # String: single HTML variant
        if isinstance(html, str):
            post.html = _wrap_dropper_media_in_links_lxml(
                html,
                base_url=base_url,
                default_width=default_width,
            )
            continue

        # Dict of variants: {"index": ..., "partial": ...}
        if isinstance(html, dict):
            new_html: Dict[str, str] = {}
            for name, html_variant in html.items():
                if not html_variant:
                    new_html[name] = html_variant
                    continue

                new_html[name] = _wrap_dropper_media_in_links_lxml(
                    html_variant,
                    base_url=base_url,
                    default_width=default_width,
                )

            post.html = new_html
        # Other types are ignored silently.

