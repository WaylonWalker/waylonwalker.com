---
date: 2024-08-05 12:22
templateKey: til
title: Vim-gq
published: true
tags:
  - vim
  - neovim
---


Vim has a handy feature to format text with `gq`.  You can use it in visual
mode, give it a motion, or if you give it `gqq` it will format the current line.
I use this quite often while writing in markdown, I do not use softwraps in vim,
so `gqq` quickly formats my current line into a paragraph.    Once I have done
this for a single line one time I typically switch to the motion for around
paragraph `gqap` to format the whole paragraph and not just the current line.

## before formatting

![vim-gq-20240805122634078.webp](https://dropper.waylonwalker.com/api/file/01c19159-c0b5-4920-b73c-774284b09940.webp)

## after formattting

![vim-gq-20240805122700026.webp](https://dropper.waylonwalker.com/api/file/e068e445-43e0-4e27-ac30-ac11e9cb9088.webp)
