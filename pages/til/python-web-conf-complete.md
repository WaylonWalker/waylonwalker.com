---
date: 2100-03-20 15:27:36.805026
templateKey: til
title: python web conf complete
tags:
  - python

---

I love the freedom of writing in markdown.  It allows me to write content from
the comfort of my editor with very little focus on page style.  It turns out
that markdown is also a fantastic tool for creating slides.

## Present from the terminal

I will most often just present right from the terminal using
[lookatme](https://lookatme.readthedocs.io/en/latest/index.html).  Presenting
from the terminal lets me see the results quick right from where I am editing.
It also allows me to pop into other terminal applications quickly.

## reveal.js

I sometimes also use reveal.js, but that's for another post.  It is handy that
it lives in the browser and is easier to share.

## New Slides

I leverage auto slides when I write my slides in markdown.  The largest
heading, usually an h2 for me, becomes the new slide marker.  Otherwise my
process is not much different, It just becomes a shorter writing style.

## Installation

lookatme is a python library that is available on pypi, you can install it with
the pip command.

```
python -m pip install lookatme
```

Since it's a command line application it works great with pipx.  This prevents
the need to manage virtual environments yourself or ending up with packages
clashing in your system python environment.

```
pipx install lookatme
```

## From my terminal

``` bash
lookatme {filepath}
```

I just run it with pipx.

``` bash
pipx run \
 --spec git+https://github.com/waylonwalker/lookatme \
 lookatme {filepath} \
 --live-reload \
 --style gruvbox-dark
```

> Note, I use a custom fork of lookatme.  It's schema validation did not like
> the date format of my blog posts, so I have a one line fix built into my
> fork that is pretty specific to me.

## From Neovim
_most often what I do_

From Neovim I use a plugin I created for sending out commands to tmux called
[telegraph](https://github.com/WaylonWalker/Telegraph.nvim).  This sends the
above command to a new session that I can bounce between quickly.

``` vim
nnoremap <leader><leader>s <cmd>lua require'telegraph'.telegraph({cmd='pipx run --spec git+https://github.com/waylonwalker/lookatme lookatme {filepath} --live-reload --style gruvbox-dark', how='tmux'})<CR>
```
