---
title: 'argocd automated sync'
date: 2024-04-20T00:36:47Z
template: link
link: none
tags:
  - k8s
  - kubernetes
  - thought
published: true

---

![[none]]

```  yaml
---

apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: kanboard
  namespace: argocd
spec:
  project: default
  destination:
    namespace: kanboard
    server: 'https://kubernetes.default.svc'
  source:
    path: kanboard
    repoURL: 'https://github.com/waylonwalker/homelab-argo'
    targetRevision: HEAD
  syncPolicy:
    automated:
      prune: true
```
