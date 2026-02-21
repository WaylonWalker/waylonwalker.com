---
title: '💭 Read a Range of Data - LIMIT and OFFSET - SQLModel'
date: 2024-01-12T02:18:35
template: link
link: https://sqlmodel.tiangolo.com/tutorial/limit-and-offset/
tags:
  - sqlmodel
  - sqlalchemy
  - orm
  - thoughts
  - thought
  - link
published: true

---

![[https://sqlmodel.tiangolo.com/tutorial/limit-and-offset/]]

Today I was running some sqlmodel queries through the sqlalchemy orm.  Admittedly I've not done enough orm queries before, and I've done quite a bit of raw sql. I was trying to get objects from two separate models that had relationships setup.

``` python
session.query(User, Images).where(User.id == 3).all()
```

It is incredibly slow, and gives me the following warning.

``` python
SELECT statement has a cartesian product between FROM element(s)
```

What I learned from the SQLModel docs is that you should give it a join to correct this and go much faster.

``` python
session.query(User, Images).join(Images).where(User.id == 3).all()
```



!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
