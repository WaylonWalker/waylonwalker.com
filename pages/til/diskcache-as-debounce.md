---
date: 2024-07-03 11:14:11
templateKey: til
title: diskcache as debounce
published: true
tags:
  - python

---

I've been using fastapi more and more lately and one feature I just started
using is background tasks [[ thoughts-333 ]].

!!! seealso
    basic diskcache example [[ python-diskcache ]]

## One Background Task per db entry

I am using it for longer running tasks and I don't want to give users the
ability to spam these long running tasks with many duplicates running at the
same time. And each fastapi worker will be running in a different process so I
cannot keep track of work in memory, I have to do it in a distributed fashion.
Since they are all running on the same machine with access to the same disk,
diskcache is a good choice

## What I need

* check if a job is running
* automatically expire jobs

## Less infrastructure complexity

My brain first went to thinking I needed another service like redis running
alongside fastapi for this, then it hit me that I can use diskcache.

## How I used diskcache

Here is how I used diskcache to debounce taking screenshots for a unique shot
every 60 seconds.

``` python
from diskcache import Cache

jobs_cache = Cache("jobs-cache")

@shots_router.get("/shot/{shot_id}", responses={200: {"content": {"image/webp": {}}}})
@shots_router.get("/shot/{shot_id}/", responses={200: {"content": {"image/webp": {}}}})
async def get_shot_by_id(
    background_tasks: BackgroundTasks,
    request: Request,
    shot_id: int,
):
    shot = Shot.get(shot_id)
    # check if the shot exists and return it or continue to create it.



    is_running = jobs_cache.get(shot_id)

    if is_running:
        expire_time = datetime.fromtimestamp(jobs_cache.peekitem(expire_time=True)[1]) - datetime.now()
        console.print("[red]Already running store_shot: ", shot_id)
        console.print(f"[red]Can retry in {expire_time.seconds}s")
    else:
        jobs_cache.set(shot_id, True, 60)
        background_tasks.add_task(
            store_shot,
            shot_id=shot_id,
        )
```
