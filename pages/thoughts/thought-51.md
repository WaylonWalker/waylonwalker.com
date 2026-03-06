---
title: '💭 Header Parameters - FastAPI'
date: 2023-07-28T14:59:37
template: link
link: https://fastapi.tiangolo.com/tutorial/header-params/#declare-header-parameters
tags:
  - python
  - fastapi
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://fastapi.tiangolo.com/tutorial/header-params/#declare-header-parameters]]

Getting request headers in fastapi has a pretty nice stetup, it allows you to get headers values as function arguments, 

I was able to use headers to detect if a request was made from htmx or not.

> If the request was made from htmx, then we want a html format, otherwise I'm probably hitting the api programatically from something like `curl` or `python`

``` python
@post_router.post("/post/")
async def post_post(
    request: Request,
    post: PostCreate,
    current_user: Annotated[User, Depends(try_get_current_active_user)],
    session: Session = Depends(get_session),
    is_hx_request: Annotated[str | None, Header()] = None,
) -> PostRead:
    "create a post"
    print('hx_request', hx_request)
    db_post = Post.from_orm(post)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    if is_hx_request:
        return templates.TemplateResponse("post_item.html", {"request": request, "config": config, "post": db_post})
    return db_post

```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
