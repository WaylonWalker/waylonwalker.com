---
title: '💭 sqlite_utils Python library - sqlite-utils'
date: 2023-08-20T14:32:39
template: link
link: https://sqlite-utils.datasette.io/en/stable/python-api.html#full-text-search
tags:
  - python
  - sql
  - sqlite
  - fts
  - thoughts
  - thought
  - link
published: true

---

![[https://sqlite-utils.datasette.io/en/stable/python-api.html#full-text-search]]

sqlite-utils is primarily a cli tool for sqlite operations such as enabling full text search, and executing searches, but it also has a nice python api that is exposed and pretty straightforward to use.

``` python
from sqlite_utils import Database
db = Database("database.db")
db["post"].enable_fts(["title", "message", "tags])
db["post"].search("water")
```

This returns a generator object that you can iterate over the row objects with.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
