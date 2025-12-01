---
date: 2022-03-23 03:18:48.631729
templateKey: til
title: How I load Markdown in Python
tags:
  - python

---

I use a package
[eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter){.hoverlink}
to load files with frontmatter in them.  Its a handy package that allows you to
load files with structured frontmatter (yaml, json, or toml).

## Install

It's on pypi, so you can install it into your virtual environment with pip.

```bash
python -m pip install python-frontmatter
```

## 🙋 What's Frontmatter

Frontmatter is a handy way to add metadata to your plain text files.  It's
quite common to have yaml frontmatter in markdown.  All of my blog posts have
yaml frontmatter to give the post metadata such as post date, tags, title, and
template.  dev.to is a popular developer blogging platform that also builds all
of its posts with markdown and yaml frontmatter.

## Let's see an example

Here is the exact frontmatter for this post you are reading on my site.

```markdown
---
date: 2022-03-24 03:18:48.631729
templateKey: til
title: How I load Markdown in Python
tags:
  - linux
  - python

---

This is where the markdown content for the post goes.
```

## So it's yaml

yaml is the most commmon, but
[python-frontmatter](https://pypi.org/project/python-frontmatter/){.hoverlink}
also supports
[Handlers](https://python-frontmatter.readthedocs.io/en/latest/handlers.html?highlight=toml#module-frontmatter.default_handlers){.hoverlink}
for toml and json.

If you want a good set of examples of yaml
[learnxinyminutes](https://learnxinyminutes.com/docs/yaml/){.hoverlink} has a fantastic set
of examples in one page.

## How to load yaml frontmatter in python

Here is how I would load this post into python using
[python-frontmatter](https://pypi.org/project/python-frontmatter/){.hoverlink}.

```python
import frontmatter
inspect(frontmatter.load("pages/til/python-frontmatter.md"))
```

We can use [rich](https://github.com/Textualize/rich){.hoverlink} to inspect the Post
object to see what all it contains.

```python
❯ inspect(frontmatter.load("pages/til/python-frontmatter.md"))
╭────────────────────────────────────────────────────────── <class 'frontmatter.Post'> ───────────────────────────────────────────────────────────╮
│ A post contains content and metadata from Front Matter. This is what gets                                                                       │
│ returned by :py:func:`load <frontmatter.load>` and :py:func:`loads <frontmatter.loads>`.                                                        │
│ Passing this to :py:func:`dump <frontmatter.dump>` or :py:func:`dumps <frontmatter.dumps>`                                                      │
│ will turn it back into text.                                                                                                                    │
│                                                                                                                                                 │
│ ╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │ <frontmatter.Post object at 0x7f03c4c23ca0>                                                                                                 │ │
│ ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│                                                                                                                                                 │
│  content = "I use a package\n[eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter)\nto load files with frontmatter in   │
│            them.  Its a handy package that allows you to\nload files with structured frontmatter (yaml, json, or toml).\n\n## Install\n\nIt's   │
│            on pypi, so you can install it into your virtual environment with pip.\n\n```bash\npython -m pip install                             │
│            python-frontmatter\n```\n\n## 🙋 What's Frontmatter\n\nFrontmatter is a handy way to add metadata to your plain text files.          │
│            It's\nquite common to have yaml frontmatter in markdown.  All of my blog posts have\nyaml frontmatter to give the post metadata such │
│            as post date, tags, title, and\ntemplate.  dev.to is a popular developer blogging platform that also builds all\nof its posts with   │
│            markdown and yaml frontmatter.\n\n## Let's see an example\n\nHere is the exact frontmatter for this post you are reading on my       │
│            site.\n\n```markdown\n---\ndate: 2022-03-24 03:18:48.631729\ntemplateKey: til\ntitle: How I load Markdown in Python\ntags:\n  -      │
│            linux\n  - python\n\n---\n\nThis is where the markdown content for the post goes.\n```\n\n## So it's yaml\n\nyaml is the most        │
│            commmon, but\n[eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter)\nalso                                    │
│            supports\n[Handlers](https://python-frontmatter.readthedocs.io/en/latest/handlers.html?highlight=toml#module-frontmatter.default_ha… │
│            toml and json.\n\nIf you want a good set of examples of yaml\n[learnxinyminutes](https://learnxinyminutes.com/docs/yaml/) has a      │
│            fantastic set\nof examples in one page.\n\n## How to load yaml frontmatter in python"                                                │
│  handler = <frontmatter.default_handlers.YAMLHandler object at 0x7f03bffbd910>                                                                  │
│ metadata = {                                                                                                                                    │
│                'date': datetime.datetime(2022, 3, 24, 3, 18, 48, 631729),                                                                       │
│                'templateKey': 'til',                                                                                                            │
│                'title': 'How I load Markdown in Python',                                                                                        │
│                'tags': ['linux', 'python', 'python']                                                                                            │
│            }                                                                                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Getting Metadata

You can get items from the posts metadata just as you would from a dict.

```python
post = frontmatter.load("pages/til/python-frontmatter.md")
post['date']
# datetime.datetime(2022, 3, 24, 3, 18, 48, 631729)

post.get('date')
# datetime.datetime(2022, 3, 24, 3, 18, 48, 631729)
```

[[ python-dict-get ]]

> I have recently become fond of the `.get` method to give it an easy default value.

## Content is content

The content of the document is stored under `.content`

```python
post.content
```

## Links

* [python dict get](https://waylonwalker.com/til/python-dict-get/)
* [eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter)
* [python-frontmatter](https://pypi.org/project/python-frontmatter/)
* [python-frontmatter Handlers](https://python-frontmatter.readthedocs.io/en/latest/handlers.html?highlight=toml#module-frontmatter.default_handlers)
* [learnxinyminutes](https://learnxinyminutes.com/docs/yaml/)
* [python-frontmatter](https://pypi.org/project/python-frontmatter/)
* [rich](https://github.com/Textualize/rich)
