---
title: '💭 Read a Range of Data - LIMIT and OFFSET - SQLModel'
date: 2023-08-01T00:10:15
template: link
link: https://sqlmodel.tiangolo.com/tutorial/limit-and-offset/?h=#combine-limit-and-offset-with-where
tags:
  - python
  - thoughts
  - thought
  - link
published: true

---

![[https://sqlmodel.tiangolo.com/tutorial/limit-and-offset/?h=#combine-limit-and-offset-with-where]]

Implement paging in sqlmodel with where, limit, and offset.

``` python
def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age > 32).limit(3)
        results = session.exec(statement)
        heroes = results.all()
        print(heroes)
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
