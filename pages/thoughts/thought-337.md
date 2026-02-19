---
title: '💭 pacman/Tips and tricks - ArchWiki'
date: 2024-07-06T16:52:09
template: link
link: https://wiki.archlinux.org/title/pacman/Tips_and_tricks
tags:
  - linux
  - arch
  - thoughts
  - thought
  - link
published: true

---

![[https://wiki.archlinux.org/title/pacman/Tips_and_tricks]]

The arch wiki is always full of good content, and pacman tips and tricks does not disappoint.  Today I discovered this command to remove orphaned dependencies on my system.

``` bash
pacman -Qdtq | pacman -Rns -
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
