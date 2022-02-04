---
date: 2022-02-04 14:23:57.147712
templateKey: til
title: Neovim Config for Git
tags:
  - vim
  - linux
  - bash

---

Creating a minimal config specifically for git commits has made running
`git commit` much more pleasant.  It starts up Much faster, and has all
of the parts of my config that I use while making a git commit.  The one
thing that I often use is autocomplete, for things coming from elsewhere
in the tmux session.  For this `cmpe-tmux` specifically is super
helpful.

The other thing that is engrained into my muscle memory is `jj`
for escape.  For that I went agead and added my `settings` and `keymap`
with no noticable performance hit.

Here is the config that has taken


~/.config/nvim/init-git.vim

``` vim
source ~/.config/nvim/settings.vim
source ~/.config/nvim/keymap.vim
source ~/.config/nvim/git-plugins.vim
lua require'waylonwalker.cmp'
```

~/.config/nvim/git-plugins.vim

``` vim
call plug#begin('~/.local/share/nvim/plugged')

" cmp
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-calc'
Plug 'andersevenrud/compe-tmux', { 'branch': 'cmp' }


call plug#end()
```

~/.gitconfig

``` toml
[core]
    editor = nvim -u ~/.config/nvim/init-git.vim
```
