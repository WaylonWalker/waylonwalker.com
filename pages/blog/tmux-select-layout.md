---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux']
title: tmux select-layout
date: 2021-07-21T23:51:21
published: true

---

https://youtu.be/F0mHnwTrNNc

When you get many splits going in tmux sometimes its time for a new layout.
There are four layout strategies that I use, main-vertical, main-horizontal,
even-vertical, even-horizontal. Almost always I am useing the main ones with
mod plus a or mod plus shift a keybindings.

``` bash
# Select Layouts
#―――――――――――――――――
bind -n M-a select-layout main-vertical
bind -n M-A select-layout main-horizontal
bind -n M-E select-layout even-vertical
bind -n M-V select-layout even-horizontal
```


https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post
