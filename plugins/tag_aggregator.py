"""Tag Aggregator Plugin with Reporting"""

from datetime import datetime
import json
from markata.hookspec import hook_impl, register_attr
import pydantic
from typing import Dict, List, Set


class TagAggregatorConfig(pydantic.BaseModel):
    synonyms: Dict[str, List[str]] = {}
    additional: Dict[str, List[str]] = {}


class Config(pydantic.BaseModel):
    tag_aggregator: TagAggregatorConfig = TagAggregatorConfig()


@hook_impl
@register_attr("post_models")
def config_model(markata: "Markata") -> None:
    markata.config_models.append(Config)


def expand_tags(tags: Set[str], additional: Dict[str, List[str]]) -> Set[str]:
    """Recursively expands tags based on additional mapping."""
    expanded_tags = set(tags)
    to_process = set(tags)

    while to_process:
        tag = to_process.pop()
        if tag in additional:
            new_tags = set(additional[tag])
            new_tags -= expanded_tags  # Avoid infinite loops
            expanded_tags.update(new_tags)
            to_process.update(new_tags)

    return expanded_tags


@hook_impl
def pre_render(markata: "Markata") -> None:
    synonyms = markata.config.tag_aggregator.synonyms
    additional = markata.config.tag_aggregator.additional

    tag_changes = []
    added_tags_report = []

    for post in markata.posts:
        original_tags = set(post.get("tags", []))

        # Normalize tags using synonyms
        normalized_tags = set()
        for tag in sorted(list(original_tags)):  # Preserve order of original_tags:
            normalized = False
            for correct_tag, replacements in synonyms.items():
                if tag in replacements:
                    normalized_tags.add(correct_tag)
                    tag_changes.append(f"[[ {post['slug']} ]]: {tag} -> {correct_tag}")
                    normalized = True
                    break
            if not normalized:
                normalized_tags.add(tag)

        # Recursively expand additional tags
        final_tags = expand_tags(normalized_tags, additional)

        added_tags = final_tags - normalized_tags
        added_tags = sorted(added_tags)
        if added_tags:
            added_tags_report.append(f"[[ {post['slug']} ]]: {', '.join(added_tags)}")

        post["tags"] = sorted(final_tags)

    # Generate content for report
    today = datetime.now().strftime("%Y-%m-%d")
    # config_section = (
    #     f"## Current Config\n\n```\n{markata.config.tag_aggregator.dict()}\n```\n"
    # )

    tag_aggregator_config = markata.config.tag_aggregator.dict()
    config_section = f"## Current Config\n\n```\n{json.dumps(tag_aggregator_config, indent=4)}\n```\n"
    tag_changes.sort()
    added_tags_report.sort()
    renamed_tags_section = (
        f"## Renamed Tags ( {len(tag_changes)} )\n\n* " + "\n* ".join(tag_changes)
        if tag_changes
        else "## Renamed Tags ( 0 )\n\nNo tags were renamed."
    )
    added_tags_section = (
        f"## Automatically Added Tags ( {len(added_tags_report)} )\n\n* "
        + "\n* ".join(added_tags_report)
        if added_tags_report
        else "## Automatically Added Tags ( 0 )\n\nNo additional tags were added."
    )

    content = f"""
# Tag Aggregator Report

Generated on {today}

{config_section}

{renamed_tags_section}

{added_tags_section}
"""

    # Create a blog post
    post_args = {
        "markata": markata,
        "templateKey": "plugin-report",
        "path": "tag-aggregator-report.md",
        "content": content,
        "raw": content,
        "tags": ["plugin-report"],
        "slug": "tag-aggregator-report",
        "title": "Tag Aggregator Report",
        "description": "Generated report from the tag aggregator plugin",
        "published": False,
        "date": today,
    }

    post = markata.Post.parse_obj(post_args)
    markata.Post.validate(post)
    markata.posts.append(post)
