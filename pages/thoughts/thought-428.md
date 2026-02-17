---
title: '💭 E576: Error while reading ShaDa file: there is an item at posi...'
date: 2024-11-16T16:04:27
templateKey: link
link: https://github.com/neovim/neovim/issues/6875
tags:
  - nvim
published: true

---

> I hit an interesting error after updating my nvim plugins today.  I'm sti not even quite sure what a ShaDa file is, but I found min in my nvim state directory, unlike this issue that mentions it being in share.

The Error.

> Error while reading ShaDa file:

The Fix

``` bash
mv ~/.local/state/nvim/shada/main.shada ~/.local/state/nvim/shada/main.shada.bak
```

[Original thought](https://github.com/neovim/neovim/issues/6875)
