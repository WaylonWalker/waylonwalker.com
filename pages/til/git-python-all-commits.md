---
date: 2022-05-09 21:24:12.550521
templateKey: til
title: List all git commits with GitPython
tags:
  - python
  - git

---

I am getting ready to do some timeseries analysis on a git repo with python, my
first step is to figure out a way to list all of the git commits so that I can
analyze each one however I want.  The GitPython library made this almost
trivial once I realized how.

``` python
from git import Repo

repo = Repo('.')
commits = repo.iter_commits()
```

This returns a generator, if you are iterating over them this is likely what
you want.

``` python
commits
# <generator object Commit._iter_from_process_or_stream at 0x7f3307584510>
```

The generator will return `git.Commit` objects with lots of information about
each commit such as `hexsha`, `author`, `commited_datetime`, `gpgsig`, and
`message`.

``` python
next(commits)
# <git.Commit "d125317892d0fab10a36638a2d23356ba25c5621">
```
