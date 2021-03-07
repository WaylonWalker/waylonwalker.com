---
templateKey: hot-tip
tags: 
  - bash
  - tip
title: Compare Directories In Bash
date: 2020-12-11T00:00:00
status: draft
description: ''
cover: "/static/compare-directories-in-bash.png"

---

Today I needed to check for articles that used the same slug from two directories, bash made it super simple.

``` bash
diff -rq src/pages/blog src/pages/notes
```
