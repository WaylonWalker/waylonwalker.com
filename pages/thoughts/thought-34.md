---
title: '💭 Python API - DuckDB'
date: 2023-07-28T14:59:37
template: link
link: https://duckdb.org/docs/api/python/overview.html
tags:
  - python
  - data
  - duckdb
  - thoughts
  - thought
  - link
published: true

---

![[https://duckdb.org/docs/api/python/overview.html]]

To persist data in duckdb you need to first make a connection to a duck db database.

``` python
con = duckdb.connect('file.db')
```

Then work off of the connection `con` rather than `duckdb`.


``` python
con.sql('CREATE TABLE test(i INTEGER)')
con.sql('INSERT INTO test VALUES (42)')
# query the table
con.table('test').show()
# explicitly close the connection
con.close()
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
