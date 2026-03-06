---
title: '💭 Use Alembic Check to check for possible upgrades'
date: 2023-08-05T01:22:06
template: link
link: None
tags:
  - python
  - data
  - database
  - alembic
  - thoughts
  - thought
  - link
published: true

---

![[None]]

Since using alembic I have been just running out a new revision checking its content and deleting it if its empty, today I learned there is an `alembic check` command to check for operations that need to be created.

``` bash
❯ alembic check
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
No new upgrade operations detected.
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
