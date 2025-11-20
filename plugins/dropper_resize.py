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

- Finds all `<img>` and `<video>` tags whose `src` begins with `base_url`.
- Wraps each in an `<a>` that links to the **original** (unsized) URL.
- If the `src` has **no** `?` query string and `default_width` is truthy,
  it updates the `src` to `src + "?width={default_width}"`.
- If the media tag is already inside an `<a>`, it reuses that anchor rather
  than nesting another one.
- Adds some `data-dropper-*` attributes for debugging/inspection.

Example result (simplified):

```html
<a href="https://dropper.wayl.one/api/file/…" data-dropper-anchor="created">
  <img
    src="https://dropper.wayl.one/api/file/…?width=500"
    data-dropper="processed"
    data-dropper-width="added"
    data-dropper-wrap="new-wrapper"
  >
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


def _wrap_dropper_media_in_links(
    html: str,
    *,
    base_url: str,
    default_width: int,
) -> str:
    """Wrap Dropper `<img>`/`<video>` tags in anchors and size them.

    - Only touches tags whose `src` begins with `base_url`.
    - Wraps each in an `<a>` to the original (pre-sized) URL.
    - Adds `?width=default_width` to the `src` when no query string exists.
    - Adds `data-dropper-*` attributes for debugging.
    """

    if not html:
        return html

    soup = BeautifulSoup(html, "html.parser")

    # Normalise base_url: we only care about prefix matching
    base_url = base_url.rstrip("/")

    # Only affect <img> and <video> elements
    for node in soup.find_all(["img", "video"]):
        src = node.get("src")
        if not src or not src.startswith(base_url):
            continue

        original_href = src  # what we link to

        # Ensure width query param only if there is no existing query
        if "?" in src:
            node["data-dropper-width"] = "existing-query"
        else:
            if default_width:
                sized_src = f"{src}?width={int(default_width)}"
                node["src"] = sized_src
                node["data-dropper-width"] = "added"
            else:
                node["data-dropper-width"] = "no-default"

        node["data-dropper"] = "processed"

        # Check if already inside an <a>
        anchor_ancestor = None
        parent = node.parent
        while parent is not None and getattr(parent, "name", None):
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

