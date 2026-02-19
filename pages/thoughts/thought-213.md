---
title: '💭 My New Python Lsp Setup'
date: 2024-03-09T02:58:03
template: link
link: None
tags:
  - python
  - nvim
  - thoughts
  - thought
  - link
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

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
