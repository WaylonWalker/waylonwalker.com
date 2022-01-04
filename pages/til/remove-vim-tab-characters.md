---
date: 2022-01-06 01:49:31.251199
templateKey: til
title: Remove Vim Tab Characters
tags:
  - vim
  - linux

---

I've been stuck many times looking at a vim buffer with little question
marks at the beginning of each line and trying to get rid of them.  for
so long I didn't know what they were so trying to get rid of them was
impossible.

![example of what the tab character renders as in my editor](https://images.waylonwalker.com/vim-tab-characters.png)

It turns out they are tabs, and you can get rid of the little leading
question marks with this substitution command.

``` vim
:%s/\t/    /g
```
