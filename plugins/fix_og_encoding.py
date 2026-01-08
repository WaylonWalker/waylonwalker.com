"""
Meta Ampersand Fix

Stopgap plugin: in rendered HTML stored in `post.html` (a dict[str, str]),
find all `<meta ...>` tags and replace `&amp;` with `&` **only inside those meta tags**.

This is useful when upstream templating/rendering double-escapes ampersands in
meta tag attribute values (e.g. `content="a&amp;b"`).

# Installation

Add to your Markata hooks:

```toml
hooks = [
  "markata.plugins.meta_amp_fix",
]
```

# Configuration

Optional:

```toml
[meta_amp_fix]
enabled = true           # turn the stopgap on/off
log_changes = false      # log how many replacements were made
```

# Usage

Run your normal Markata build. After render, this plugin mutates `post.html`
in-place.

# Notes

- This intentionally does **not** touch the rest of the HTML to avoid breaking
  legitimate escaping in body content.
- It targets `<meta ...>` tags only (case-insensitive).
"""

from __future__ import annotations

import re
from typing import Any, Dict

import pydantic
from markata.hookspec import hook_impl, register_attr

MARKATA_PLUGIN_NAME = "Meta Ampersand Fix"
MARKATA_PLUGIN_PACKAGE_NAME = "meta-amp-fix"


class MetaAmpFixConfig(pydantic.BaseModel):
    enabled: bool = True
    log_changes: bool = False

    model_config = pydantic.ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True,
        extra="allow",
        str_strip_whitespace=True,
        validate_default=True,
        coerce_numbers_to_str=True,
        populate_by_name=True,
    )


class Config(pydantic.BaseModel):
    meta_amp_fix: MetaAmpFixConfig = MetaAmpFixConfig()


@hook_impl
@register_attr("config_models")
def config_model(markata: "Markata") -> None:
    markata.config_models.append(Config)


# Match <meta ...> or <meta ... />
# - case-insensitive
# - minimal match up to first >
_META_TAG_RE = re.compile(r"<meta\b[^>]*?>", re.IGNORECASE)


def _fix_meta_tags(html: str) -> tuple[str, int]:
    """
    Replace '&amp;' with '&' ONLY inside <meta ...> tags.
    Returns (updated_html, replacements_count).
    """
    replacements = 0

    def _sub(m: re.Match[str]) -> str:
        nonlocal replacements
        tag = m.group(0)
        if "&amp;" not in tag:
            return tag
        count = tag.count("&amp;")
        replacements += count
        return tag.replace("&amp;", "&")

    updated = _META_TAG_RE.sub(_sub, html)
    return updated, replacements


@hook_impl
def post_render(markata: "Markata") -> None:
    cfg = getattr(markata.config, "meta_amp_fix", MetaAmpFixConfig())
    if not getattr(cfg, "enabled", True):
        return

    total_replacements = 0
    total_posts_touched = 0

    for post in markata.filter("not skip"):
        html_dict: Any = getattr(post, "html", None)
        if not isinstance(html_dict, dict):
            continue

        changed_any = False
        new_html: Dict[str, str] = {}

        for key, value in html_dict.items():
            if not isinstance(value, str):
                new_html[key] = value
                continue

            fixed, n = _fix_meta_tags(value)
            new_html[key] = fixed
            if n:
                changed_any = True
                total_replacements += n

        if changed_any:
            post.html = new_html
            total_posts_touched += 1

    if getattr(cfg, "log_changes", True):
        markata.console.log(
            f"[meta_amp_fix] posts_touched={total_posts_touched} "
            f"meta_amp_replacements={total_replacements}"
        )

