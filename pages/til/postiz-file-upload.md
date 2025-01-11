---
date: 2025-01-10 20:35:39
templateKey: til
title: postiz-file-upload
published: true
tags:
  - social
  - postiz
  - containers
  - compose
  - docker

---

Today I learned that the docs in postiz are a bit behind, (fantastic docs btw,
they are to the point, and cover almost all of what you need).  The docs state
that you need to include an R2 bucket to handle uploads.

This [issue](https://github.com/gitroomhq/postiz-app/issues/322) shows that
more work has been done, one of which is local storage.  The [compose
file](https://docs.postiz.com/installation/docker-compose) they use in the
quick start has the required env variables to set this up.

```yaml
      STORAGE_PROVIDER: "local"
      UPLOAD_DIRECTORY: "/uploads"
      NEXT_PUBLIC_UPLOAD_DIRECTORY: "/uploads"
```

looking into my running instance I can see my images there.

``` bash
⬢ [devtainer] ❯ podman exec postiz ls /uploads/2025/01/09
811747b3f703f5d9a7f10aff5103412ff0.jpeg
a221db10a76f0c414171ab417379b09ec.jpeg
```
