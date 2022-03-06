---
date: 2022-03-06 16:22:49.829089
templateKey: til
title: Open Files with Nvim Remote
tags:
  - python
  - vim
  - tmux

---

I recently found a really great [plugin](https://github.com/mhinz/neovim-remote) by
[mhinz](https://github.com/mhinz) to open files in neovim from a
different tmux split, without touching neovim at all.

## Installation

[neovim-remote](https://github.com/mhinz/neovim-remote) is not a neovim
plugin at all, it's a python cli that you can install with pip.  Unlike
the repo suggests, I use pipx to install `nvr`.


``` bash
pipx install neovim-remote
```

## How I use it

I have this added to my `.envrc` that is in every one of my projects.
This will tie a neovim session to that directory, and all directories
under it.

``` bash
export NVIM_LISTEN_ADDRESS=/tmp/nvim-$(basename $PWD)
```

> In my workflow I open a tmux session for each project, so this
> essentially ties a neovim session to a tmux session.

### Open neovim

First open neovim, but with the `nvr` command.  This will open neovim,
and look pretty much the same as always.

``` bash
nvr
```

If you try to run `nvr` again in another shell nothing will happen as
its already runnin under that address, but if you give it a filename it
will open the file in the first instance of neovim that you opened.

``` bash
nvr readme.md
````

## Links

* [GitHub](https://github.com/mhinz/neovim-remote)
