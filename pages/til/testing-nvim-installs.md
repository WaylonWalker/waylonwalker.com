---
date: 2025-02-12 21:02:03
templateKey: til
title: testing nvim installs
published: true
tags:
  - just
  - nvim

---

Testing fresh nvim installs can be a pain, and hard to di without borking your
known good install.  I've been using `NVIM_APPNAME` to run a test nvim in a
sandbox that wont bork my main install.  This usually runs for me in under a
minute, can be down under 15s if I remove some of the TreeSitter installs at
the end.  This beats a full docker build of my full devtainer to test out nvim
packaging woes.

``` bash
rm ~/.cache/wwtest -rf
rm ~/.local/share/wwtest -rf
rm ~/.config/wwtest -rf
cp -r nvim/.config/nvim/ ~/.config/wwtest
NVIM_APPNAME=wwtest nvim --headless "+Lazy sync" +qa
NVIM_APPNAME=wwtest nvim --headless "+TSUpdateSync" "+sleep 5000m" +qa
NVIM_APPNAME=wwtest nvim --headless "+MasonUpdate" +qa
NVIM_APPNAME=wwtest nvim --headless "+TSInstallSync! c cpp go lua python rust tsx javascript typescript vimdoc vim bash yaml toml vue just" +qa
NVIM_APPNAME=wwtest nvim --headless "+MasonInstall lua-language-server rustywind ruff ruff-lsp html-lsp typescript-language-server beautysh fixjson isort markdownlint stylua yamlfmt python-lsp-server" +qa
NVIM_APPNAME=wwtest nvim
```

I've started to use this as a `just` recipe to run before deploying a new
version of my dotfiles. So far its pairing nicely with [[nvim-manager]]
