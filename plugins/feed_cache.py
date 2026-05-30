"""
Plugin to cache expensive feed rendering and eliminate duplication.

This plugin pre-renders and caches the most expensive feed components
that would otherwise be rendered multiple times per page build.
"""

from typing import Dict, Any
from markata.hookspec import hook_impl


@hook_impl
def prerender(markata) -> None:
    """Pre-render expensive feed components to cache and eliminate duplication."""
    # Cache the most frequently rendered recent feeds
    expensive_feeds = ["recently_written", "recent_thoughts", "recent_stars"]

    for feed_name in expensive_feeds:
        if hasattr(markata.feeds, feed_name):
            feed = getattr(markata.feeds, feed_name)
            # Pre-render and cache the feed HTML
            template = markata.jinja_env.get_template("feed_sm_partial.html")
            cached_html = template.render(feed=feed)

            # Store in cache for later use
            cache_key = f"cached_feed_{feed_name}"
            markata.cache[cache_key] = cached_html
