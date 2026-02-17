---
title: '💭 Optimizing SQLite for servers'
date: 2024-04-01T20:55:23
templateKey: link
link: https://kerkour.com/sqlite-for-servers
tags:
  - sql
  - sqlite
published: true

---

> Very interesting article by Sylvain, suggested by Simon Willison.

Definitely some things that I want to come back and try later on.


Here is the TLDR of the whole post

``` bash
PRAGMA journal_mode = WAL;
PRAGMA busy_timeout = 5000;
PRAGMA synchronous = NORMAL;
PRAGMA cache_size = 1000000000;
PRAGMA foreign_keys = true;
PRAGMA temp_store = memory;
```

This is interesting, and something I need to consider.  I definitely have an application with slow count queries.  I am not sure how to make it better as its not a full `count(*)` so a count table doesn't work, nor does counting by index.

I might need to have a table of cached results, and if a write matches the counter increase it, or update all counters on write.

> COUNT queries are slow
> SQLite doesn't keep statistics about its indexes, unlike PostgreSQL, so COUNT queries are slow, even when using a WHERE clause on an indexed field: SQLite has to scan for all the matching records.

> One solution is to use a trigger on INSERT and DELETE that updates a running count in a separate table then query that separate table to find the latest count.

[Original thought](https://kerkour.com/sqlite-for-servers)
