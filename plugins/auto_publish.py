from markata.hookspec import hook_impl


@hook_impl(trylast=True)
def load(markata):
    """
    change status to published for template
    """
    ...
    config = markata.get_plugin_config(__file__)
    for article in markata.articles:
        try:
            article["status"] = article.get("status", "draft")
        except:
            article["status"] = article.__dict__.get("status", "draft")
        if article["status"] == "published" and "published" not in article.keys():
            article["published"] = article.get("published", True)
        else:
            article["published"] = article.get("published", False)

    for filter in config["filters"].values():
        for article in markata.filter(filter):
            article["status"] = "published"
            article["published"] = True
