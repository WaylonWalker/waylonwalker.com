---
date: 2025-02-08 09:30:08
templateKey: til
title: bc
published: true
tags:
  - linux

---

<https://www.youtube.com/watch?v=03KsS09YS4E&t=610s>

Today I learned about the basic calculator, bc.  At the very end of this video
prime uses it to add numbers in vim.

## REPL

You can start a calculator repl at the command line, by running bc.

## Vim

Since bc supports standard unix pipes you can easily pipe data from vim into bc
and back out using `!!bc`.  All you need is a string of math on the line you
want to calculate, go to normal mode and run `!!bc` to get the answer.

Traditionally I will open my system calculator or ipython to do something like
this.

To keep the equation and the result in the same line you can send the equation
to stderr and the result to stdout using tee.

``` bash
:.!tee >(cat >&2) | bc
```
