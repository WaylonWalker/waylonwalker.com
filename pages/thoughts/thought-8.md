---
title: '💭 How to fix ZFS pool not importing at boot :: ./techtipsy — Her...'
date: 2023-07-28T14:59:37
templateKey: link
link: https://ounapuu.ee/posts/2021/02/01/how-to-fix-zfs-pool-not-importing-at-boot/
tags:
  - linux
  - zfs
  - systemd
published: true

---

> Hacky solution to get `zpool import tank` to work on boot right away.  This has been an issue that has plagued my system for months and no matter what dependencies I add in it never works, but adding a sleep as ExecStartPre did the trick.

[Original thought](https://ounapuu.ee/posts/2021/02/01/how-to-fix-zfs-pool-not-importing-at-boot/)
