"""
Glossary Terms Plugin

Replaces the first instance of a glossary term in each post with a rendered glossary snippet.

# Installation

Add to your `markata.toml` config:

```toml
hooks = ["markata.plugins.glossary"]
```

# Configuration

```toml
[glossary]
filter = '"glossary" in post.templateKey'  # Filter to identify glossary posts
template_path = "templates/glossary-snippet.html"  # Jinja template for rendering glossary
```

# Usage

- Add short glossary entries to your content with `templateKey = "glossary"`.
- Include a list of `aliases` in each glossary post’s metadata.
- When rendering other posts, the plugin will find the first usage of each glossary term or alias and replace it with the rendered glossary snippet.

# Notes

- Only the first occurrence of a glossary term in each post is replaced.
- Aliases are respected when matching terms.
"""

from markata.hookspec import hook_impl, register_attr
import pydantic
import re
from pathlib import Path
from jinja2 import Template

MARKATA_PLUGIN_NAME = "Glossary Terms"
MARKATA_PLUGIN_PACKAGE_NAME = "glossary"


class GlossaryConfig(pydantic.BaseModel):
    filter: str = '"glossary" in post.templateKey'
    template_path: str = "templates/glossary-snippet.html"

    model_config = pydantic.ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True,
        extra="allow",
        str_strip_whitespace=True,
        validate_default=True,
        coerce_numbers_to_str=True,
        populate_by_name=True,
    )


class Config(pydantic.BaseModel):
    glossary: GlossaryConfig = GlossaryConfig()


@hook_impl
@register_attr("config_models")
def config_model(markata: "Markata") -> None:
    markata.config_models.append(Config)


@hook_impl
@register_attr("glossary_terms")
def load(markata: "Markata") -> None:
    glossary_posts = markata.map("post", filter=markata.config.glossary.filter)
    glossary = {}

    for post in glossary_posts:
        terms = [post.slug]
        if hasattr(post, "aliases"):
            terms.extend([alias.lower() for alias in post.aliases])
        for term in terms:
            glossary[term] = post
    markata.glossary_terms = glossary


@hook_impl
def pre_render(markata: "Markata") -> None:
    glossary = markata.glossary_terms
    template_file = Path(markata.config.glossary.template_path)
    template = Template(template_file.read_text())

    for post in markata.filter("not skip"):
        used_terms = set()
        content = post.content

        for term, glossary_post in glossary.items():
            if term in used_terms:
                continue
            pattern = r"\\b" + re.escape(term) + r"\\b"

            def replacer(match):
                rendered = template.render(post=glossary_post)
                used_terms.add(term)
                return rendered

            new_content, count = re.subn(
                pattern, replacer, content, count=1, flags=re.IGNORECASE
            )
            if count > 0:
                content = new_content

        post.content = content
