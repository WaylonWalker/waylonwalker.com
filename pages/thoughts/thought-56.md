---
title: '💭 Podman - ArchWiki'
date: 2023-07-29T01:03:23
template: link
link: https://wiki.archlinux.org/title/Podman
tags:
  - linux
  - podman
  - thoughts
  - thought
  - link
published: true

---

![[https://wiki.archlinux.org/title/Podman]]

I kept running into limits in the number of subuid and subgid's I had on my system by default.  As always thank the arch wiki guide for having the most comprehensive yet consice guide to setup podman.

What I needed to do to fix the error.

``` bash
usermod --add-subuids 100000-165535 --add-subgids 100000-165535 username
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
