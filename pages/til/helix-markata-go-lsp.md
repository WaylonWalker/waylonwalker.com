---
date: 2026-07-28 22:21:13
templateKey: til
title: helix markata go lsp
published: true
tags:
  - markdown
  - markata

---

Helix has got to have one of the easiest configurations.  It is this easy to get
the markata-go lsp in helix.

``` bash
markata-go lsp setup --editor helix
# Helix languages.toml (usually ~/.config/helix/languages.toml)
[language-server.markata-go]
command = "markata-go"
args = ["lsp"]

[[language]]
name = "markdown"
language-servers = ["markata-go"]
```
