---
title: '💭 Delete a Postgres Cluster · Fly Docs'
date: 2023-10-17T18:42:30
templateKey: link
link: https://fly.io/docs/postgres/managing/deleting/
tags:
  - infra
  - fly
published: true

---

> Deleting a fly postgres db cluster was not straightforward to me as the app name is not inferred from the toml like it is for the main app.


``` bash
fly apps destroy <pg-app-name>
fly pg db list -a <pg-app-name>
```

[Original thought](https://fly.io/docs/postgres/managing/deleting/)
