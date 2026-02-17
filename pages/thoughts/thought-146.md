---
title: '💭 Translate a Docker Compose File to Kubernetes Resources | Kube...'
date: 2023-10-22T02:04:18
templateKey: link
link: https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/
tags:
  - homelab
  - k3s
  - containers
published: true

---

> `kompose` is a sick cli to convert docker-compose.yml to kubernetes manifest.

``` bash
# install

curl -L https://github.com/kubernetes/kompose/releases/download/v1.26.0/kompose-linux-amd64 -o kompose

kompose convert
kompose convert -o deployment.yaml
```


[Original thought](https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/)
