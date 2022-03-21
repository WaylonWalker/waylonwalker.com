---
templateKey: blog-post
tags: ['blog', ]
title: How I deploy my blog in 2022 | https://waylonwalker.com/how-i-deploy-2022
title: https://waylonwalker.com/how-i-deploy-2022
date: 2021-10-29
status: draft
author: '@_waylonwalker'
styles:
    margin:
        bottom: 0
        left: 0
        right: 0
        top: 0
    padding:
        bottom: 0
        left: 10
        right: 10
        top: 0
    headings:
        '1':
            bg: default
            fg: '#ff66c4,bold,italics'
            prefix: ' ⇁ '
            suffix: ' ↽ '
    quote:
        side: '│'
        style:
            bg: default
            fg: '#aaa'
        top_corner: '╭'
        bottom_corner: '╰'
    title:
        bg: default
        fg: '#e1af66,bold,italics'
        fg: '#e1af66'
    author:
        bg: default
        fg: '#ff66c4,bold,italics'
        fg: '#368ce2'
    date:
        bg: default
        fg: '#ff66c4,bold,italics'
        fg: '#368ce2,bold,italics'
        fg: '#368ce2'
    slides:
        bg: default
        fg: '#ff66c4,bold,italics'
        fg: '#368ce2,bold,italics'
        fg: '#368ce2'

---


## How I Continuously Deliver Content to my Blog with Markdown, GitHub, Python, and netlify

Content at the speed of thought.

> well, as fast as I can type

## Me

* Mechanical Engineering
* Data Engineering
* Terminal Junkie

## Ask Questions in slido

Please ask questions in slido # 983 911 | App Dev 1 Track

## Slido Poll

Do **you** have a personal blog / notes / website?

> * Yes - Static, built with python
> * Yes - I manage a server running python
> * Yes - Not python
> * No

we will circle back around in a few minutes

## I'll give away my answer

* Yes - Static, built with python

## Slack Channel: #track-1-appdev

If you are in the slack give me a 🔥🔥🔥🔥🔥🔥🔥

Let's light up slack 🔥🔥🔥🔥🔥🔥🔥

## 4 parts

* Why
* My workflow
* Under the hood
* Open Source

## Part 1 WHY

## 2016

## I want to own my content

Twitter is a great networking tool, but it's rare to see anything more
than a few hours old.

## I want to own my content

No one can take my domain or shut down the platform that my content is on.

## Some of my Stats

* 48 Google top 10 ranking pages
* 6500 monthly clicks on google
* 12k page monthly views

> from ahrefs and google search console

## [Learn In Public](https://www.swyx.io/learn-in-public/)

I'm creating learning exhaust.

