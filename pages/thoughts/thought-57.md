---
title: '💭 containers/aardvark-dns: Authoritative dns server for A/AAAA c...'
date: 2023-07-29T01:05:22
templateKey: link
link: https://github.com/containers/aardvark-dns
tags:
  - linux
  - arch
published: true

---

> I ran into some dns issues while running podman on arch, aparantly I had missed an optional dependency of aardvark-dns for container to container dns resolution.

``` bash
paru -S aardvark-dns
```

[Original thought](https://github.com/containers/aardvark-dns)
