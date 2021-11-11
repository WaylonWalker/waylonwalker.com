---
templateKey: blog-post
tags: ['kedro', ]
title: nvim conf 2021 | IDE's are slow | Waylon Walker
date: 2021-10-29
status: published

---

https://youtu.be/E18m4KkJUnI

[//]: <> (## images)

[//]: <> (too many codes)
[//]: <> ( https://pbs.twimg.com/media/FAEmRjYUcAUk2eR?format=jpg&name=large )
[//]: <> ( https://twitter.com/_WaylonWalker/status/1438849269407047686/photo/1 )
[//]: <> ( https://twitter.com/_WaylonWalker/status/1438849269407047686/photo/1 )

---

## Slides 👇

## welcome

[//]: <> (Rather than saying vim is fast lets fix some things live.  While we are trying)
[//]: <> (to present on how fast vim is, popups will iterrupt with critical production)
[//]: <> (failures that need fixed straight away.)

[//]: <> (## topics)
[//]: <> (* lsp)
[//]: <> (* make vim yours)
[//]: <> (* I use tmux)
[//]: <> (* quickfix)


## Other possible titles

* Using Vim as a Team Lead
* I 💜 Tmux
* Why I stopped using @code
* Get there fast
* How I vim


## It's ok

Use a graphical IDE if it works for you.

## Trick it out

vim is so well integrated into the terminal, take advantage

## It wasn't working for me anymore

[//]: <> (seriously,)

## dozens of instances

As a team lead I bounce betweeen a dozen projects a per day

https://pbs.twimg.com/media/FAEmRjYUcAUk2eR?format=jpg&name=large 

[//]: <> (Trying to run more than one instance of an ide is hard, especially when)
[//]: <> (projects are so similar and all start looking the same.)

## Move With Intent

Running vim inside tmux lets me move swiftly between the exact project I need.

https://twitter.com/_WaylonWalker/status/1438849269407047686/photo/1
[//]: <> (__)

## Hub and Spoke

* direct link to specific projects
* fuzzy into all projects
* fuzzy into open projects


https://waylonwalker.com/tmux-nav-2021/#hub-and-spoke

[//]: <> (I'm sure there are other ways do do this, I bet you can get a vim plugin to do this)

## Other Things That Make this Possible

* tmux
* direnv

> vim adjacent things

[//]: <> (## Check messages)


[//]: <> (a short interruption where I am called back to work where I show flying swiftly)
[//]: <> (between projects with the perfect intent.)

## yes, vim is ugly, make it yours

@rook
``` vim
command! Q :q
```

@_waylonwalker
``` vim
nnoremap <leader>6 <c-^>
```


[//]: <> (__)

## lsp


``` vim
lua vim.lsp.buf.definition()
```

## treesitter


``` vim
Plug 'nvim-treesitter/nvim-treesitter-textobjects'
```

## telescope

fuzzy matching like a boss

fzf is ok too

## Check Messages

[//]: <> (Another interruption comes in, this time the change uses the lsp and some custom bindings)
[//]: <> (Data Pipeline is down.)
[//]: <> (* Use the lsp go to definition.)
[//]: <> (* Open data in visidata)
[//]: <> (* use jumplist to get back)
[//]: <> (* make the fix)
[//]: <> (* use fugitive to commit)
