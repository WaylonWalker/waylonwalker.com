---
date: 2024-04-16 21:31:24
templateKey: til
title: sqlite vacuum
published: true
tags:
  - data

---

Today I learned how to VACUUM a sqlite database and cut its size in about half.
It's a database that I have had running for quite awhile and has some decent
traffic on it.

Why is it important to do a VACUUM? In short its becuase the file system gets
fragmented with as data is updated. On delete the files are removed from the
database and marked as available for reuse in the filesystem, but the space is
not reclaimed.

To VACUUM a database, run the following sql command.  You can do it right form
the sqlite shell by running `sqlite3`.

> You will need about double the current size of the database as free space to
> do the VACUUM, you need space for a full copy, journaling or write ahead
> logs, and the existing database.

``` sql
VACUUM;
```

The docs are fantastic for [vacuum](https://www.sqlite.org/lang_vacuum.html).
