---
date: 2021-12-22T19:34:18
templateKey: til
title: fugitive verbose commit
tags:
  - git
  - vim

---

Fugitive comes with a pretty sick way to commit files and see the diff at the
same time with verbose commit.  Opening the fugitive menu with `:G` brings up
your git status, you can stage files with `s`, unstage them with `u`, toggle
them with `-`, and toggle their diff with `>`.  Once you have staged your files
for commit, you can commit with `cc`, but today I found that you can commit
verbose with `cvc`.  This brings up not only a commit widow with your git
status shown, but the diff that you are about to commit.

![fugitive verbose commit example](https://images.waylonwalker.com/fugitive-verbose-commit.png)

> example of a verbose commit in fugitive
