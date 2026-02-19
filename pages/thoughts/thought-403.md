---
title: '💭 help on setting up ruff formatter + ruff + pyright please : r/...'
date: 2024-10-08T02:25:37
template: link
link: https://www.reddit.com/r/HelixEditor/comments/17gglgm/help_on_setting_up_ruff_formatter_ruff_pyright/
tags:
  - helix
  - thoughts
  - thought
  - link
published: true

---

![[https://www.reddit.com/r/HelixEditor/comments/17gglgm/help_on_setting_up_ruff_formatter_ruff_pyright/]]

This post shows how to set up multiple LSP's in helix, the example uses pyright and ruff-lsp for python.

Add this to your `~/.config/helix/languages.toml`
a
``` toml
[[language]]
name = "python"
auto-format = true
language-servers = [
    {name = "pyright"},
    {name = "ruff-lsp"},
]

[language-server.pyright]
command = "pyright-langserver"
args = ["--stdio"]
config = {}

[language-server.ruff-lsp]
command = "ruff-lsp"
args = []
config = {}
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
