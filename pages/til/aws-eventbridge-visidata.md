---
date: 2022-02-15 03:04:26.450467
templateKey: til
title: View AWS event bridge rules with visidata
tags:
  - python
  - cli
  - bash

---

Reading eventbridge rules from the command line can be a total drag, pipe it
into visidata to make it a breeze.

I just love when I start thinking through how to parse a bunch of json at the
command line, maybe building out my own custom cli, then the solution is as
simple as piping it into visidata.  Which is a fantastic tui application that
had a ton of vim-like keybindings and data features.


``` python
alias awsevents = aws events list-rules | visidata -f json
```
