---
title: '💭 "Pacman is currently in use, please wait."'
date: 2025-09-16T01:26:33
template: link
link: https://bbs.archlinux.org/viewtopic.php?id=67729
tags:
  - arch
  - linux
  - thoughts
  - thought
  - link
published: true

---

![[https://bbs.archlinux.org/viewtopic.php?id=67729]]

I ran into this issue today, never have I ever before though. Omarchy looking a bit sus on me.  This was even after a fresh boot, no pacman process running. just realized I forgot to check yay which it has installed for me.   I had to force it in.

``` bash
sudo rm /var/lib/pacman/db.lck
```


!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
