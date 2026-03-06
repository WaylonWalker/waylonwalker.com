---
title: '💭 Form Data - FastAPI'
date: 2023-07-28T14:59:37
template: link
link: https://fastapi.tiangolo.com/tutorial/request-forms/#define-form-parameters
tags:
  - fatapi
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://fastapi.tiangolo.com/tutorial/request-forms/#define-form-parameters]]

Getting form data inside of fastapi was not intuitive to me at first. Everything I had used in fastapi leaned on pydantic models.  Form data comes in differently and needs collected differently.

``` python
from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
