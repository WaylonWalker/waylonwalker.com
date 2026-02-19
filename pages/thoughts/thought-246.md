---
title: '💭 sql - How can I list the tables in a SQLite database file that...'
date: 2024-04-18T01:13:59
template: link
link: https://stackoverflow.com/questions/82875/how-can-i-list-the-tables-in-a-sqlite-database-file-that-was-opened-with-attach#answer-83195
tags:
  - sqlite
  - thoughts
  - thought
  - link
published: true

---

![[https://stackoverflow.com/questions/82875/how-can-i-list-the-tables-in-a-sqlite-database-file-that-was-opened-with-attach#answer-83195]]

I learned about the sqlite_master table from this stack overflow answer.  This helps make a lot of sense to how sqlite works.  The master table contains all the sqlite objects and the sql to create them.

> The .tables, and .schema "helper" functions don't look into ATTACHed databases: they just query the SQLITE_MASTER table for the "main" database. Consequently, if you used

``` bash
sqlite3 database.db "SELECT * from sqlite_master;"
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
