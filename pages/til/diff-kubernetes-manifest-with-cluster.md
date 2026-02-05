---
date: 2026-02-05 09:37:39
templateKey: til
title: diff kubernetes manifest with cluster
published: true
tags:
  - kubernetes

---

Like a dufus this morning I did a hard reset on a git repo for getting I was
working on a manifest for.  You see I generally use argo, but occasionally I
have no idea what I am doing or want yet and I start raw doggin it, fully aware
that I'm going to just nuke this namespace before getting it into a proper
argocd.

I was overjoyed when I found out that you can diff your manifests with live
production using the `kubectl diff` command.  It uses standard diff so you can
bring all your fancy diff viewers you like.

``` bash
# regular manifest
kubectl diff -f k8s/shots -n shot
# kustomize
kubectl diff -k k8s -n go-waylonwalker-com
# using a fancy diff viewer
kubectl diff -f k8s/shots -n shot | delta
# using an even fancier diff viewer
# pinkies out for this one
kubectl diff -f k8s/shots -n shot | delta --diff-so-fancy
```

Now I can get those changes back that I thought I lost, and apply updates with
confidence knowing what is about to change.
