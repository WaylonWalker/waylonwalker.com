---
date: 2025-05-04 14:23:41
templateKey: til
title: ruff single line import
published: true
tags:
  - python
  - linting
  - ruff

---

I've been using ruff to lint my python code for quite awhile now, I was pretty
early to jump on it after release.  Some of my projects have had a nice
force-single-line setting and some have not.  I dug into the docs and it was
not clear what I needed to make it work.

``` toml
[tool.ruff]
select = ['I'] # you probably want others as well

[tool.ruff.isort]
force-single-line = true
```

Turns out I was missing **I**sort in the select list.
