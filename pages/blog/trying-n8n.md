---
date: 2024-09-03 11:24
templateKey: til
title: Trying-n8n
published: true
tags:
---

Today I gave n8n a try using podman, their docs gave me docker commands, but it
ran fine on my machine using podman.

```
podman volume create n8n_data
podman run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```
