---
title: '💭 "Pacman is currently in use, please wait."'
date: 2025-09-16T01:26:33
templateKey: link
link: https://bbs.archlinux.org/viewtopic.php?id=67729
tags:
  - arch
  - linux
published: true

---

> I ran into this issue today, never have I ever before though. Omarchy looking a bit sus on me.  This was even after a fresh boot, no pacman process running. just realized I forgot to check yay which it has installed for me.   I had to force it in.

``` bash
sudo rm /var/lib/pacman/db.lck
```


[Original thought](https://bbs.archlinux.org/viewtopic.php?id=67729)
