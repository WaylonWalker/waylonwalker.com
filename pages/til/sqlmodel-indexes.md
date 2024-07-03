---
date: 2024-04-17 21:55:25
templateKey: til
title: sqlmodel indexes
published: true
tags:
  - python

---

I've really been enjoying using sqlmodel for my projects that need a database.
One thing that I definitely lacked on for too long was indexing my database.  I
hit a point with one database where it was taking 7s for pretty simple
paginated queries to return 10 records.

For every field that you will be querying on, you can create an index, by
setting it equal to `Field(index=True)`

``` python
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
```

_example courtesy of the docs_

!!! Note
     primary keys are indexed by default.

> The docs cover this pretty well, and in quite depth - [Optimizing Queries](https://sqlmodel.tiangolo.com/tutorial/indexes/)
