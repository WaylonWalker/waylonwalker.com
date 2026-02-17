---
title: '💭 SQLite FTS5 Extension'
date: 2023-08-21T13:33:24
templateKey: link
link: https://www.sqlite.org/fts5.html
tags:
  - sqlite
  - data
  - database
published: true

---

> sqlite has 3 different tokenizers, `porter, ascii, trigram`.  

These can be used with sqlite-utils.

``` bash
sqlite-utils enable-fts --tokenize porter database.db post title message tags
```

And with the python api.

``` python
db = Database('database.db')
db["post"].enable_fts(
                ["title", "message", "tags"], create_triggers=True, tokenize="trigram"
            )
posts = list(db["post"].search(search))
```




[Original thought](https://www.sqlite.org/fts5.html)
