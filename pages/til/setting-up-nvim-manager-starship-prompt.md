---
date: 2025-01-21 16:03:46
templateKey: til
title: setting up nvim-manager starship prompt
published: true
tags:
  - nvim
  - nvim-manager
  - starship

---

I built out a tool for myself to manage my nvim configuration, and I wanted to
quickly see which one I am running in my starship prompt. Here's the config I
ended up with.  It warns if the `NVIM_APPNAME` environment variable is not set, and
it shows which nvim I am using if it is set.

``` toml
[custom.nvim-manager-system]
when = '[[ ! -n "${NVIM_APPNAME}" ]]'
style = "bold yellow"
symbol = '[ ](fg:#15AABF)'
format = '$symbol[USING SYSTEM NVIM]($style)'

[env_var.NVIM_APPNAME]
style = "green"
symbol = '[ ](fg:#15AABF)'
format = '[$symbol${env_value}]($style)'
variable = "NVIM_APPNAME"
```
