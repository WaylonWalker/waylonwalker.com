---
title: '💭 logs with FastAPI and Uvicorn · Issue #1508 · tiangolo/fastapi'
date: 2023-12-15T22:04:42
template: link
link: https://github.com/tiangolo/fastapi/issues/1508
tags:
  - python
  - fastapi
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/tiangolo/fastapi/issues/1508]]

Setting an additional log handler to the uvicorn logger for access logs in fastapi was not straightforward, but This post was very helpful.


```
@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
