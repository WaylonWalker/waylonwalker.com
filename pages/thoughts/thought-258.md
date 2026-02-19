---
title: '💭 Handling Errors - FastAPI'
date: 2024-04-30T18:08:35
template: link
link: https://fastapi.tiangolo.com/tutorial/handling-errors/
tags:
  - webdev
  - fastapi
  - thoughts
  - thought
  - link
published: true

---

![[https://fastapi.tiangolo.com/tutorial/handling-errors/]]

This page shows how to customize your fastapi errors.  I found this very useful to setup common templates so that I can return the same 404's both programatically and by default, so it all looks the same to the end user.


``` python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
```

---


This post sat in draft for months.  I stumbled upon it again and found great success returning good error messages based on user preferences.  the default remains json, but if a user requests `text/html` it will be an html response, and text for `application/rtf` or `text/plain`

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
