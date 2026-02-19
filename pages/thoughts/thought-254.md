---
title: '💭 How to Restart All Pods in a Kubernetes Namespace | Boot.dev'
date: 2024-04-25T21:59:56
template: link
link: https://blog.boot.dev/open-source/how-to-restart-all-pods-in-a-kubernetes-namespace/
tags:
  - k8s
  - kubernetes
  - thoughts
  - thought
  - link
published: true

---

![[https://blog.boot.dev/open-source/how-to-restart-all-pods-in-a-kubernetes-namespace/]]

As of kubernetes 1.15 there is an easy way to restart all pods in a deployment.

``` bash
kubectl -n {NAMESPACE} rollout restart deploy
```

Thanks Lane give him a follow [@wagslane](https://twitter.com/wagslane)

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
