---
title: '💭 python - SQLAlchemy ORDER BY DESCENDING? - Stack Overflow'
date: 2023-07-29T22:30:25
templateKey: link
link: https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending
tags:
  - python
  - sql
  - sqlalchemy
published: true

---

> How to sort results from a sqlalchemy based orm.

``` python
.order_by(model.Entry.amount.desc())
```

I needed this to enable paging on my thoughts api.

``` python
@post_router.get("/posts/")
async def get_posts(
    *,
    request: Request,
    session: Session = Depends(get_session),
    hx_request: Annotated[str | None, Header()] = None,
    accept: Annotated[str | None, Header()] = None,
    current_user: Annotated[User, Depends(try_get_current_active_user)],
    page_size: int = 10,
    page: int = 1,
) -> Posts:
    "get all posts"
    statement = (
        select(Post)
        .where(Post.published)
        .order_by(Post.id.desc())
        .limit(page_size)
        .offset((page - 1) * page_size)
    )
    posts = session.exec(statement).all()
    posts = Posts(__root__=posts)

    if isinstance(current_user, RedirectResponse):
        is_logged_in = False
    else:
        is_logged_in = True

    if hx_request and page == 1 and len(posts.__root__) == 0:
        return HTMLResponse('<ul id="posts"><li>No posts</li></ul>')
    if hx_request and len(posts.__root__) == 0:
        return HTMLResponse("")
    if not hx_request and len(posts.__root__) == 0:
        return ["no posts"]
    if hx_request:
        return templates.TemplateResponse(
            "posts.html",
            {
                "request": request,
                "config": config,
                "posts": posts,
                "md": md,
                "is_logged_in": is_logged_in,
                "page": page,
            },
        )

    if accept.startswith("text/html"):
        return templates.TemplateResponse(
            "base.html",
            {
                "request": request,
                "config": config,
                "posts": posts,
                "md": md,
                "is_logged_in": is_logged_in,
                "page": page,
            },
        )

    return posts

```

[Original thought](https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending)
