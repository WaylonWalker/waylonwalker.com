"""
glossary - inline glossary definitions

# Installation

```toml
hooks = [
  "markata.plugins.glossary",
]
```

# Configuration

```toml
[markata.glossary]
filter = 'post.templateKey == "glossary"'  # filter to find glossary posts
template = "{{ term }}"                       # jinja2 template used to inject definition
```

# Usage

Use this to inject inline definitions from glossary posts into other posts.
Glossary posts must have a templateKey == "glossary".
They can define `aliases` as a list of strings to match alternate terms.

# Notes

Only the first occurrence of each glossary term or alias in a post is replaced.
Replacement occurs in paragraph elements only, not in code blocks, titles, or other HTML structures.
Glossary terms are not replaced within their own post.

"""

from markata.hookspec import hook_impl, register_attr
import pydantic
from bs4 import BeautifulSoup

MARKATA_PLUGIN_NAME = "Glossary"
MARKATA_PLUGIN_PACKAGE_NAME = "glossary"


class GlossaryConfig(pydantic.BaseModel):
    filter: str = 'post.templateKey == "glossary"'
    template: str = "{{ term }}"

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
def config_model(markata):
    markata.config_models.append(Config)


@hook_impl
@register_attr("glossary_terms")
def load(markata):
    markata.glossary_terms = {}
    glossary_posts = markata.map("post", filter=markata.config.glossary.filter)

    for post in glossary_posts:
        terms = [post.title, post.slug] + post.get("aliases", [])
        for term in terms:
            markata.glossary_terms[term.lower()] = post


@hook_impl
def post_render(markata):
    template = markata.jinja_env.get_template(markata.config.glossary.template_path)
    for post in markata.posts:
        # if post.templateKey == "glossary":
        #     continue

        html_map = post.html if isinstance(post.html, dict) else {"default": post.html}
        new_html_map = {}

        for key, html in html_map.items():
            soup = BeautifulSoup(html, "html.parser")
            seen_terms = set()

            for p in soup.find_all("p"):
                text = p.decode_contents()

                for term, glossary_post in markata.glossary_terms.items():
                    if term in seen_terms:
                        continue
                    if glossary_post.slug == post.slug:
                        continue
                    if term in text.lower():
                        seen_terms.add(term)

                        rendered = template.render(
                            term=term,
                            glossary_post=glossary_post,
                            post=post,
                        )

                        # Replace only first occurrence with original casing
                        idx = text.lower().find(term)
                        original = text[idx : idx + len(term)]
                        text = text[:idx] + rendered + text[idx + len(term) :]

                        p.clear()
                        p.append(BeautifulSoup(text, "html.parser"))
                        break

            new_html_map[key] = str(soup)

        post.html = (
            new_html_map if isinstance(post.html, dict) else new_html_map.get("default")
        )
