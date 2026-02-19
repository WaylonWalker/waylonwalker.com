---
title: '💭 Column INSERT/UPDATE Defaults — SQLAlchemy 1.4 Documentation'
date: 2023-07-28T14:59:37
template: link
link: https://docs.sqlalchemy.org/en/14/core/defaults.html#server-invoked-ddl-explicit-default-expressions
tags:
  - python
  - sql
  - sqlalchemy
  - thoughts
  - thought
  - link
published: true

---

![[https://docs.sqlalchemy.org/en/14/core/defaults.html#server-invoked-ddl-explicit-default-expressions]]

sqlalchemy server_defaults end up as defaults in the database when new values are inserted.

``` python
t = Table(
    "test",
    metadata_obj,
    Column("abc", String(20), server_default="abc"),
    Column("created_at", DateTime, server_default=func.sysdate()),
    Column("index_value", Integer, server_default=text("0")),
)

```

``` sql
CREATE TABLE test (
    abc varchar(20) default 'abc',
    created_at datetime default sysdate,
    index_value integer default 0
)
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
