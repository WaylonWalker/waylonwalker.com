---
date: 2025-02-13 08:41:39
templateKey: blog-post
title: fixed long standing nvim startup error
tags:
  - vim
  - nvim
published: True

---

Here's the diff, this is it.

``` diff
  local M = {}


  M.setup = require("waylonwalker.setup")
  M.settings = require("waylonwalker.settings")
+ M.lazy = require("waylonwalker.lazy")
  M.options = require("waylonwalker.options")
  M.globals = require("waylonwalker.globals")
  M.keymap = require("waylonwalker.keymap")
- M.lazy = require("waylonwalker.lazy")
  M.autocmds = require("waylonwalker.autocmds")
  M.util = require("waylonwalker.util")
  M.plugins = require("waylonwalker.plugins")
  M.snippets = require("waylonwalker.snippets")

  return M

```

## The error

On first install of my dotfiles I'm presenting with this flashbang of an error
filling the screen with red background.  Its kinda hard to read, I'm not deep
into lua and reading their tracebacks.  It pops up in this pager that if I
scroll too far it quits and the error is gone before I know what it is or how
it got there.

![image](https://dropper.wayl.one/api/file/20eafd2f-fbcd-4f93-8bd9-541edf42fba4.webp)

For the longest time it just felt like it randomly showed up without much warning.

## I sent ai at the issue

I tried some chatgpt and windsurf, both gave me overconfident answers that all
did nothing.  They just sent me in loops for way too long.

## I fixed it

What did it take??

Just sitting down and thinking about what the problem was and setting up a good
test workflow.  Yesterday I worked out [[testing-nvim-installs]] and I was
immediately able to replicate the error over and over.  Unlike before where it
felt random, I now have a good problem statement that I can replicate.

* clean install
* start nvim
* Lazy pops up
* FLASHBANG!! Error that treesitter is not installed

What was confusing for so long was that treesitter was the first thing in lazy,
and it appeared that lazy was running before the error.

## The fix

Once I really thought about <package> not installed, it clicked.  It must be
the order of operations. I popped open my `init.lua` and there it was, lazy
running after things that use treesitter.  A little ++d+d+k+k+k+k+k+p++ and it
was fixed. running `just testnvim` the next time there was no flashbang!

``` diff
  local M = {}


  M.setup = require("waylonwalker.setup")
  M.settings = require("waylonwalker.settings")
+ M.lazy = require("waylonwalker.lazy")
  M.options = require("waylonwalker.options")
  M.globals = require("waylonwalker.globals")
  M.keymap = require("waylonwalker.keymap")
- M.lazy = require("waylonwalker.lazy")
  M.autocmds = require("waylonwalker.autocmds")
  M.util = require("waylonwalker.util")
  M.plugins = require("waylonwalker.plugins")
  M.snippets = require("waylonwalker.snippets")

  return M

```
