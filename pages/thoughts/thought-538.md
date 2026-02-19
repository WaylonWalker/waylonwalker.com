---
title: '💭 poolers.postgresql.cnpg.io CRD metadata.annotations Too long ·...'
date: 2025-01-21T17:06:21
template: link
link: https://github.com/cloudnative-pg/charts/issues/325
tags:
  - k8s
  - argo
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/cloudnative-pg/charts/issues/325]]

I've never seen or needed to use a serversideapply in kubernetes before, but I ran into this same issue in my k3s homelab while installing cloudnative-pg.


You can do it with argo

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
spec:
syncPolicy:
syncOptions:
- ServerSideApply=true
```

and you can do it with kubectl

``` bash
kubectl apply --server-side --force-conflicts -f cnpg-1.25.0.yaml
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
