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
from bs4 import BeautifulSoup
from bs4.element import Tag
from markata.hookspec import hook_impl, register_attr

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


def _find_video_media_tag(video: Tag, base_url: str) -> tuple[str | None, Tag | None]:
    """Find the effective media URL for a `<video>` tag.

    Preference order:
    1. First `<source>` child whose `src` starts with `base_url`.
    2. The `<video>`'s own `src` attribute, if present and matching.

    Returns a tuple of `(src, tag_with_src)` where `tag_with_src` is the
    element whose `src` attribute should be updated (either the `<source>` or
    the `<video>` itself). If no matching URL is found, returns `(None, None)`.
    """

    base_url = base_url.rstrip("/")

    # Prefer <source> children
    for source in video.find_all("source", recursive=False):
        if not isinstance(source, Tag):  # pragma: no cover - defensive
            continue
        src = source.get("src")
        if src and src.startswith(base_url):
            return src, source

    # Fallback to <video src="..."> if present
    src = video.get("src")
    if src and src.startswith(base_url):
        return src, video

    return None, None


def _wrap_dropper_media_in_links(
    html: str,
    *,
    base_url: str,
    default_width: int,
) -> str:
    """Wrap Dropper `<img>`/`<video>` tags in anchors and size them.

    - Only touches media whose URL begins with `base_url`.
      - For `<img>`, this is the `src` on the `<img>` itself.
      - For `<video>`, this can be either the `src` on `<video>` or the `src`
        of the first `<source>` child within the `<video>`.
    - Wraps each `<img>` / `<video>` in an `<a>` to the original (pre-sized)
      URL.
    - Adds `?width=default_width` to the media URL when no query string exists.
    - Adds `data-dropper-*` attributes for debugging.
    """

    if not html:
        return html

    soup = BeautifulSoup(html, "html.parser")

    # Normalise base_url: we only care about prefix matching
    base_url = base_url.rstrip("/")

    # Only affect <img> and <video> elements
    for node in soup.find_all(["img", "video"]):
        if not isinstance(node, Tag):  # pragma: no cover - defensive
            continue

        media_url: str | None
        media_tag: Tag

        if node.name == "img":
            media_url = node.get("src")
            media_tag = node
        else:  # node.name == "video"
            media_url, media_tag_or_none = _find_video_media_tag(node, base_url)
            if media_tag_or_none is None:
                # No matching <source> or <video src> with our base_url
                continue
            media_tag = media_tag_or_none

        if not media_url or not media_url.startswith(base_url):
            continue

        original_href = media_url  # what we link to

        # Ensure width query param only if there is no existing query
        if "?" in media_url:
            node["data-dropper-width"] = "existing-query"
        else:
            if default_width:
                sized_src = f"{media_url}?width={int(default_width)}"
                media_tag["src"] = sized_src
                node["data-dropper-width"] = "added"
            else:
                node["data-dropper-width"] = "no-default"

        # Mark the root media node (img/video) as processed
        node["data-dropper"] = "processed"

        # Check if already inside an <a>
        anchor_ancestor: Tag | None = None
        parent = node.parent
        while parent is not None and isinstance(parent, Tag):
            if parent.name == "a":
                anchor_ancestor = parent
                break
            parent = parent.parent

        if anchor_ancestor is not None:
            # Reuse existing anchor
            anchor_ancestor["data-dropper-anchor"] = "existing"
            if not anchor_ancestor.get("href"):
                anchor_ancestor["href"] = original_href
            node["data-dropper-wrap"] = "already-wrapped"
            continue

        # Create a new <a> wrapper and wrap the node in-place
        new_anchor = soup.new_tag("a", href=original_href)
        new_anchor["data-dropper-anchor"] = "created"
        node["data-dropper-wrap"] = "new-wrapper"
        node.wrap(new_anchor)

    return str(soup)


@hook_impl
def post_render(markata: "Markata") -> None:  # type: ignore[name-defined]
    """After render, wrap Dropper media in anchors and add sizing.

    Handles both string and dict forms of `post.html`:

    - If `post.html` is a string, it is transformed directly.
    - If `post.html` is a dict (e.g. `{"index": ..., "partial": ..., "og": ...}`),
      each value is transformed independently.
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

        if isinstance(html, dict):
            new_html: Dict[str, str] = {}
            for name, html_variant in html.items():
                if not html_variant:
                    new_html[name] = html_variant
                    continue

                new_html[name] = _wrap_dropper_media_in_links(
                    html_variant,
                    base_url=base_url,
                    default_width=default_width,
                )

            post.html = new_html
        elif isinstance(html, str):
            post.html = _wrap_dropper_media_in_links(
                html,
                base_url=base_url,
                default_width=default_width,
            )
        # Any other type is ignored silently to avoid breaking builds.

