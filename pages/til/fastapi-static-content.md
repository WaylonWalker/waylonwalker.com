---
date: 2023-10-04 08:32:58
templateKey: til
title: how to host static content with fastapi
published: true
tags:
  - python
---

I wanted to host some static files through fastapi. Typical use cases for this
might be some static web content like html/css/js. It could also be images or
some data that doesn't need dynamically rendered.

## From the Docs

The docs cover how to host static files, and give this solution that is built
into fastapi.

https://fastapi.tiangolo.com/tutorial/static-files/

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

## Authenticated Static Files

_Thanks to [#858](https://github.com/tiangolo/fastapi/issues/858)._

[OscartGiles](https://github.com/OscartGiles) posted this solution to add
authentication to static files. I tried this out on my
[thoughts](https://thoughts.waylonwalker.com) and it worked flawlessly.

```python
import typing
from pathlib import Path
import secrets

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials


PathLike = typing.Union[str, "os.PathLike[str]"]
app = FastAPI()
security = HTTPBasic()


async def verify_username(request: Request) -> HTTPBasicCredentials:

    credentials = await security(request)

    correct_username = secrets.compare_digest(credentials.username, "user")
    correct_password = secrets.compare_digest(credentials.password, "password")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


class AuthStaticFiles(StaticFiles):
    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

    async def __call__(self, scope, receive, send) -> None:

        assert scope["type"] == "http"

        request = Request(scope, receive)
        await verify_username(request)
        await super().__call__(scope, receive, send)


app.mount(
    "/static",
    AuthStaticFiles(directory=Path(__file__).parent / "static"),
    name="static",
)
```

If you want both then, all you have to do is mount `AuthStaticFiles` to a
different route. Now you can have private, or paid content behind
`/restricted`.

```python
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount(
    "/restricted",
    AuthStaticFiles(directory=Path(__file__).parent / "restricted"),
    name="restricted"
)
```
