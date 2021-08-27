---
templateKey: blog-post
tags: ['vim', ]
title: Notes for second vim-fundamentals course meetup
date: 2021-08-27T22:40:45
status: draft

---

newline
another


Mahesh Subrajmanium Venkatachalam - Plugins | Installing a Theme
Hunter Phillips - Quickfix | Offline Ordering with getqflist
Andrea Wackerle - Search & Replace | Macros

Matthew Fletcher - Registers | Advanced Motions Jump, Delete, & Select | Advanced Motions: Paste & Move
Nicholas Payne - My First Vim Plugin | What Makes a Good Plugin
Zev Averbach - Harpoon | Wrap up

## Plugin-manager

* get a plugin manager
* unless you are going full lua, most people use vim-plug by the great junegunn

https://github.com/junegunn/vim-plug

## Install pluggged

``` bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim     
```

``` vim
call plug#begin('~/.vim/plugged')

Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

call plug#end()
```

## Install Plugins

``` vim
:PlugInstall
:PlugClean
:PlugUpdate
```

## Installing a Theme

install using plug

``` vim
Plug 'ayu-theme/ayu-vim'
```

set the theme

``` vim
set termguicolors
let ayucolor="dark"
colorscheme ayu
```

## Quickfix

sending things to the quickfix list

``` vim
:grep SOCKET_OPEN **/*.(c\|h)
```

quickfix commands

``` vim
:copen
:cnext
:cdo s/vim/nvim/g
```


## Some remaps to consider

``` vim
nnoremap <C-k> :cnext<CR>
nnoremap <C-j> :cprev<CR>
nnoremap <C-E> :copen<CR>
```

## Offline Ordering with getqflist

## Search & Replace

Walk through example.

```  bash
curl https://raw.githubusercontent.com/ThePrimeagen/vim-fundamentals/master/course-website/lessons/exercise-3-search-and-replace.md > exercise.md && vim exercise.md
```

## Macros

* Macro Pressure

``` bash
curl https://raw.githubusercontent.com/ThePrimeagen/vim-fundamentals/master/course-website/lessons/exercise-4-macros.md > exercise.md && vim exercise.md
```
