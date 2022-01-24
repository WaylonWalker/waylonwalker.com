---
templateKey: blog-post
tags: ['kedro', ]
title: How I deploy my blog in 2022
date: 2021-10-29
status: draft

---

This is my first cfp for [python web conf 2022](https://2022.pythonwebconf.com/).

## How I Continuously Deliver Content to my Blog with Markdown, GItHub, Python, and netlify

After being sick of long and broken builds from my javascript-based static site
generator I decided it was time to switch to a language I was far more
comfortable in.  At the time I was really interested in learning how to build
my own frameworks with pluggy, so a new static site generator was born.


## Description

## Markata was born

The idea of markata is a plugins all the way down static site generator at the
intersection of markdown and data.  It comes with 6 defines lifecycle methods,
21 pre-defined plugins, a cache store built on diskcahe, and a configuration
system.  Creating new functionality is as easy as making as decorating
lifecycle functions with a markata lifecycle method and adding it to the list
of active plugins in your markata.toml.

* 6 lifecycle methods
* 21 pre-defined plugins
* cache store
* toml based configuration

## Markdown

All of the content on this site is written in markdown and always has been.
Moving to the new site I chose to use pymdown-extensions so that I could
potentially use some of their great existing extensions.

```
pymdown-extensions
python-frontmatter
```

setting up extensions

``` python
DEFAULT_MD_EXTENSIONS = [
    "markdown.extensions.toc",
    "markdown.extensions.admonition",
    "markdown.extensions.tables",
    "markdown.extensions.md_in_html",
    "pymdownx.magiclink",
    "pymdownx.betterem",
    "pymdownx.tilde",
    "pymdownx.emoji",
    "pymdownx.tasklist",
    "pymdownx.superfences",
    "pymdownx.highlight",
    "pymdownx.inlinehilite",
    "pymdownx.keys",
    "pymdownx.saneheaders",
    "codehilite",
]

self.markdown_extensions = [*DEFAULT_MD_EXTENSIONS, *markdown_extensions]
self.md = markdown.Markdown(extensions=self.markdown_extensions)
```

## Pluggy


* comes from pytest
* allows users to easily modify the framework to their liking


``` python
"""Define hook specs."""
import pluggy

HOOK_NAMESPACE = "markata"

hook_spec = pluggy.HookspecMarker(HOOK_NAMESPACE)
hook_impl = pluggy.HookimplMarker(HOOK_NAMESPACE)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from markata import Markata


class MarkataSpecs:
    """
    Namespace that defines all specifications for Load hooks.

    glob -> load -> render -> save
    """

    @hook_spec
    def glob(self, markata: "Markata") -> None:
        """Glob for files to load."""
        pass

    @hook_spec
    def load(self, markata: "Markata") -> None:
        """Load list of files."""
        pass

    @hook_spec
    def pre_render(self, markata: "Markata") -> None:
        """Pre render content from loaded data."""
        pass

    @hook_spec
    def render(self, markata: "Markata") -> None:
        """Render content from loaded data."""
        pass

    @hook_spec
    def post_render(self, markata: "Markata") -> None:
        """Post render content from loaded data."""
        pass

    @hook_spec
    def save(self, markata: "Markata") -> None:
        """Save content from data."""
        pass
```

``` python
self._pm = pluggy.PluginManager("markata")
self._pm.add_hookspecs(hookspec.MarkataSpecs)
self._register_hooks()
```

## Diskcache

Markata defines a diskcache cache for you.

``` python
    @property
    def cache(self):
        return FanoutCache(self.MARKATA_CACHE_DIR, statistics=True)
```

Markata provides a convenience function to help make your own unique cache key
consistently.

``` python
def make_hash(self, *keys: str) -> str:
    str_keys = [str(key) for key in keys]
    return hashlib.md5("".join(str_keys).encode("utf-8")).hexdigest()
```

Plugins can access the cache, add to it, and set thier own expiration interval.
Here is an example from the built in markdown rendering function.

``` python
@hook_impl(tryfirst=True)
def render(markata: "Markata") -> None:
    with markata.cache as cache:
        for article in markata.iter_articles("rendering markdown"):
            key = markata.make_hash(
                "render_markdown", "render", article["content"]
            )
            html_from_cache = cache.get(key)
            if html_from_cache is None:
                html = markata.md.convert(article.content)
                cache.add(key, html, expire=15 * 24 * 60)
            else:
                html = html_from_cache
            article.html = html
            article.article_html = html
````

## Configuration

everything is in toml

## GitHub Actions

Rendering the site inside of github actions with the cache is pretty
straightforward with these four steps.  Keying off of the configuration will
bust the cache every time we change the configuration.  You can hack a full
rebuild by changing anything inside of the configuration file.

``` yaml

- name: Cache
uses: actions/cache@v2
with:
    path: .markata.cache
    key: ${{ runner.os }}-${{ hashfiles('markata.toml') }}-markata

- name: Set up Python 3.8
uses: actions/setup-python@v1
with:
    python-version: 3.8

- name: install markata
run: pip install git+https://github.com/WaylonWalker/markata.git@develop python-twitter background # checksumdir

- name: run markata
run: markata --no-rich
```
## Netlify

I deploy to netlify but any static site host would work.
