---
date: 2024-04-22 19:54:24
templateKey: til
title: Redka Runs on SQLite
published: true
tags:
  - linux
  - infrastructure

---

With the liscense changes to redis there are several new forks out there.  One
that I am particularly interested in is
[redka](https://github.com/nalgeon/redka).

``` bash
curl https://i.jpillora.com/nalgeon/redka | bash
chmod +x redka
./redka database.db
```

We now have redis running on port 6379 that we can connect to with a redis
client. And we have a sqlite database that we can inspect.

``` bash
❯ sqlite3 database.db "SELECT name FROM sqlite_master;"
rkey
rkey_key_idx
rkey_etime_idx
rkey_on_type_update
rstring
rstring_pk_idx
vstring
rhash
rhash_pk_idx
rhash_key_id_idx
vhash
```

We can look at the values in the vstring table.

``` bash
sqlite3 database.db "SELECT * from vstring;"
1|hi|hello there you||2024-04-17 01:46:26
```
