---
date: 2022-02-18 15:57:37.751541
templateKey: til
title: Git rebase to the beginning of time
tags:
  - git
  - cli

---

Git has a built in way to rebase all the way back to the beginning of
time.  There is no need to scroll through the log to find the first
hash, or find the total number of commits. Just use `--root`

```
git rebase --root
```
