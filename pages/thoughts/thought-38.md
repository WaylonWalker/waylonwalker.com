---
title: '💭 Static Files - FastAPI'
date: 2023-07-28T14:59:37
templateKey: link
link: https://fastapi.tiangolo.com/tutorial/static-files/
tags:
  - python
  - fastapi
  - webdev
published: true

---

> Mounting static files in fastapi.

``` python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

[Original thought](https://fastapi.tiangolo.com/tutorial/static-files/)
