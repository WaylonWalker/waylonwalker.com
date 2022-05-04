---
date: 2022-05-04 14:31:05
templateKey: til
title: Review Pull Requests with git worktrees
tags:
  - git

---

Sometimes you get a PR on a project, but cannot review it without wrecking your
current working setup.  This might be because it needs to be compiled, or a new
set of requirements.  Git worktrees is a great way to chekout the remote branch
in a completely separate directory to avoid changing any files in your current
project.

``` bash
# pattern
# git worktree add -b <branch-name> <PATH> <remote>/<branch-name>
git worktree add -b fix-aws-service-cnsn /tmp/project origin/fix-aws-service-cnsn
```

This will create a new directory `/tmp/project` that you can review the branch
`fix-aws-service-cnsn` from the remote `origin`.  If you have setup different remotes locally you can check for the name of it with `git remote -v`
