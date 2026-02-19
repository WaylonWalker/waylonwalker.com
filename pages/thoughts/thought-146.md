---
title: '💭 Translate a Docker Compose File to Kubernetes Resources | Kube...'
date: 2023-10-22T02:04:18
template: link
link: https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/
tags:
  - homelab
  - k3s
  - containers
  - thoughts
  - thought
  - link
published: true

---

![[https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/]]

`kompose` is a sick cli to convert docker-compose.yml to kubernetes manifest.

``` bash
# install

curl -L https://github.com/kubernetes/kompose/releases/download/v1.26.0/kompose-linux-amd64 -o kompose

kompose convert
kompose convert -o deployment.yaml
```


!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
