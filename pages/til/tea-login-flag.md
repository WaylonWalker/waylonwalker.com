---
date: 2025-11-23 21:09:36
templateKey: til
title: tea login flag
published: true
tags:
  - cli
  - git
  - gitea
  - forgejo

---

The tea command for gitea (used by forgejo) has a flag for login.  With gitea
you can have multiple accounts logged in.  When you try to run a command such
as `repo create` it will prompt you which login to use, but I learned that you
can bake it in to all of them with `--login <login-name>`

``` bash
❯ tea repo create --name deleteme --description 'for example'
┃ NOTE: no gitea login detected, whether falling back to login 'git.waylonwalker.com'?
```

![image showing message NOTE: no gitea login detected, whether falling back to login 'git.waylonwalker.com'?](https://dropper.waylonwalker.com/file/11dc820d-1680-414c-9624-cd970b057a74.webp)

``` bash
tea repo create --name deleteme --description 'for example' --login git.wayl.one
```
