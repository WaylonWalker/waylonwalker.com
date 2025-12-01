---
date: 2025-08-29 08:32:44
templateKey: til
title: vim noa
published: true
tags:
  - vim

---

Vim `:noa` is a command that runs what you call without autocommands on.  This
is typically used when you have some `BufWritePre` commands for formatting,
most auto formatters are implemented this way in vim.  It can be super useful
if you have something like a yaml/json file that you have crafted perfectly how
you want it, maybe it has some source code for a small script or sql embeded
and your formatter wants to turn it into one line.  You could get a better
formatter, but for these one off cases that aren't a big bother to me I run
`:noa w`.

``` vim
:noa w
```
