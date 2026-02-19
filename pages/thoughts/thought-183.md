---
title: '💭 Show some equivalent list comprehensions in filter examples · ...'
date: 2023-12-14T20:28:34
template: link
link: https://github.com/pallets/jinja/issues/1068
tags:
  - webdev
  - python
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/pallets/jinja/issues/1068]]

I often want to reach for non existing list comprehensions in jinja 2, Here are a few nice equivalents.

``` python
a: {{ data | selectattr('x', 'gt', 5) | list }}
b: {{ data | map(attribute='c') | list }} 
c: {{ data | selectattr('x', 'gt', 5) | map(attribute='c') | list }} 
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
