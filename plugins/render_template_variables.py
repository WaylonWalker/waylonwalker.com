import datetime

import pytz
from markata.hookspec import hook_impl, register_attr


@hook_impl
@register_attr("articles")
def pre_render(markata) -> None:
    for article in markata.iter_articles("rendering markdown"):

        if "date" not in article.keys():
            article["date"] = datetime.datetime.today().min

        if article["date"] is None:
            article["date"] = datetime.datetime.today().min

        if "datetime" not in article.keys():
            # all dates get cohersed to datetime later
            article["datetime"] = article["date"]

        if article["datetime"] is None:
            article["datetime"] = datetime.datetime.now().min

        if isinstance(article["date"], datetime.datetime):
            article["date"] = article["date"].date()

        if isinstance(article["datetime"], datetime.date):
            article["datetime"] = datetime.datetime.combine(
                article["datetime"], datetime.datetime.min.time()
            )

        if article["datetime"].tzinfo is None:
            article["datetime"] = article["datetime"].replace(tzinfo=pytz.utc)

        try:
            article["year"] = article["date"].year
        except KeyError:
            article["year"] = datetime.datetime.today().year
            article["date"] = datetime.datetime.today().min
