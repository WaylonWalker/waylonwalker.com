---
date: 2025-12-12 07:53:57
templateKey: til
title: git name status
published: true
tags:
  - git

---

`--name-status` is a great way to see what files have changed in a git diff
alongside the status code.  I recently used this in a script to create a report
of new and modified files during a build.

``` bash
git diff --name-status
git diff --name-status origin/main
git diff --name-status --staged
git diff --name-status 'HEAD@{3 days ago}'
```
