from markata.hookspec import hook_impl
from more_itertools import flatten, unique_everseen
from rich import console

console = console.Console()

IGNORE_TAGS = [
    "rss",
    "",
]


@hook_impl()
def cli(app, markata):
    @app.command()
    def generate_feed_conf():
        """
        generate the config for tags
        """
        tags_of_tags = [
            [tag.lower().split(",") for tag in post.tags] for post in markata.posts
        ]
        tags = unique_everseen(flatten(flatten(tags_of_tags)))

        config = "# ---- GENERATED TAGS ----\n\n"
        for tag in tags:
            if tag in IGNORE_TAGS:
                console.print(f"[green]INFO: tag {tag} is ignored[/green]")
            else:
                tag = (
                    tag.strip()
                    .lower()
                    .replace(" ", "-")
                    .replace("/", "-")
                    .replace(":", "-")
                    .replace(".", "-")
                    .replace("_", "-")
                )
                if tag.replace("-", "_") in markata.feeds.keys():
                    console.print(f"[green]INFO: tag {tag} is already a feed[/green]")
                else:
                    if tag in markata.map("post.slug"):
                        console.print(
                            f"[red]WARNING: tag {tag} is already a post[/red]"
                        )
                    else:
                        config += f'[[markata.feeds]]\nslug = "{tag.lower()}"\nfilter = "date<=today and \'{tag}\' in tags and published"\nsort = "date"\nreverse = true\ndescription = "Posts about {tag}"\n\n'

        console.print(config, markup=False)
        try:
            import pyperclip

            pyperclip.copy(config)
        except ImportError:
            console.print(
                "[red]ERROR: pyperclip is not installed. Please install it to get results in your clipboard.[/red]"
            )
