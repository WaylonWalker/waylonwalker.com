---
date: 2026-03-02 08:47:44
templateKey: til
title: gh do I have a pr
published: true
tags:
  - cli

---

In the age of agentss sometimes work gets done on so many different worktrees
and branches its hard to tell if there is already a PR or any of them or not,
the great `gh` cli has us covered.

``` bash
gh pr list --head fix/markata-go-connections-graph
```
