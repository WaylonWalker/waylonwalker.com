---
title: '💭 Delete a Postgres Cluster · Fly Docs'
date: 2023-10-17T18:42:30
template: link
link: https://fly.io/docs/postgres/managing/deleting/
tags:
  - infra
  - fly
  - thoughts
  - thought
  - link
published: true

---

![[https://fly.io/docs/postgres/managing/deleting/]]

Deleting a fly postgres db cluster was not straightforward to me as the app name is not inferred from the toml like it is for the main app.


``` bash
fly apps destroy <pg-app-name>
fly pg db list -a <pg-app-name>
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
