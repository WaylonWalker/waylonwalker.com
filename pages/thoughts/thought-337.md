---
title: '💭 pacman/Tips and tricks - ArchWiki'
date: 2024-07-06T16:52:09
templateKey: link
link: https://wiki.archlinux.org/title/pacman/Tips_and_tricks
tags:
  - linux
  - arch
published: true

---

> The arch wiki is always full of good content, and pacman tips and tricks does not disappoint.  Today I discovered this command to remove orphaned dependencies on my system.

``` bash
pacman -Qdtq | pacman -Rns -
```

[Original thought](https://wiki.archlinux.org/title/pacman/Tips_and_tricks)
