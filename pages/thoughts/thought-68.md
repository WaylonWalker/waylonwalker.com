---
title: '💭 API — Jinja Documentation'
date: 2023-08-04T23:35:09
template: link
link: https://jinja.palletsprojects.com/en/3.0.x/api/#jinja2.FileSystemLoader
tags:
  - python
  - jinja
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://jinja.palletsprojects.com/en/3.0.x/api/#jinja2.FileSystemLoader]]

I've definitely been missing out on setting up a proper jinja loader on a few projects, I need to lean on this a bit more.

``` python
class jinja2.FileSystemLoader(searchpath, encoding='utf-8', followlinks=False):
    '''
    Load templates from a directory in the file system.
    '''
```
> The path can be relative or absolute. Relative paths are relative to the current working directory.

``` python
loader = FileSystemLoader("templates")
# A list of paths can be given. The directories will be searched in order, stopping at the first matching template.
loader = FileSystemLoader(["/override/templates", "/default/templates"])
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
