---
templateKey: blog-post
tags: ['blog', ]
title: How I deploy my blog in 2022 | https://waylonwalker.com/how-i-deploy-2022
date: 2021-10-29
status: draft

---

## How I Continuously Deliver Content to my Blog with Markdown, GItHub, Python, and netlify

Content at the speed of thought.

> well, as fast as I can type

## 3 parts

* Why
* My workflow
* Under the hood

## I want to own my content

Twitter is a great networking tool, but it's rare to see anything more
than a few hours old.

## [Learn In Public](https://www.swyx.io/learn-in-public/)

I'm just some guy that posts about what I am learning.

> Inspired by [swyx](https://www.swyx.io/learn-in-public/)

## Some Stats

* 48 Google top 10 ranking pages
* 6500 monthly clicks on google
* 12k page monthly views

## Focus on content

I could not do any of this if I was focused on Building rather than
writing.

## Focus on content

No one needs elastic search navigate your first 50 posts.

## Focus on content

No one is going to make comments.

## Write for yourself

You are your biggest audience out of the gate.

> If you continue writing others like you will find you

## Part 2 Workflow and tools

> To the meat of the talk

1. Let's start by making a post
2. then show how it works under the hood

## My Flow

``` txt
   ┌───────┐
   │  TIL  │
   └─┬─────┘
     │
     │  ┌─────────────┐
     │  │             │
     └─►│    Posts    │
        │             │
        └─┬───────────┘
          │
          │   ┌────────────────┐
          └──►│    YouTube     │
          │   └────────────────┘
          │   ┌────────────────┐
          └──►│    Conference  │
              │    Talks       │
              └────────────────┘
```

## Let's Make a Til
_the process_

### shoutout to @[jbrancha](https://twitter.com/jbrancha)

Check out his amazing [til repo](https://github.com/jbranchaud/til)

> If you ask google very many questions about git, you will end up
> finding him on the top

## Copier give me a new page

``` bash
copier copy ~/.copier-templates/`ls ~/.copier-templates |\
    fzf --header $(pwd) --preview='tree ~/.copier-templates/{} |\
    lolcat'` . \
```

## nvim open my file

Once it starts getting uncomfortable to find posts, its nice to have
good shortcuts to get around.

## nvim open my file

``` bash
markata list --map path --filter 'templateKey=="til"' --sort date --reverse
```

``` vim
nnoremap geil <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,templateKey=='til',--sort,date,--reverse<cr>
```

## Paste in a snippet

Often times I am working away on some sort of project, and I just need
to save a snippet for a later post.

## Write the content

Later I come back and fill in the content.

## git push

I have a vim hotkey `gic` to commit my current file, and `gpp` to push
it.

## It's nearly live

It will be live within a few minutes.

## Cross Post

I've tried to cross post to more, but it really gets overwhelming.

* Twitter
* dev.to

## Part 3 How it's deployed

After being sick of long and broken builds from my javascript-based static site
generator I decided it was time to switch to a language I was far more
comfortable in.  At the time I was really interested in learning how to build
my own frameworks with pluggy, so a new static site generator was born.

## Part 3 How it's deployed

This part might be a ton of code coming quick.

* Show how it comes together
* Link to the slides

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

## frontmatter

By the time I get out of my

``` yaml
---
templateKey: blog-post
tags: ['kedro', ]
title: How I deploy my blog in 2022
date: 2021-10-29
status: draft

---
```

## Everything is markdown

``` python
pymdown-extensions
python-frontmatter
```

## setting up extensions

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
```

## setting the markdown object

``` python
self.markdown_extensions = [
    *DEFAULT_MD_EXTENSIONS,
    *markdown_extensions
]
self.md = markdown.Markdown(
    extensions=self.markdown_extensions
)
```

## Pluggy

* comes from pytest
* allows users to easily modify the framework to their liking

``` python
"""Define hook specs."""
import pluggy


hook_spec = pluggy.HookspecMarker("markata")
hook_impl = pluggy.HookimplMarker("markata")

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

Diskcache allows you to setup a persistent cache layer

``` python
def cache(self):
    return FanoutCache(self.MARKATA_CACHE_DIR, statistics=True)
```

## make a key

Markata provides a convenience function to help make your own unique cache key
consistently.

``` python
def make_hash(self, *keys: str) -> str:
    str_keys = [str(key) for key in keys]
    return hashlib.md5("".join(str_keys).encode("utf-8")).hexdigest()
```

## accessing the cache

Plugins can access the cache, add to it, and set thier own expiration interval.
Here is an example from the built in markdown rendering function.

## accessing the cache

``` python
@hook_impl(tryfirst=True)
def render(markata: "Markata") -> None:
    with markata.cache as cache:
        plugin_code = Path(__file__).read_text()
        for article in markata.iter_articles():
            key = markata.make_hash(
                 plugin_code, article.content
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

## GitHub Actions

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

## GitHub Actions

``` python
- name: install markata
run: pip install git+https://github.com/WaylonWalker/markata.git@develop python-twitter background # checksumdir
```

I run bleeding edge, don't do that

## Netlify

I deploy to netlify but any static site host would work.

## Netlify -> Cloudflare Pages

Since Making the title I've moved to Cloudflare pages.

> Netlify is great, but I'm cheap and wanted analytics

## Results

markata.dev

Markdown to site, with seo, cover images, full works.
