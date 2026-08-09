---
title: 'How to Restart All Pods in a Kubernetes Namespace | Boot.dev'
date: 2024-04-26T02:59:56Z
template: link
link: https://blog.boot.dev/open-source/how-to-restart-all-pods-in-a-kubernetes-namespace/
tags:
  - k8s
  - kubernetes
  - thought
published: true

---

![[https://blog.boot.dev/open-source/how-to-restart-all-pods-in-a-kubernetes-namespace/]]

As of kubernetes 1.15 there is an easy way to restart all pods in a deployment.

``` bash
kubectl -n {NAMESPACE} rollout restart deploy
```

Thanks Lane give him a follow [@wagslane](https://twitter.com/wagslane)
