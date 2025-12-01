---
date: 2024-04-21 07:53:54
templateKey: til
title: Am I vulnerable to the xz backdoor?
published: true
tags:
  - linux

---

The main system that I am concerned about is my arch BTW machine. I found a
great [article](https://archlinux.org/news/the-xz-package-has-been-backdoored/)
from the official archlinux site covering it.

For my machine I am concerned with this line.

> The xz packages prior to version 5.6.1-2 (specifically 5.6.0-1 and 5.6.1-1)
> contain this backdoor.

I checked my xz package with paru, and I am good.

``` bash
paru -Qii zx
```
