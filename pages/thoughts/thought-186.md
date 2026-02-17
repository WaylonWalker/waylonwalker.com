---
title: '💭 logs with FastAPI and Uvicorn · Issue #1508 · tiangolo/fastapi'
date: 2023-12-15T22:04:42
templateKey: link
link: https://github.com/tiangolo/fastapi/issues/1508
tags:
  - python
  - fastapi
  - webdev
published: true

---

> Setting an additional log handler to the uvicorn logger for access logs in fastapi was not straightforward, but This post was very helpful.


```
@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
```

[Original thought](https://github.com/tiangolo/fastapi/issues/1508)
