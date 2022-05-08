---
date: 2022-05-09 21:24:12.550521
templateKey: til
title: List all git commits with GitPython
tags:
  - python

---

``` python
from git import Repo

repo = Repo('.')
commits = repo.iter_commits()
```
