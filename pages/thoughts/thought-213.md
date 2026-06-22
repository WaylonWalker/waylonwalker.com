---
title: 'My New Python Lsp Setup'
date: 2024-03-09T02:58:03
template: link
link: None
tags:
  - python
  - nvim
  - thought
published: true

---

![[None]]

I figured out the killer combination for python lsp servers, ruff and jedi!  ruff does all of the diagnostics and formatting, then jedi handles all the code objects like go to definition and go to reference.

``` lua
	local servers = {
		ruff_lsp = {},
		jedi_language_server = {},
}
```
