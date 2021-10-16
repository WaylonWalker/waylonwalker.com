---
templateKey: blog-post
tags: ['kedro', 'python']
title: IDE's are slow
date: 2021-08-18
status: draft

---

## meta

### topics
* lsp
* make vim yours
* I use tmux
* quickfix

### idea

Rather than saying vim is fast lets fix some things live.  While we are trying
to present on how fast vim is, popups will iterrupt with critical production
failures that need fixed straight away.

### interruptions

Data Pipeline is down. 

* Use the lsp go to definition.
* Open data in visidata
* use jumplist to get back
* make the fix
* use fugitive to commit

### todo

* design obs popup

## The slides

## Other possible titles

* Using Vim as a Team Lead
* I 💜 Tmux

## It's ok

Use a graphical IDE if it works for you.


## dozens of instances

As a team lead I bounce betweeen a dozen projects a per day

## Move With Intent

https://twitter.com/_WaylonWalker/status/1438849269407047686/photo/1

## Other Things That Make this Possible

* tmux
* direnv

> vim adjacent things

## kedro lsp 

!! interruption


## yes, vim is ugly, make it yours

@rook
command! Q :q 

## lsp


``` vim
lua vim.lsp.buf.definition()

```

## treesitter


``` vim
Plug 'nvim-treesitter/nvim-treesitter-textobjects'
```

## telescope

Do some work

* Lint
* PR review





