---
title: '💭 Daniel Nashed''s Blog'
date: 2023-10-21T01:49:41
template: link
link: https://blog.nashcom.de/nashcomblog.nsf/dx/k3s-podman-and-a-registry.htm
tags:
  - homelab
  - containers
  - thoughts
  - thought
  - link
published: true

---

![[https://blog.nashcom.de/nashcomblog.nsf/dx/k3s-podman-and-a-registry.htm]]

Running your own docker registry in one line


``` bash
podman run -d -p 5000:5000 --restart=always --name registry registry:latest
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