> Inspired by [swyx](https://www.swyx.io/learn-in-public/)
> https://www.swyx.io/learn-in-public/

## from swyx

> Whatever your thing is, make the thing you wish you had found when you
> were learning. Don’t judge your results by “claps” or retweets or
> stars or upvotes - just talk to yourself from 3 months ago. I keep an
> almost-daily dev blog written for no one else but me.


## Focus on content

I could not do any of this if I was focused on Building rather than
writing.

## Focus on content

No one needs elastic search navigate your first 50 posts.

> when you are starting

## Focus on content

No one is going to make comments.

> when you are starting

## Write for yourself

You are your biggest audience out of the gate.

> If you continue writing others like you will find you

## Don't worry about the Trolls

No one is going to take your python keys away.

## Slido Check

Please ask questions in slack/slido

## Part 2 Workflow and tools

> To the meat of the talk

1. Let's start by making a post
2. then show how it works under the hood

## If you take away anything

Focus on content that you want to consume.

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

## Let's start with a Til
_the process_

### shoutout to @[jbrancha](https://twitter.com/jbrancha)

Check out his amazing [til repo](https://github.com/jbranchaud/til)

> If you ask google very many questions about git, you will end up
> finding him on the top

## Copier

I use [copier](https://copier.readthedocs.io/en/stable/) for single file
templates.


## Copier give me a new page

How I Present from the terminal with lookatme
lookatme-slides

``` bash
copier copy ~/.copier-templates/`ls ~/.copier-templates |\
    fzf --header $(pwd) --preview='tree ~/.copier-templates/{} |\
    lolcat'` . \
```

## nvim open my file

!TIP Once it starts getting uncomfortable to find posts, its nice to have
good shortcuts to get around.

> I have about 700 files on my blog to sift through

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

## Cross Post

I have a plugin to convert my markdown to a more dev.to friendly format.

## Slido Check

Let'g grab a question from slack/slido

## Part 3 How it's deployed

In March of 2021 I made the big switch from a javascript based framework
to my own ssg.

## I thought it would be easy....

There are a bunch of open source libraries that do all the things I need
an ssg to do.

## Moving to python

One of the biggest selling points to moving back to python was that I
use it every day and know the ecosystem much better.

* [ipython](https://ipython.org/)
* [pyinstrument](https://github.com/joerick/pyinstrument)
* breakpoint

## Part 3 How it's deployed
_word of caution_

This part might be a lot of code coming quick.

* Show how it comes together
* Link to the slides

## Everything is markdown

``` python
pymdown-extensions
python-frontmatter
```

## frontmatter

All the metadata is defined in yaml frontmatter and read in with the
[python-frontmatter](https://github.com/eyeseast/python-frontmatter)
library.

``` yaml
---
templateKey: blog-post
tags: ['webdev', 'meta' ]
title: How I deploy my blog in 2022
date: 2021-10-29
status: draft

---
```

## setting up extensions

markata supports [pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/)

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

## [Pluggy](https://pluggy.readthedocs.io/en/stable/)

* comes from pytest
* allows users to easily modify the framework to their liking

> one of the biggest reasons I started down this path is that I wanted
> to build my own plugins all the way down framework.

## [Pluggy](https://pluggy.readthedocs.io/en/stable/)

[Pluggy](https://pluggy.readthedocs.io/en/stable/) is what I use to
implement my lifecycle.

* configure
* glob
* load
* pre_render
* render
* post_render
* save

## Pluggy

Pluggy allows the framework to crate a `hook_spec` and plugin authors to
implement hooks with the `hook_impl`.

``` python
"""Define hook specs."""
import pluggy


# the framework's definition
hook_spec = pluggy.HookspecMarker("markata")

# the plugin author's implementation
hook_impl = pluggy.HookimplMarker("markata")
```

## creating the hookspec

It's an empty class.

``` python
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

## creating the plugin manager

``` python
pm = pluggy.PluginManager("markata")
pm.add_hookspecs(hookspec.MarkataSpecs)

# register hooks
for hook in config.hooks:
    plugin = importlib.import_module(hook)
    pm.register(plugin)
```

## Diskcache

[Diskcache](https://github.com/grantjenks/python-diskcache/) allows you
to setup a persistent cache layer.

``` python
cache = FanoutCache(self.MARKATA_CACHE_DIR, statistics=True)
```

## make a key

To set soemthing to cache we need a unique identifier.

``` python
def make_hash(self, *keys: str) -> str:
    str_keys = [str(key) for key in keys]
    return hashlib.md5("".join(str_keys).encode("utf-8")).hexdigest()
```

## make a key

From my plugins I cache anything that the function I run touches.

* plugin code
* article content
* article frontmatter

``` python
from pathlib import Path

key = make_hash(Path(__file__).read_text(), article.content, article.metadata['title'])
```

## accessing the cache

Now that we have a cache and a key we can ask the cache for values.

``` python
html_from_cache = cache.get(key)
```

## if it's not yet been set

If the content is not yet set or has expired, you will get `None` back and need
to create the value.

``` python
html_from_cache = cache.get(key)
if html_from_cache is None:
    html = markata.md.convert(article.content)
    cache.add(key, html, expire=15 * 24 * 60)
else:
    html = html_from_cache
```

## Configuration

[anyconfig](https://github.com/ssato/python-anyconfig) is a great tool
to pull your config from generic config files.

* markta.toml
* markta.yaml
* markta.ini
* pyproject.toml

## Configuration

Anyconfig needs a `path`, `parser`, and `keys`.  The key is your tools
prefix

``` python
import anyconfig

anyconfig.load(
            path_specs= (Path() / f"markata.toml"),
            ac_parser= "toml",
            keys= ['markata'],
        )
```

## Configuration

Each key in the config files used with `anyconfig` must be prefixed with
the tool's name.

```
# markata.toml
[markata]
default_cache_expire = 1209600

[markata.auto_description.description]
len=160
```

## Markata was born

A plugins all the way doen static site generator written in python.

* 6 lifecycle methods
* 21 pre-defined plugins
* cache store
* toml based configuration

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

> Note: I run bleeding edge, don't do that

## Netlify

I use deploy to netlify but any static site host would work.

## Netlify -> Cloudflare Pages

Since Making the title I've moved to Cloudflare pages.

> Netlify is great, but I'm cheap and wanted analytics

## Results

markata.dev

Markdown to site, with seo, cover images, full works.

* seo/og tags
* cover images
* frontmatter cleansing
* feeds
* rss
* cli
* sitemap
* heading links
* build profiler

## Markata.dev

In early 2022 I packaged up my blog's backend as a package for others to use.

## Markata.dev

I now have several users running their site with what I have built

* My buddy has a near clone of mine with 15 posts
* Techdestructive

## Markata.dev

* plugins all the way down
* use the parts you want
* modify to your liking

## Markata.dev

It lets you get started quick, write content early, and grow into your own platform

## Markata.dev

⚠ I'ts still very much beta

## Open Source

```
# install it for your application
pip install markata

# try it out
pipx run markata build
```

## quickstart

```
mkdir pages
echo '# My First Post' > first-post.md
echo '# Hello World' > hello-world.md
```

```
# or if pipx is your thing
pix run markata build
```

## You can do it too

Don't worry about having the perfect post, just make something that is
useful to you, and others who will find it.

## Connect

* [ twitter ](https://twitter.com/_WaylonWalker)
* [ LinkedIn ](https://www.linkedin.com/in/waylonwalker/)
* [ GitHub ](https://github.com/WaylonWalker)
* [ Dev.to](https://dev.to/waylonwalker)
* [ twitch ](https://www.twitch.tv/waylonwalker)


## Links

* [Learn In Public](https://www.swyx.io/learn-in-public/)
* [swyx](https://www.swyx.io/learn-in-public/)
* [jbrancha](https://twitter.com/jbrancha)
* [til repo](https://github.com/jbranchaud/til)
* [copier](https://copier.readthedocs.io/en/stable/)
* [ipython](https://ipython.org/)
* [pyinstrument](https://github.com/joerick/pyinstrument)
* [python-frontmatter](https://github.com/eyeseast/python-frontmatter)
* [pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/)
* [Pluggy](https://pluggy.readthedocs.io/en/stable/)
* [Pluggy](https://pluggy.readthedocs.io/en/stable/)
* [Pluggy](https://pluggy.readthedocs.io/en/stable/)
* [Diskcache](https://github.com/grantjenks/python-diskcache/)
* [anyconfig](https://github.com/ssato/python-anyconfig)
