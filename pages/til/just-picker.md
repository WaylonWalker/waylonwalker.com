---
date: 2024-05-08 20:48:23
templateKey: til
title: just picker
published: true
tags:
  - linux

---

[`just`](https://github.com/casey/just) has been by go to tool for saving
commands in a way that I can replay them and have team members replay them
without relying on the shell history of any given machine.  This is my go to
default step, it lets you pick a just command to run with a fuzzy picker.

``` bash
default:
  @just --list
```
