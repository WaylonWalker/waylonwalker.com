---
title: '💭 FastHX'
date: 2024-07-10T12:53:15
template: link
link: https://volfpeter.github.io/fasthx/
tags:
  - webdev
  - fastapi
  - htmx
  - thoughts
  - thought
  - link
published: true

---

![[https://volfpeter.github.io/fasthx/]]

Very interesting approach to htmx and fast api.  It uses separate decorators for returning template partials and json that can be stacked to include both options on a single route.  The templates are explicitly set in the decorator.  Separate decorators are used for full page and partial pages.  I don't see an example of full and partial pages being combined.  I think the demo app must be behaving in a spa like fashion where it does not get all of the data when it calls index and index will ask for user-list.

Definitely going to keep my eye on this project and ponder on it.


``` python
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx import Jinja
from pydantic import BaseModel

# Pydantic model of the data the example API is using.
class User(BaseModel):
    first_name: str
    last_name: str

# Create the app.
app = FastAPI()

# Create a FastAPI Jinja2Templates instance and use it to create a
# FastHX Jinja instance that will serve as your decorator.
jinja = Jinja(Jinja2Templates("templates"))

@app.get("/")
@jinja.page("index.html")
def index() -> None:
    ...

@app.get("/user-list")
@jinja.hx("user-list.html")
async def htmx_or_data() -> list[User]:
    return [
        User(first_name="John", last_name="Lennon"),
        User(first_name="Paul", last_name="McCartney"),
        User(first_name="George", last_name="Harrison"),
        User(first_name="Ringo", last_name="Starr"),
    ]

@app.get("/admin-list")
@jinja.hx("user-list.html", no_data=True)
def htmx_only() -> list[User]:
    return [User(first_name="Billy", last_name="Shears")]

```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
