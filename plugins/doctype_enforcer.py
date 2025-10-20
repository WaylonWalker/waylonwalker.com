from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic
from markata.hookspec import hook_impl, register_attr

if TYPE_CHECKING:
    from typing import Optional
    from markata import Markata  # type: ignore


MARKATA_PLUGIN_NAME = "Doctype Enforcer"
MARKATA_PLUGIN_PACKAGE_NAME = "doctype_enforcer"



@hook_impl(trylast=True)
def post_render(markata: "Markata") -> None:
    """
    Ensure each rendered HTML page begins with a doctype.

    This mutates post.content in-place only when:
      - post.content looks like HTML, and
      - it does not already begin with a doctype (ignoring leading whitespace/BOM).
    """

    for post in markata.filter("not skip"):
        for key, html in post.html.items():
            if not isinstance(html, str):
                continue

            if not html.startswith("<!doctype"):
                doctype = "<!DOCTYPE html>\n"
                html = doctype + html
                post.html[key] = html
