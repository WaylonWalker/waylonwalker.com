---
title: '💭 Static Files - FastAPI'
date: 2023-07-28T14:59:37
template: link
link: https://fastapi.tiangolo.com/tutorial/static-files/
tags:
  - python
  - fastapi
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://fastapi.tiangolo.com/tutorial/static-files/]]

Mounting static files in fastapi.

``` python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
