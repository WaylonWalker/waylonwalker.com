---
date: 2025-01-31 20:17:00
templateKey: blog-post
title: markata 0.8.0
tags:
  - markata
published: True

---

I realize that I never did a post on markata  0.8.0, so here it is. 0.8.0 was
released on Jan 2, 2024, just over a year ago at this point.  This was the
release that we got pydantic support, and multi feeds.

![screenshot-2025-02-01T02-37-59-690Z.png](/api/file/76e6f022-360f-4566-9b35-a06cecd48738.png){.more-cinematic}

## Pydantic Support Was kinda big

Markata is leaning on pydantic for configuration and Post models.  These
models are filled with validators such that you can give it an empty markdown
post and it will figure out some pretty sane default values for the
frontmatter. From there you can progressively enhance your post with more
information like title, date, tags, slug, description.

> **validators are awesome!!** for instance I don't set the description on many
> of my posts by hand, I let the auto_description grab the first bit of text
> from the post most of the time.

## Multi Feeds

Markata==0.8.1 brought multiple feeds into the mix, and started to take place
of RSS and sitemap.  Feeds are a list of posts that are configured with a slug,
filter, sort, reverse, description, and a template.  These feeds then become
objects you can use to access posts, as well as html pages, RSS feeds and
sitemaps.

## Jinja Templates

The final major change within this series is the change out from string
templates to proper jinja templates with partial templates that you can
include.  This has made maintaining templates much easier, as well as the
ability to customize.  Markata will load templates from both your local
templates directory then from its built in templates directory if it does not
find a template locally.

``` toml
[[markata.feeds]]
slug = 'python'
filter = "date<=today and 'python' in str(tags).lower()"
sort = "date"
reverse = true
description = 'A feed of all my python posts'
```

* <https://waylonwalker.com/python/>
* <https://waylonwalker.com/python/rss.xml>
* <https://waylonwalker.com/python/sitemap.xml>
* <https://waylonwalker.com/python/partial/>

---

## Directly from the release notes

The rest of the post is details directly from the release notes.

## 0.8.2

* Fix: markata installs setuptools required by one dependency
* Fix: cleanup cli output
* Fix: speed up cli startup with some lazy imports
* Fix: all cache.adds were replaced with cache.set
* Fix: Updated to new typer format requiring name=
* Fix: teardown only runs if the build process was started, i.e. some cli's
  will not need to teardown

## 0.8.1

### Feeds have partials

The `feeds` plugin now has configurable `partial_template` that can be used to
render only the inside of the feeds page.  This is indented to allow you to
load small feeds into a page with htmx.

### Better Jinja Templates

Markata now fully supports jinja templates with a loader that will load from
your templates directory, the markata built-in templates, and from a
dynamically generated templates directory in your .markata.cache directory.

#### cli

You can list out your templates and configuration with the following command

``` bash
markata templates show
```

#### Variables

The following variables are available within jinja templates for post
templates.  This is now consistent across all three built in plugins that
render jinja templates.

##### post_template

* `__version__` - the version of markata
* `markata` - the markata instance
* `config` - the markata config
* `body` - the body of the post
* `post` - the current post object

##### feeds

Similarly from within rendering feeds.

* `__version__` - the version of markata
* `markata` - the markata instance
* `config` - the markata config
* `posts` - the list of posts
* `post` - a pseudo post object with title, slug, description, and date for template consistency
* `feed` - the current feed object

##### jinja_md

Similar to posts from within jinja_md to render a markdown post as a template.

* `__version__` - the version of markata
* `markata` - the markata instance
* `body` - the body of the post
* `config` - the markata config
* `post` - the current post object

#### Feeds cli

The feeds cli will help show which templates each feed will be using.

