---
title: '💭 Form Data - FastAPI'
date: 2023-07-28T14:59:37
templateKey: link
link: https://fastapi.tiangolo.com/tutorial/request-forms/#define-form-parameters
tags:
  - fatapi
  - webdev
published: true

---

> Getting form data inside of fastapi was not intuitive to me at first. Everything I had used in fastapi leaned on pydantic models.  Form data comes in differently and needs collected differently.

``` python
from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
```

[Original thought](https://fastapi.tiangolo.com/tutorial/request-forms/#define-form-parameters)
