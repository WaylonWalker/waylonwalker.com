---
title: '💭 python - Concepts of backref and back_populate in SQLalchemy? ...'
date: 2024-03-06T01:55:42
template: link
link: https://stackoverflow.com/questions/51335298/concepts-of-backref-and-back-populate-in-sqlalchemy#answer-59920780
tags:
  - sqlalchemy
  - thoughts
  - thought
  - link
published: true

---

![[https://stackoverflow.com/questions/51335298/concepts-of-backref-and-back-populate-in-sqlalchemy#answer-59920780]]

Today I came across some sqlalchemy models that created some relationships, some used `backref` 
 some used `back_populates`.   I was stumped why, I had never came accross `backref` before and I felt skill issues sinking in.

## backref is considered legacy

https://docs.sqlalchemy.org/en/14/orm/backref.html

As stated in the sqlalchemy docs, backref is a legacy feature.  Its shorthand to creating relationships between parent and child, but only adding it to the parent.  While this is simpler it introduces some invisible magic.


!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
