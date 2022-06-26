---
date: 2022-06-28 12:31:10
templateKey: til
title: Two new shell aliases for git
status: false
tags:
  - git

---

Recently I added two new bash/zsh aliases to make my git experience just a tad better.


## The Aliases

``` bash
alias trackme='git branch --set-upstream-to=origin/$(git symbolic-ref --short HEAD)'
alias rebasemain='git pull origin main --rebase'
```
