---
templateKey: blog-post
tags: ['python',]
title: Develop Python Faster with automatic imports with pyflyby
date: 2021-12-04T11:34:47
status: Draft

---

This is not a flaky works half the time kind of plugin, its a seriously smooth
editiing experience.  I've just started using pyflyby and it is solid so far.
I have automatic imports on every save of a python file in neovim, and
automatic imports on every command in ipython.

## configuration setup with stow



```
cd ~/dotfiles
mkdir ipython
touch ipython/.pyflyby
stow ipython
```

## How to Configure pyflyby

## ipython setup
_Automatically import python libraries in ipython with pyflyby_

## ipython setup next level
_automatically import modules in python **without %load_ext**_

``` python
from IPython import get_ipython
import subprocess


ipython = get_ipython()

try:
    ipython.magic("load_ext pyflyby")
except ModuleNotFoundError:
    print("installing pyflyby")
    subprocess.Popen(
        ["pip", "install", "pyflyby"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).wait()
    ipython.magic("load_ext pyflyby")
```

## nvim pyflyby setup
_automatically importing python modules in vim, neovim, nvim_

``` vim
function! s:PyPreSave()
    Black
endfunction

function! s:PyPostSave()
    execute "silent !tidy-imports --black --quiet --replace-star-imports --action REPLACE " . bufname("%")
    execute "e"
endfunction

:command! PyPreSave :call s:PyPreSave()
:command! PyPostSave :call s:PyPostSave()

augroup waylonwalker
    autocmd!
    autocmd bufwritepre *.py execute 'PyPreSave'
    autocmd bufwritepost *.py execute 'PyPostSave'
    autocmd bufwritepost .tmux.conf execute ':!tmux source-file %'
    autocmd bufwritepost .tmux.local.conf execute ':!tmux source-file %'
    autocmd bufwritepost *.vim execute ':source %'
augroup end
```
