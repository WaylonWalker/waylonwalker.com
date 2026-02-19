---
title: '💭 containers/aardvark-dns: Authoritative dns server for A/AAAA c...'
date: 2023-07-29T01:05:22
template: link
link: https://github.com/containers/aardvark-dns
tags:
  - linux
  - arch
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/containers/aardvark-dns]]

I ran into some dns issues while running podman on arch, aparantly I had missed an optional dependency of aardvark-dns for container to container dns resolution.

``` bash
paru -S aardvark-dns
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
