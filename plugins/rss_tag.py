"""tagged rss plugin"""
from pathlib import Path
from typing import Dict

from feedgen.feed import FeedGenerator
from more_itertools import flatten

from markata import Markata
from markata.hookspec import hook_impl, register_attr


class MarkataRss(Markata):
    fg: "FeedGenerator"
    rss: str
    rss_tags: Dict


@hook_impl(trylast=True)
@register_attr("rss_tags")
def render(markata: "MarkataRss") -> None:
    status = "published"
    all_posts = reversed(sorted(markata.articles, key=lambda x: x["date"]))
    posts = [post for post in all_posts if post["status"] == status]
    tags = list(set(flatten([a["tags"] for a in markata.articles])))
    tagged_posts = {
        tag: [post for post in posts if tag in post["tags"]] for tag in tags
    }

    markata.rss_tags = {
        tag: make_rss(markata, posts, tag) for tag, posts in tagged_posts.items()
    }


def make_rss(markata: MarkataRss, posts: list, tag: str) -> FeedGenerator:
    fg = FeedGenerator()
    fg.id(markata.config["url"] + f"/{tag}-rss.xml")
    fg.title(f"{markata.config['title']} - {tag} posts")
    fg.author(
        {"name": markata.config["author_name"], "email": markata.config["author_email"]}
    )
    fg.link(href=markata.config["url"], rel="alternate")
    fg.logo(markata.config["icon"])
    fg.subtitle(f"{markata.config['rss_description']} - {tag} posts")
    fg.link(href=markata.config["url"] + f"/{tag}-rss.xml", rel="self")
    fg.language(markata.config["lang"])

    for article in posts:
        fe = fg.add_entry()
        fe.id(markata.config["url"] + "/" + article["slug"])
        fe.title(article.metadata["title"])
        fe.published(article.metadata["datetime"])
        fe.description(article.metadata["description"])
        fe.summary(article.metadata["long_description"])
        fe.link(href=markata.config["url"] + "/" + article["slug"])
        fe.content(article.article_html.translate(dict.fromkeys(range(32))))

    return fg


@hook_impl
def save(markata: "MarkataRss") -> None:
    output_dir = Path(markata.config["output_dir"])

    for tag, fg in markata.rss_tags.items():
        output_file = output_dir / tag / "rss.xml"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        fg.rss_file(str(output_file))
