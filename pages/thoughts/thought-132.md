---
title: '💭 sysid/sse-starlette'
date: 2023-10-12T19:14:45
template: link
link: https://github.com/sysid/sse-starlette
tags:
  - htmx
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/sysid/sse-starlette]]

sse-starlette provides server sent events for startlette and FastApi.  I'm evaluating for use with htmx.

## Installation:

``` bash
pip install sse-starlette
```
## Usage:

``` python
import asyncio
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from sse_starlette.sse import EventSourceResponse

async def numbers(minimum, maximum):
    for i in range(minimum, maximum + 1):
        await asyncio.sleep(0.9)
        yield dict(data=i)

async def sse(request):
    generator = numbers(1, 5)
    return EventSourceResponse(generator)

routes = [
    Route("/", endpoint=sse)
]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level='info')
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
