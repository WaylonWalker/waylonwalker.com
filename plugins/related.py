from typing import Union, List
from markata.hookspec import hook_impl
from string import Template
from pathlib import Path
from more_itertools import unique_everseen


@hook_impl
def pre_render(markata):
    published_articles = [a for a in markata.articles if a["status"] == "published"]
    published_articles.sort(key=lambda x: x["date"])
    for article in markata.iter_articles("related"):
        tags = article["tags"]
        try:
            index = published_articles.index(article)
            articles = published_articles[index:] + list(
                reversed(published_articles[:index])
            )
            articles = [a for a in articles if "slug" in a.metadata.keys()]

            tagged_articles = [
                a
                for a in articles
                if set(article["tags"]) & set(a["tags"]) and a != article
            ]
            related_articles = list(unique_everseen([*tagged_articles, *articles]))[:3]
            # article["related"] = related_articles
            article.content = (
                article.content + "\n\n---\n## Check Out These Related Posts\n\n"
            )
            article.content = article.content + "\n\n".join(
                [
                    "https://waylonwalker.com/" + a.metadata["slug"] + "/"
                    for a in related_articles
                ]
            )

        except ValueError:

            # article is not in published articles
            pass
