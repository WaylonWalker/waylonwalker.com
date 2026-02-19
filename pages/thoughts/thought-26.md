---
title: '💭 URL Decoding query strings or form parameters in Python | URLD...'
date: 2023-07-28T14:59:37
template: link
link: https://www.urldecoder.io/python/
tags:
  - python
  - urlib
  - fastapi
  - thoughts
  - thought
  - link
published: true

---

![[https://www.urldecoder.io/python/]]

In order to turn url encoded links back into links that I would find in the database of my thoughts project I need to urldecode them when they hit the api.  When anything hits the api it must urlencode the links in order for them to be sent correctly as data and not get parsed as part of the url.


> Here is a snippet of how I am using urlib.parse.unquote to un-encode encoded urls so that I can fetch posts from the database.

``` python
@post_router.get("/link/")
async def get_post_by_link(
    *,
    session: Session = Depends(get_session),
    link: str,
) -> PostRead:
    "get one post by link"
    link = urllib.parse.unquote(link)
    print(f'link: {link}')
    post = session.exec(select(Post).where(Post.link==link)).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post not found for link: {link}")

    return post
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
