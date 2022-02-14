---
date: 2022-02-14 14:53:17.647087
templateKey: til
title: Vim remaps use cmd in place of :
status: draft
tags:
  - vim
  - linux
  - cli

---

Anyone just starting out their vim customization journey is bound to run into this error.

``` vim
E5520: <Cmd> mapping must end with <CR>
```

I'll admit, in hindsight it's very clear whta

``` vim
                                                          E5520
  <Cmd> commands must terminate, that is, they must be followed by <CR> in the
  {rhs} of the mapping definition.  Command-line mode is never entered.
```
