---
title: '💭 Formatting on save · jose-elias-alvarez/null-ls.nvim Wiki'
date: 2023-08-06T01:19:23
templateKey: link
link: https://github.com/jose-elias-alvarez/null-ls.nvim/wiki/Formatting-on-save#code
tags:
  - vim
  - nvim
published: true

---

> neovim stopped formatting on save for me awhile ago and I have just been dealing with it.  looks like there may have been an api change, idk.


I had to make this update.4

``` diff
- vim.lsp.buf.format()
+ vim.lsp.buf.format({async=false})
``` 

[Original thought](https://github.com/jose-elias-alvarez/null-ls.nvim/wiki/Formatting-on-save#code)
