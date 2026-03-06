---
title: '💭 argocd automated sync'
date: 2024-04-19T19:36:47
template: link
link: none
tags:
  - k8s
  - kubernetes
  - thoughts
  - thought
  - link
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

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
