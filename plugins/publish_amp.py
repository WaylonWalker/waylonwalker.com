from pathlib import Path
from typing import TYPE_CHECKING

from jinja2 import Template
from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from markata import Markata


def _try_get_date(article):
    try:
        return article.metadata["date"]
    except KeyError:
        return None


@hook_impl
def render(markata: "Markata") -> None:
    template_file = markata.config["amp_template"]
    with open(template_file) as f:
        template = Template(f.read())
    with markata.cache as cache:
        for article in markata.iter_articles("apply amp template"):
            date = _try_get_date(article)
            key = markata.make_hash(
                __file__,
                Path(__file__).read_text(),
                "render",
                article["content"],
                article.article_html,
                article.metadata["title"],
                article.metadata["slug"],
                date,
            )
            amp_html_from_cache = cache.get(key)
            if amp_html_from_cache is None:
                amp_html = template.render(
                    body=article.article_html,
                    title=article.metadata["title"],
                    slug=article.metadata["slug"],
                    date=date,
                )
            else:
                amp_html = amp_html_from_cache
            article.amp_html = amp_html


@hook_impl
def save(markata: "Markata") -> None:
    output_dir = Path(markata.config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    for article in markata.articles:
        article_path = output_dir / article["slug"] / "amp" / "index.html"
        article_path.parent.mkdir(parents=True, exist_ok=True)
        with open(article_path, "w+") as f:
            f.write(
                article.amp_html.replace(
                    '<html lang="en">',
                    '<html ⚡ lang="en">',
                )
                .replace('async=""', "async")
                .replace('async="True"', "async")
            )
