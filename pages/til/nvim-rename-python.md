---
date: 2022-01-16 15:27:22.251161
templateKey: til
title: Rename Python Variables with nvim
tags:
  - python
  - vim
  - vim

---

I don't use refactoring tools as much as I probably should.  mostly
because I work with small functions with unique names, but I recently
had a case where a variable name `m` was everywhere and I wanted it
named better.  This was not possible with find and replace, because
there were other `m`'s in this region.


I first tried the nvim lsp rename, and it failed, Then I pip installed
rope, a refactoring tool for python, and it just worked!

```bash
pip install rope
```

Once you have rope installed you can call rename on the variable.

```vim
:lua vim.lsp.buf.rename()
```
