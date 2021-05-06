from pathlib import Path
from typing import TYPE_CHECKING

from markata.hookspec import hook_impl
from jinja2 import Template

if TYPE_CHECKING:
    from markata import Markata


@hook_impl
def render(markata: "Markata") -> None:
    template_file = markata.config["amp_template"]
    with open(template_file) as f:
        template = Template(f.read())
    for article in markata.iter_articles("apply template"):

        article.amp_html = template.render(
            body=article.article_html,
            title=article.metadata["title"],
            slug=article.metadata["slug"],
            date=article.metadata["date"],
        )


@hook_impl
def save(markata: "Markata") -> None:
    output_dir = Path(markata.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for article in markata.articles:
        article_path = output_dir / article["slug"] / "amp" / "index.html"
        article_path.parent.mkdir(parents=True, exist_ok=True)
        with open(article_path, "w+") as f:
            f.write(
                article.amp_html.replace(
                    '<html lang="en">',
                    '<html ⚡ lang="en">',
                ).replace('async=""', "async")
            )
