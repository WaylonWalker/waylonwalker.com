---
date: 2025-02-11 13:55:04
templateKey: til
title: aptitude why
published: true
tags:
  - linux

---

Today I ran into an interesting question, why am I being asked to configure
tzdata while installing npm.  Turns out that the `aptitude` cli has a why
command that very handily nails down why you have something installed on a
debian based system.

## Install aptitude

``` bash
apt install aptitude
```

## Why tzdata

Now we can query why we need tzdata and see the full chain with the root
package being `npm`.

``` bash
root@47685221fb82:/# aptitude why tzdata
i   npm        Depends  node-gyp
i A node-gyp   Depends  gyp (>= 0.1+20200513gitcaa6002)
i A gyp        Depends  python3:any
i A python3    Provides python3:any
i A python3    Depends  python3.12 (>= 3.12.3-0~)
i A python3.12 Depends  tzdata
```
