---
date: 2024-04-17 20:03:27
templateKey: til
title: How to List Sqlite tables
published: true
tags:
  - python

---

You can inspect sqlite tables with the sqlite shell.

> note that you get into the shell with `sqlite3 database.db`

``` sql
.tables
```

I also learned that `.tables`, `.index` and `.schema` are helper functions that
query the `sqlite_master` table on the `main` database.

Here is an output from my redka database.  The sqlite_master table contains all
the sqlite objects type, name, tbl_name, rootpage, and sql to create them.

``` bash
❯ sqlite3 database.db "SELECT * from sqlite_master;"
table|rkey|rkey|2|CREATE TABLE rkey (
    id       integer primary key,
    key      text not null,
    type     integer not null,
        version  integer not null,
    etime    integer,
        mtime    integer not null
)
index|rkey_key_idx|rkey|3|CREATE UNIQUE INDEX rkey_key_idx on rkey (key)
index|rkey_etime_idx|rkey|4|CREATE INDEX rkey_etime_idx on rkey (etime)
where etime is not null
trigger|rkey_on_type_update|rkey|0|CREATE TRIGGER rkey_on_type_update
before update of type on rkey
for each row
when old.type is not new.type
begin
    select raise(abort, 'key type mismatch');
end
table|rstring|rstring|5|CREATE TABLE rstring (
    key_id integer not null,
    value  blob not null,

    foreign key (key_id) references rkey (id)
          on delete cascade
)
index|rstring_pk_idx|rstring|6|CREATE UNIQUE INDEX rstring_pk_idx on rstring (key_id)
view|vstring|vstring|0|CREATE VIEW vstring as
  select
    rkey.id as key_id, rkey.key, rstring.value,
        datetime(etime/1000, 'unixepoch') as etime,
        datetime(mtime/1000, 'unixepoch') as mtime
  from rkey join rstring on rkey.id = rstring.key_id
  where rkey.type = 1
    and (rkey.etime is null or rkey.etime > unixepoch('subsec'))
table|rhash|rhash|7|CREATE TABLE rhash (
    key_id integer not null,
    field text not null,
    value blob not null,

    foreign key (key_id) references rkey (id)
      on delete cascade
)
index|rhash_pk_idx|rhash|8|CREATE UNIQUE INDEX rhash_pk_idx on rhash (key_id, field)
index|rhash_key_id_idx|rhash|9|CREATE INDEX rhash_key_id_idx on rhash (key_id)
view|vhash|vhash|0|CREATE VIEW vhash as
  select
    rkey.id as key_id, rkey.key, rhash.field, rhash.value,
        datetime(etime/1000, 'unixepoch') as etime,
        datetime(mtime/1000, 'unixepoch') as mtime
  from rkey join rhash on rkey.id = rhash.key_id
  where rkey.type = 4
    and (rkey.etime is null or rkey.etime > unixepoch('subsec'))
```
