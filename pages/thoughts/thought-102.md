---
title: '💭 Bigger Applications - Multiple Files - FastAPI'
date: 2023-08-24T14:51:23
templateKey: link
link: https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter
tags:
  - python
  - api
  - fastapi
published: true

---

>  Fastapi lets you tag your `APIRouter`'s so that the swagger docs are grouped according to the router.

``` python
router = APIRouter(tags=['router'])
```

Now all routes in `router` will appear in the router group in the swagger docs.

[Original thought](https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter)
