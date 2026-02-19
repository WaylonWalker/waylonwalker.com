---
title: '💭 Bigger Applications - Multiple Files - FastAPI'
date: 2023-08-24T14:51:23
template: link
link: https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter
tags:
  - python
  - api
  - fastapi
  - thoughts
  - thought
  - link
published: true

---

![[https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter]]

 Fastapi lets you tag your `APIRouter`'s so that the swagger docs are grouped according to the router.

``` python
router = APIRouter(tags=['router'])
```

Now all routes in `router` will appear in the router group in the swagger docs.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
