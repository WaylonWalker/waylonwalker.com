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
[markata.glossary]
filter = '"glossary" in post.templateKey'  # Filter to identify glossary posts
template_path = "templates/glossary-snippet.html"  # Jinja template for rendering glossary
```

# Usage

- Add short glossary entries to your content with `templateKey = "glossary"`.
- Include a list of `aliases` in each glossary post’s metadata.
- When rendering other posts, the plugin will find the first usage of each glossary term or alias and replace it with the rendered glossary snippet.

# Notes

- Only the first occurrence of a glossary term in each post is replaced.
- Aliases, titles, and slugs are respected when matching terms.
- Matches are ignored if they appear in code blocks, inline code, links, images, or HTML blocks.
- The glossary is not injected into glossary posts themselves.
"""

from markata.hookspec import hook_impl, register_attr
import pydantic
from pathlib import Path
from jinja2 import Template
from markdown_it import MarkdownIt
from markdown_it.token import Token

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
        terms = [post.title, post.slug]
        if hasattr(post, "aliases"):
            terms.extend(post.aliases)
        for term in terms:
            glossary[term.lower()] = post
    markata.glossary_terms = glossary


@hook_impl
def pre_render(markata: "Markata") -> None:
    glossary = markata.glossary_terms
    template_file = Path(markata.config.glossary.template_path)
    template = Template(template_file.read_text())
    md = MarkdownIt()

    for post in markata.filter("not skip"):
        used_terms = set()
        tokens = md.parse(post.content)

        for token in tokens:
            if token.type == "inline":
                new_children = []
                for child in token.children:
                    if child.type != "text":
                        new_children.append(child)
                        continue

                    content = child.content
                    lowered = content.lower()
                    for term, glossary_post in glossary.items():
                        if glossary_post == post:
                            continue
                        if term in used_terms:
                            continue
                        index = lowered.find(term)
                        if index == -1:
                            continue
                        rendered = template.render(
                            post=glossary_post, glossary_term=term
                        )
                        before = content[:index]
                        after = content[index + len(term) :]
                        new_children.append(Token("text", "", 0, content=before))
                        new_children.append(
                            Token("html_inline", "", 0, content=rendered)
                        )
                        new_children.append(Token("text", "", 0, content=after))
                        used_terms.add(term)
                        break
                    else:
                        new_children.append(child)
                token.children = new_children

        rendered_content = md.renderer.render(tokens, md.options, {})
        post.content = rendered_content
