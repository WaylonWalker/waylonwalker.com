---
date: 2021-12-25T20:24:48
templateKey: til
title: Finding hidden (dotfiles) using Telescope in neovim
tags:
  - vim

---

Finding hidden files using Telescope as you fuzzy file finder is not too
hard, its a single flag passed in.  Then it will use whichever file
finder it can find ['fd', 'fdfind', 'rg --files', 'find', or 'where'] in
that order.  These tools each have their own way of handling hidden
files, but telescope takes care of that so all you need to do is pass in
`hidden=true`.

I have this keymap set to help me list out all files including hidden
files using the pnumonic go edit hidden.  I use ge for quite a few
different things to take me directly to a specific file or picker.

``` python
nnoremap geh :Telescope find_files hidden=true<CR>
```


see the
[implementation](https://github.com/nvim-telescope/telescope.nvim/blob/82e3cc322ad87b262aef092cb7475e769740e83a/lua/telescope/builtin/files.lua#L167-L184)
telescope finds your files.
