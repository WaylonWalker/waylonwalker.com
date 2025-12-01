---
date: 2025-02-20 08:11:35
templateKey: til
title: pre-commit exclude
published: true
tags:
  - python

---


I run tailwind for my personal blog, whenever I update it, pre-commit goes in
and fixes end of file.  I'm sick of these things fighting each other, since it
is a generated app it is going to et ignored from pre-commit from now on.

``` yaml
exclude: ^static/app.*\.css$
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```
