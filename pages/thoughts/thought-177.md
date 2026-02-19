---
title: '💭 Path Operation Advanced Configuration - FastAPI'
date: 2023-12-12T01:37:35
template: link
link: https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#exclude-from-openapi
tags:
  - webdev
  - fastapi
  - thoughts
  - thought
  - link
published: true

---

![[https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#exclude-from-openapi]]

        Excluding routes from fastapi docs, can be done from the route configuration using `include_in_schema`.  This is handy for routes that are not really api based or duplicates.  


## From the Docs

``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", include_in_schema=False)
async def read_items():
    return [{"item_id": "Foo"}]
```

## trailing slash

I've had better luck just routing both naked and trailing slash routes in fastapi.  I've had api's deployed as a subroute to a site rather than a subdomain, and the automatic redirect betweens them tended to always get messed up.  This is pretty easy fix for the pain is causes just give vim a yyp, and if you don't want deuplicates in your docs, ignore one.

``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
@app.get("/items/", include_in_schema=False)
async def read_items():
    return [{"item_id": "Foo"}]
```

## favicon.ico

Now you do not need to deploy favicons to your api in any way,  it is nice to have it in your browser tab, but more importantly to me I hate having console errors that are meaningless, this gives the browser something to automatically grab and not log errors.

``` python
@app.get("/favicon.ico", include_in_schema=False)
def get_favicon():
    return RedirectResponse(url="https://fokais.com/favicon.ico", status_code=status.HTTP_302_FOUND)

```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
