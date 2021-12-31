from markata.hookspec import hook_impl


@hook_impl(trylast=True)
def load(markata):
    """
    change status to published for template
    """
    config = markata.get_plugin_config(__file__)
    for filter in config["filters"].values():
        for article in markata.filter(filter):
            article["status"] = "published"
