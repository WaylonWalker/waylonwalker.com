---
dateCreated: 2025-01-31 20:43:29
date: 2025-02-12 12:51
templateKey: til
title: vim date
published: true
tags:
  - vim
  - nvim

---


When I want to put a date in a document like a blog post from vim I use !!date
from insert mode.  Note that entering `!!` from normal mode puts you in command
mode with `:.!` filled out.  This runs a shell command, i.e. `date` for this
example.

It outputs the following

Fri Jan 31 08:46:11 PM CST 2025

You can also pass in a date such as tommorrow by pasdding in the -d `date -d tomorrow`.

It outputs the following

Sat Feb  1 08:53:20 PM CST 2025

> codeium just taught me this one with autocomplete

``` vim
:put =strftime('%Y-%m-%d')
```

This outputs the following

2025-01-31

What I like about the `:put =strftime(` method is that you can add a format,
but that is a lot more for me to remember than `!!date`

## A few weeks later

I'm going through a bunch of blog posts and dont want my date formats to change
to the Wed Feb format so I broke down and made these keybindings.  I think I'm
still going to be using `.!date` a lot, but these keybindings will be nice for
editing blog post frontmatter.

``` lua
set("n", "<leader>dd", "<cmd>put =strftime('%Y-%m-%d')<cr>", { noremap = true, silent = true })
set("n", "<leader>dt", "<cmd>put =strftime('%Y-%m-%d %H:%M:%S')<cr>", { noremap = true, silent = true })
```

* <leader>dd 2025-02-12
* <leader>dt 2025-02-12 12:53:47
* :.!date    Wed Feb 12 12:53:47 PM CST 2025
