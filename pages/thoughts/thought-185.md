---
title: '💭 How to group FastAPI endpoints in Swagger UI?'
date: 2023-12-15T15:30:37
templateKey: link
link: https://stackoverflow.com/questions/63762387/how-to-group-fastapi-endpoints-in-swagger-ui#answer-63762765
tags:
  - python
  - fastapi
  - webdev
published: true

---

>         Setting tags in your fastapi endpoints will group them in the docs.  You can also set some metadata around the tags to get nice descriptions.

Here is a full example from the post.

``` python
from fastapi import FastAPI

tags_metadata = [
    {"name": "Get Methods", "description": "One other way around"},
    {"name": "Post Methods", "description": "Keep doing this"},
    {"name": "Delete Methods", "description": "KILL 'EM ALL"},
    {"name": "Put Methods", "description": "Boring"},
]

app = FastAPI(openapi_tags=tags_metadata)


@app.delete("/items", tags=["Delete Methods"])
@app.put("/items", tags=["Put Methods"])
@app.post("/items", tags=["Post Methods"])
@app.get("/items", tags=["Get Methods"])
async def handle_items():
    return
```

[Original thought](https://stackoverflow.com/questions/63762387/how-to-group-fastapi-endpoints-in-swagger-ui#answer-63762765)
