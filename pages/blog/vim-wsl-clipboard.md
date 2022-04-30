---
templateKey: blog-post
tags: ['vim', 'bash']
title: Vim Wsl Clipboard
date: 2021-04-17T00:00:00
status: published

---

I've long used neovim from within windows wsl, and for far too long, I went
without a proper way to get text out of it and into windows.


## wsl has access to cmd applications

wsl can access clip.exe.  You can do some cool things with it, such as
cat a file into the clipboard, sending output from a command to the clipboard,
or set an autocmd group in vim to send yank to the windows clipboard.

## using clip.exe

Let's say you want to send a teammate the tail of a log file over chat. You can
tail the file into clip.exe.

``` bash
tail -n 1 info.log | clip.exe
```

> pipe streams of text into clip.exe

## make it a bit more natural

I recently made mine feel a bit more natural by aliasing it to clip.

``` bash
alias clip=clip.exe
```

> pop this in your ~/.bashrc or ~/.zshrc

## yanking to windows clipboard from vim

I use neovim as my daily text editor and its a pain to share code with a
teammate over chat, stack overflow, into a gist, or whatever you need.  The
following snippet has been quite useful and flawless for me.

``` vim
if system('uname -r') =~ "Microsoft"
    augroup Yank
        autocmd!
        autocmd TextYankPost * :call system('/mnt/c/windows/system32/clip.exe ',@")
        augroup END
endif
```

> add this to your ~/.vimrc or your ~/.config/nvim/init.vim

## Wsl2

Based on some
[feedback](https://github.com/WaylonWalker/waylonwalker.com/issues/4)
from [l-sannin](https://github.com/l-sannin) the 'uname -r' command now
returns `uname -r command returns '5.10.16.3-microsoft-standard-WSL2'`
So you will need an all lowercase microsoft.

``` vim
if system('uname -r') =~ "microsoft"
  augroup Yank
  autocmd!
  autocmd TextYankPost * :call system('/mnt/c/windows/system32/clip.exe ',@")
  augroup END
endif
```
