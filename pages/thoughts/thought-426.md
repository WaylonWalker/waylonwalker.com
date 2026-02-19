---
title: '💭 Proper handling of None in WHERE condition · Issue #109 · fast...'
date: 2024-11-08T13:36:30
template: link
link: https://github.com/fastapi/sqlmodel/issues/109#issuecomment-1046223225
tags:
  - python
  - sqlmodel
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/fastapi/sqlmodel/issues/109#issuecomment-1046223225]]

SQLModel models ship with an `is_`, and `is_not` that you can use to compare to None without pesky linters complaining.

This comment summed it up quite well.

> I believe this is concerned entirely with SQLAlchemy, not with SQLModel, and has to do with the required semantics to construct a BinaryExpression object.
> Hero.age == None evaluates to a BinaryExpression object which is eventually used to construct the SQL query that the SQLAlchemy engine issues to your DBMS.
> Hero.age is None evaluates to False immediately, and not a BinaryExpression, which short-circuits the query no matter the value of age in a row.
> From a cursory search, it does not seem that the is operator can be overridden in Python. This could help explain why the only possibility is by using the == operator, which can be overridden.


so rather than using `Team.heros == None` we can use `Team.seros.is_(None)` which checks for itentity not equality.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
