---
date: 2024-04-25 20:15:29
templateKey: til
title: showmount-e
published: true
tags:
  - linux

---

TIL how to display the list of nfs mounts on your network.

``` bash
showmount -e
```

You can even look for mounts of other machines on your network.

``` bash
showmount -e <hostname>
```
