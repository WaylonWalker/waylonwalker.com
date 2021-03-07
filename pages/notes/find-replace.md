---
templateKey: blog-post
title: Find and Replace in the Terminal.
date: 2020-11-12T05:00:00.000+00:00
status: published
description: notes about find and replace techniques
tags: 
  - linux
  - bash

---

## grepr

```bash
grepr() {grep -iRl "$1" | xargs sed -i "s/$1/$2/g"}

```bash
grepr() {grep -iRl "$1" | xargs sed -i "s/$1/$2/g"}
```

## grepd

``` python
grepd() {grep -iRl "$1" | xargs sed -i "/^$1/d"}
```

## CocSearch


``` bash
:CocSearch status: 'false' -g *.md
```



