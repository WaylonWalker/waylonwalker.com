import typer
from markata.hookspec import hook_impl
from more_itertools import flatten, unique_everseen
from rich import console

console = console.Console()

IGNORE_TAGS = [
    "rss",
    "",
]


def check_feed_conflicts(tag, existing_feeds):
    """Check for conflicts between a tag and existing feeds."""
    conflicts = []
    for feed_slug, feed_config in existing_feeds.items():
        # Match on slug patterns (with/without tag/ prefix)
        slug_patterns = [tag, f"tag/{tag}"]
        if any(pattern in feed_slug for pattern in slug_patterns):
            conflicts.append(
                {
                    "slug": feed_slug,
                    "filter": getattr(feed_config, "filter", ""),
                    "description": getattr(feed_config, "description", ""),
                    "type": "slug_match",
                }
            )

        # Match on filter content
        if f"'{tag}' in tags" in getattr(feed_config, "filter", ""):
            conflicts.append(
                {
                    "slug": feed_slug,
                    "filter": getattr(feed_config, "filter", ""),
                    "description": getattr(feed_config, "description", ""),
                    "type": "filter_match",
                }
            )
    return conflicts


@hook_impl()
def cli(app, markata):
    @app.command()
    def generate_feed_conf(
        all_flag: bool = typer.Option(
            False, "--all", "-a", help="Generate all configs, not just missing ones"
        ),
    ):
        """
        generate the config for tags
        """
        # Run only essential stages to get posts without running problematic plugins
        markata.run("load")

        tags_of_tags = [
            [tag.lower().split(",") for tag in post.tags] for post in markata.posts
        ]
        all_tags = unique_everseen(flatten(flatten(tags_of_tags)))
        all_tags_list = list(all_tags)  # Convert to list to preserve for later use

        # Get tag_aggregator data if available
        alias_to_canonical = {}
        canonical_tags = all_tags_list  # Default to all tags if no aggregator data

        # Try to get tag_aggregator_data without running pre_render
        if hasattr(markata.config, "tag_aggregator"):
            # Build the mappings manually from config
            synonyms = markata.config.tag_aggregator.synonyms
            additional = markata.config.tag_aggregator.additional

            for canonical_tag, aliases in synonyms.items():
                for alias in aliases:
                    alias_to_canonical[alias] = canonical_tag

            # Determine canonical tags by filtering out aliases
            canonical_tags = {
                tag for tag in all_tags_list if tag not in alias_to_canonical
            }

        # Get existing feeds from config without triggering pre_render
        existing_feeds = {}
        if hasattr(markata.config, "feeds"):
            for feed in markata.config.feeds:
                if hasattr(feed, "slug"):
                    existing_feeds[feed.slug] = feed

        for feed_slug, feed_config in existing_feeds.items():
            filter_str = getattr(feed_config, "filter", "")
            # Extract tag references from filter (handles both 'tag' in tags and 'tag' in str(tags).lower())
            import re

            # Match patterns like: 'tag' in tags OR 'tag' in str(tags).lower()
            tag_matches = re.findall(r"'([^']+)' in.*tags", filter_str)
            for tag_ref in tag_matches:
                if tag_ref in alias_to_canonical:
                    canonical_tag = alias_to_canonical[tag_ref]
                    console.print(
                        f"[yellow]WARNING: Feed '{feed_slug}' uses alias '{tag_ref}' (canonical: '{canonical_tag}')[/yellow]"
                    )

        force_mode = " (all mode)" if all_flag else ""
        config = f"# ---- GENERATED TAGS{force_mode} ----\n\n"
        for tag in all_tags_list:
            if tag in IGNORE_TAGS:
                console.print(f"[green]INFO: tag {tag} is ignored[/green]")
                continue

            # Skip alias tags - only process canonical tags
            if tag in alias_to_canonical:
                continue

            # Process canonical tags
            tag_normalized = (
                tag.strip()
                .lower()
                .replace(" ", "-")
                .replace("/", "-")
                .replace(":", "-")
                .replace(".", "-")
                .replace("_", "-")
            )

            # Check for conflicts with existing feeds (only skip for exact slug matches unless --all)
            conflicts = check_feed_conflicts(tag_normalized, existing_feeds)
            exact_slug_conflict = any(c["type"] == "slug_match" for c in conflicts)
            if exact_slug_conflict and not all_flag:
                continue  # Skip generating feed for exact slug conflicts

            # Check if it's already a feed (legacy check)
            tag_normalized_variant = tag_normalized.replace("-", "_")
            if tag_normalized_variant in existing_feeds and not all_flag:
                console.print(
                    f"[green]INFO: tag {tag_normalized} is already a feed[/green]"
                )
                continue

            # Check if tag conflicts with existing post slug
            if tag_normalized in markata.map("post.slug"):
                console.print(
                    f"[red]WARNING: tag {tag_normalized} is already a post[/red]"
                )
                continue

            # Generate feed config
            config += f'[[markata.feeds]]\nslug = "tag/{tag_normalized.lower()}"\nfilter = "date<=today and \'{tag_normalized}\' in tags and published"\nsort = "date"\nreverse = true\ndescription = "Posts about {tag_normalized}"\n\n'

        console.print(config, markup=False)
        try:
            import pyperclip

            pyperclip.copy(config)
        except ImportError:
            console.print(
                "[red]ERROR: pyperclip is not installed. Please install it to get results in your clipboard.[/red]"
            )
