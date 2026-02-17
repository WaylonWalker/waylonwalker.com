---
title: '💭 Switching Configs in Neovim • Michael Uloth'
date: 2024-08-21T12:57:56
templateKey: link
link: https://michaeluloth.com/neovim-switch-configs/
tags:
  - nvim
published: true

---

> Switching between nvim configs can be really easy to do since they implemented the `NVIM_APPNAME` Environment Variable.

``` bash
NVIM_APPNAME=nvim-lazyvim nvim
```

Now config will be loaded from `~/.config/nvim-lazyvim`

Michael lays out some aliases in the full article.

``` bash
alias v='nvim' # default Neovim config
alias vz='NVIM_APPNAME=nvim-lazyvim nvim' # LazyVim
alias vc='NVIM_APPNAME=nvim-nvchad nvim' # NvChad
alias vk='NVIM_APPNAME=nvim-kickstart nvim' # Kickstart
alias va='NVIM_APPNAME=nvim-astrovim nvim' # AstroVim
alias vl='NVIM_APPNAME=nvim-lunarvim nvim' # LunarVim
````


[Original thought](https://michaeluloth.com/neovim-switch-configs/)
