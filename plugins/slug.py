"""Flat Slug Plugin

Creates a slug in article.metadata if missing based on filename.
"""
from pathlib import Path, TYPE_CHECKING

from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from markata import Markata


@hook_impl(tryfirst=True)
def pre_render(markata: "Markata") -> None:
    """pre-render.

    [TODO:description]

    Args:
        markata: [TODO:description]

    Returns:
        [TODO:description]
    """
    for article in markata.iter_articles(description="creating slugs"):
        try:
            article["slug"] = article.metadata["slug"]
        except KeyError:
            article["slug"] = (
                (str(Path(article["path"]).parent / Path(article["path"]).stem))
                .replace("pages/", "")
                .replace("blog/", "")
                .replace("notes/", "")
            )
