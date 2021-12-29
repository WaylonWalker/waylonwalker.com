---
date: 2021-12-29T20:24:48
templateKey: til
title: List all the files containing a phrase
tags:
  - vim
  - linux
  - bash

---

``` bash
ag nvim --md -l
```

``` bash
rg --files-with-matches you -g ".md"
```
