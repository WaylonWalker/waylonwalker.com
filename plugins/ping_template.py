"""
ping_template - Map templateKey:ping to ping.html template

Automatically assigns ping.html template to posts with templateKey 'ping'

# Installation

Add to your hooks list in markata.toml:

```toml
hooks = [
    "plugins.ping_template",
    # ... your other hooks
]
```

# Usage

This plugin automatically maps posts with `templateKey: ping` to use the `ping.html` template.
No manual configuration is required - the plugin handles the mapping automatically.

"""

from typing import TYPE_CHECKING
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from markata import Markata


@hook_impl(trylast=True)
def pre_render(markata: "Markata") -> None:
    """Set template for ping posts before rendering."""
    for post in markata.posts:
        if hasattr(post, "templateKey") and post.templateKey == "ping":
            if not hasattr(post, "template") or post.template is None:
                post.template = "ping.html"
