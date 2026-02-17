---
title: '💭 Bug #2006590 “gdm3 crashes with SIGTRAP on startup” : Bugs : g...'
date: 2024-05-02T00:54:02
templateKey: link
link: https://bugs.launchpad.net/ubuntu/+source/gdm3/+bug/2006590
tags:
  - linux
  - ubuntu
published: true

---

> This Thread saved my son's ubuntu 24.04 install.
His was failing to start with the following error.

``` bash
Gdm: GdmSession: no session desktop files installed, aborting...
```

https://twitter.com/_WaylonWalker/status/1785825677079441482


``` bash
sudo apt install --reinstall ubuntu-session
```

[Original thought](https://bugs.launchpad.net/ubuntu/+source/gdm3/+bug/2006590)
