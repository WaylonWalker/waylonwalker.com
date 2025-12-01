---
date: 2025-10-22 09:11:31
templateKey: til
title: starlette head request
published: true
tags:
  - python
  - webdev

---

Starlette has a head request that works right along side your get requests.
This morning I fiddled around with custom routes for `GET` and `HEAD`, but had
to manually set some things about the file, and was still missing `e-tag` in
the end.  Turns out as a developer you can [[ just ]] add a `head` route to
your `get` routes and starlette will strip the content for you, while
preserving all of those good headers that fastapi `FileResponse` created
automatically for you.

``` python
from fastapi import APIRouter
from fastapi.response import FileResponse
from fastapi import Request
from pathlib import Path

router = APIRouter()

@router.get("/file/{filename}")
@router.head("/file/{filename}")
async def get_file(filename: str, request: Request,):
    headers = {
      "Cache-Control": "no-cache, no-store, must-revalidate",
    }
    from pathlib import Path
    filename = Path(f"data/{filename}")
    if not filename.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(filename, headers=headers)
```

Here is an example of the response with curl.

``` bash
❯ curl -I -L "http://localhost:8100/api/file/e5523925-1565-454c-bab3-c70c4deabc83.webp?width=250"
HTTP/1.1 200 OK
date: Wed, 22 Oct 2025 14:16:03 GMT
server: uvicorn
cache-control: no-cache, no-store, must-revalidate
content-type: image/webp
content-length: 17206
last-modified: Tue, 23 Sep 2025 14:03:20 GMT
etag: f891660c1543feb1af7564f08abdd511

❯ curl -I -L "http://localhost:8100/api/file/unknown-file.webp?width=250"
HTTP/1.1 404 Not Found
date: Wed, 22 Oct 2025 14:16:11 GMT
server: uvicorn
content-length: 27
content-type: application/json
```
