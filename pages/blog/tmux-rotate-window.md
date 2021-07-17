---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux']
title: tmux rotate-window
date: 2021-07-22T23:51:21
status: published

---

When you get many splits going in tmux sometimes its time for a new layout.
There are four layout strategies that I use, main-vertical, main-horizontal,
even-vertical, even-horizontal. Almost always I am useing the main ones with
mod plus a or mod plus shift a keybindings.

Default keybindings

``` bash
bind-key        C-o rotate-window
bind-key          o select-pane -t :.+
```

My keybindings look just a bit different than the default ones, I do not like
needing to hit prefix for every command, especially for repeated commands.  I
set a similar keybinding to the default one that uses mod instead of prefix.

``` bash
bind -n M-o select-pane -t :.+
bind -n M-O rotate-window
```

https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post
