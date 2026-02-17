---
title: '💭 argocd automated sync'
date: 2024-04-19T19:36:47
templateKey: link
link: none
tags:
  - k8s
  - kubernetes
published: true

---

> ```  yaml
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

[Original thought](none)
