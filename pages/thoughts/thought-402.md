---
title: '💭 configuring pylsp · helix-editor/helix · Discussion #6623'
date: 2024-10-08T02:23:03
templateKey: link
link: https://github.com/helix-editor/helix/discussions/6623
tags:
  - helix
published: true

---

> How to set your python formatter to black with helix.  The following snippet lays out how to set the helix editor to auto-format on save with the black formatter.

``` toml
[[language]]
name = "python"
language-servers = ["pylsp"]

[language-server.pylsp.config.pylsp]
plugins.pyls_mypy.enabled = true
plugins.pyls_mypy.live_mode = true
plugins.flake8.maxLineLength = 88
plugins.pycodestyle.maxLineLength = 88

[language.formatter]
command = "black"
args = ["--line-length", "88", "--quiet", "-"]
```

[Original thought](https://github.com/helix-editor/helix/discussions/6623)
