---
title: '💭 sql - SQLite: COUNT slow on big tables - Stack Overflow'
date: 2024-04-01T20:59:40
template: link
link: https://stackoverflow.com/questions/8988915/sqlite-count-slow-on-big-tables
tags:
  - sql
  - sqlite
  - thoughts
  - thought
  - link
published: true

---

![[https://stackoverflow.com/questions/8988915/sqlite-count-slow-on-big-tables]]

Another interesting option for slow count queries in sqlite.

> If you haven't DELETEd any records, doing:

``` sql
SELECT MAX(ROWID) FROM "table" LIMIT 1;
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
