---
date: 2022-03-04 19:08:49.539488
templateKey: til
title: Dedup your shell paths
tags:
  - linux
  - cli

---

If you have ever ran `which <command>` and see duplicate entries it's likely
that you have duplicate entries in your $PATH.  You can clean this up with a
one liner at the end of your bashrc or zshrc.

``` bash
eval "typeset -U path"
```
