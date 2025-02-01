---
date: 2025-01-31 20:43:29
templateKey: til
title: vim date
published: true
tags:
  - vim
  - nvim

---


When I want to put a date in a document like a blog post from vim I use !!date
from insert mode.  Note that entering `!!` from normal mode puts you in command
mode with `:.!` filled out.  This runs a shell command, i.e. `date` for this
example.

It outputs the following

Fri Jan 31 08:46:11 PM CST 2025

You can also pass in a date such as tommorrow by pasdding in the -d `date -d tomorrow`.

It outputs the following

Sat Feb  1 08:53:20 PM CST 2025

> codeium just taught me this one with autocomplete

``` vim
:put =strftime('%Y-%m-%d')
```

This outputs the following

2025-01-31
