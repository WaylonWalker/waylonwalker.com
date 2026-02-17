---
title: '💭 FastAPI - dependency inside Middleware? - Stack Overflow'
date: 2023-12-17T17:05:46
templateKey: link
link: https://stackoverflow.com/questions/72243379/fastapi-dependency-inside-middleware#answer-72480781
tags:
  - fastapi
  - webdev
published: true

---

> After struggling to get dependencies inside of middleware I learned that you can make global dependencies at the app level.  I used this to set the user on every single route of the application without needing Depend on getting the user on each route.


``` python
from fastapi import Depends, FastAPI, Request


def get_db_session():
    print("Calling 'get_db_session(...)'")
    return "Some Value"


def get_current_user(session=Depends(get_db_session)):
    print("Calling 'get_current_user(...)'")
    return session


def recalculate_resources(request: Request, current_user=Depends(get_current_user)):
    print("calling 'recalculate_resources(...)'")
    request.state.foo = current_user


app = FastAPI(dependencies=[Depends(recalculate_resources)])


@app.get("/")
async def root(request: Request):
    return {"foo_from_dependency": request.state.foo}
```

[Original thought](https://stackoverflow.com/questions/72243379/fastapi-dependency-inside-middleware#answer-72480781)
