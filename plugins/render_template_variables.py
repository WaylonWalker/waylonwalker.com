import datetime

from markata.hookspec import hook_impl, register_attr


@hook_impl
@register_attr("articles")
def pre_render(markata) -> None:
    for article in markata.iter_articles("rendering markdown"):
        try:
            article["date"] = datetime.datetime.today().min
            article["year"] = article["date"].year
        except KeyError:
            article["year"] = datetime.datetime.today().year
            article["date"] = datetime.datetime.today().min
        if isinstance(article["date"], datetime.datetime):
            # article["date"] = datetime.datetime.combine(
            #     article["date"], datetime.datetime.min.time()
            # )
            article["date"] = article["date"].date()
