---
title: '💭 sqlite_utils Python library - sqlite-utils'
date: 2023-08-20T14:32:39
templateKey: link
link: https://sqlite-utils.datasette.io/en/stable/python-api.html#full-text-search
tags:
  - python
  - sql
  - sqlite
  - fts
published: true

---

> sqlite-utils is primarily a cli tool for sqlite operations such as enabling full text search, and executing searches, but it also has a nice python api that is exposed and pretty straightforward to use.

``` python
from sqlite_utils import Database
db = Database("database.db")
db["post"].enable_fts(["title", "message", "tags])
db["post"].search("water")
```

This returns a generator object that you can iterate over the row objects with.

[Original thought](https://sqlite-utils.datasette.io/en/stable/python-api.html#full-text-search)
