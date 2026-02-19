---
title: '💭 Using Rich Inspect to interrogate Python objects - Textual'
date: 2023-07-29T00:58:00
template: link
link: https://textual.textualize.io/blog/2023/07/27/using-rich-inspect-to-interrogate-python-objects/
tags:
  - python
  - rich
  - terminal
  - debugging
  - thoughts
  - thought
  - link
published: true

---

![[https://textual.textualize.io/blog/2023/07/27/using-rich-inspect-to-interrogate-python-objects/]]

I love rich inspect.  It's one of my most often used features of rich.  It gives you a great human readable insight into python object instances.

``` python
>>> from rich import inspect
>>> text_file = open("foo.txt", "w")
>>> inspect(text_file)
```

I have a pyflyby entry for it so that I can just run it ang get automatic imports.  To not clash with the standard library inspect, which is quite useful on it's own, I have aliased it to `rinspect`.

``` python
from rich import inspect as rinspect
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
