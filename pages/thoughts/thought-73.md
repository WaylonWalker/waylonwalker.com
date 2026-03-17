---
title: '💭 Formatting on save · jose-elias-alvarez/null-ls.nvim Wiki'
date: 2023-08-06T01:19:23
template: link
link: https://github.com/jose-elias-alvarez/null-ls.nvim/wiki/Formatting-on-save#code
tags:
  - vim
  - nvim
  - thought
published: true

---

![[https://github.com/jose-elias-alvarez/null-ls.nvim/wiki/Formatting-on-save#code]]

neovim stopped formatting on save for me awhile ago and I have just been dealing with it.  looks like there may have been an api change, idk.


I had to make this update.4

``` diff
- vim.lsp.buf.format()
+ vim.lsp.buf.format({async=false})
``` 

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
