---
title: '💭 How to fix ZFS pool not importing at boot :: ./techtipsy — Her...'
date: 2023-07-28T14:59:37
template: link
link: https://ounapuu.ee/posts/2021/02/01/how-to-fix-zfs-pool-not-importing-at-boot/
tags:
  - linux
  - zfs
  - systemd
  - thoughts
  - thought
  - link
published: true

---

![[https://ounapuu.ee/posts/2021/02/01/how-to-fix-zfs-pool-not-importing-at-boot/]]

Hacky solution to get `zpool import tank` to work on boot right away.  This has been an issue that has plagued my system for months and no matter what dependencies I add in it never works, but adding a sleep as ExecStartPre did the trick.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
