---
title: '💭 Filter Data - WHERE - SQLModel'
date: 2023-07-28T14:59:37
templateKey: link
link: https://sqlmodel.tiangolo.com/tutorial/where/#filter-rows-using-where-with-sqlmodel
tags:
  - python
  - fastapi
  - sqlmodel
published: true

---

> When fetching pydantic models from the database with sqlmodel, and you cannot select your item by id, you probably need to use a where clause.  This is the sqlmodel way of doing it.

> Here is a snippet of how I am using sqlmodel select and where to find a post by link in my thoughts database.

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

[Original thought](https://sqlmodel.tiangolo.com/tutorial/where/#filter-rows-using-where-with-sqlmodel)