``` bash
❯ markata feeds show
                                          Feeds 6
┏━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃            Feed ┃ posts ┃ config                                                        ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ project_gallery │ 2     │ DEFAULT_TITLE: All Posts                                      │
│                 │       │ title: Project Gallery                                        │
│                 │       │ slug: project-gallery                                         │
│                 │       │ name: project_gallery                                         │
│                 │       │ filter: 'project-gallery' in str(path)                        │
│                 │       │ sort: title                                                   │
│                 │       │ reverse: False                                                │
│                 │       │ rss: True                                                     │
│                 │       │ sitemap: True                                                 │
│                 │       │ card_template: card.html                                      │
│                 │       │ template: feed.html                                           │
│                 │       │ rss_template: rss.xml                                         │
│                 │       │ sitemap_template: sitemap.xml                                 │
│                 │       │ xsl_template: rss.xsl                                         │
│                 │       │                                                               │
│            docs │ 10    │ DEFAULT_TITLE: All Posts                                      │
│                 │       │ title: Documentation                                          │
│                 │       │ slug: docs                                                    │
│                 │       │ name: docs                                                    │
│                 │       │ filter: "markata" not in slug and "tests" not in slug and ... │
│                 │       │ sort: slug                                                    │
│                 │       │ reverse: False                                                │
│                 │       │ rss: True                                                     │
│                 │       │ sitemap: True                                                 │
│                 │       │ card_template: card.html                                      │
│                 │       │ template: feed.html                                           │
│                 │       │ rss_template: rss.xml                                         │
│                 │       │ sitemap_template: sitemap.xml                                 │
│                 │       │ xsl_template: rss.xsl                                         │
│                 │       │                                                               │
│         autodoc │ 17    │ DEFAULT_TITLE: All Posts                                      │
│                 │       │ title: AutoDoc Python Modules.                                │
│                 │       │ slug: autodoc                                                 │
│                 │       │ name: autodoc                                                 │
│                 │       │ filter: "markata" in slug and "plugin" not in slug and "te... │
│                 │       │ sort: slug                                                    │
│                 │       │ reverse: False                                                │
│                 │       │ rss: True                                                     │
│                 │       │ sitemap: True                                                 │
│                 │       │ card_template: card.html                                      │
│                 │       │ template: feed.html                                           │
│                 │       │ rss_template: rss.xml                                         │
│                 │       │ sitemap_template: sitemap.xml                                 │
│                 │       │ xsl_template: rss.xsl                                         │
│                 │       │                                                               │
│             all │ 73    │ DEFAULT_TITLE: All Posts                                      │
│                 │       │ title: All Markata Modules                                    │
│                 │       │ slug: all                                                     │
│                 │       │ name: all                                                     │
│                 │       │ filter: True                                                  │
│                 │       │ sort: date                                                    │
│                 │       │ reverse: False                                                │
│                 │       │ rss: True                                                     │
│                 │       │ sitemap: True                                                 │
│                 │       │ card_template: card.html                                      │
│                 │       │ template: feed.html                                           │
│                 │       │ rss_template: rss.xml                                         │
│                 │       │ sitemap_template: sitemap.xml                                 │
│                 │       │ xsl_template: rss.xsl                                         │
│                 │       │                                                               │
│    core_modules │ 17    │ DEFAULT_TITLE: All Posts                                      │
│                 │       │ title: Markata Core Modules                                   │
│                 │       │ slug: core_modules                                            │
│                 │       │ name: core_modules                                            │
│                 │       │ filter: 'plugin' not in slug and 'test' not in slug and ti... │
│                 │       │ sort: date                                                    │
│                 │       │ reverse: False                                                │
│                 │       │ rss: True                                                     │
│                 │       │ sitemap: True                                                 │
│                 │       │ card_template: card.html                                      │
│                 │       │ template: feed.html                                           │
│                 │       │ rss_template: rss.xml                                         │
│                 │       │ sitemap_template: sitemap.xml                                 │
│                 │       │ xsl_template: rss.xsl                                         │
│                 │       │                                                               │
│         plugins │ 42    │ DEFAULT_TITLE: All Posts                                      │
│                 │       │ title: Markata Plugins                                        │
│                 │       │ slug: plugins                                                 │
│                 │       │ name: plugins                                                 │
│                 │       │ filter: 'plugin' in slug and 'test' not in slug               │
│                 │       │ sort: date                                                    │
│                 │       │ reverse: False                                                │
│                 │       │ rss: True                                                     │
│                 │       │ sitemap: True                                                 │
│                 │       │ card_template: card.html                                      │
│                 │       │ template: feed.html                                           │
│                 │       │ rss_template: rss.xml                                         │
│                 │       │ sitemap_template: sitemap.xml                                 │
│                 │       │ xsl_template: rss.xsl                                         │
│                 │       │                                                               │
└─────────────────┴───────┴───────────────────────────────────────────────────────────────┘
```

## 0.8.0

* pydantic support

### Pydantic Support

Now plugins are configured through a pydantic Config object.

### breaking changes

There are a number of breaking changes going into 0.8.0. Use caution when
upgrading.

#### glob config is now under markata.glob

```diff
- [markata]
- glob_patterns = "pages/**/*.md"
+ [markata.glob]
+ glob_patterns = "pages/**/*.md"
```

#### Feeds are now a list

Feeds are now a list of Objects within the configuration that you choose from
whether its toml or yaml.  Also templates_dir is now configurable, and once you
have a templates dir it is better to specify templates by name relative to your
templates_dir.

```toml
[markata]
templates_dir = "pages/templates"

[markata.feeds.published]
template="archive_template.html"
card_template = "feed_card.html"
filter="date<=today and templateKey in ['blog-post', 'til'] and status.lower()=='published'"
sort="date"
```

> old

```toml
[[markata.feeds.published]]
template="pages/templates/archive_template.html"
card_template = "pages/templates/feed_card.html"
filter="date<=today and templateKey in ['blog-post', 'til'] and status.lower()=='published'"
sort="date"
```

> new

### markata.summary.filter_count is now a list

The old way was to set up a dict, where the keys were the name, now its a list
of Objects with an explicit name field.

```toml
[markata.summary.filter_count.drafts]
filter="published == 'False'"
color='red'
```

> Old

```toml
[[markata.summary.filter_count]]
name='drafts'
filter="published == 'False'"
color='red'
```
