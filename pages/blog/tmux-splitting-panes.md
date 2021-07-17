---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux']
title: tmux splitting panes
date: 2021-07-17T23:51:21
status: published

---

https://youtu.be/kzgyiHap1nQ

splitting panes is a core feature of tmux.  It allows us to split the terminal
vertically or horizontally into new panes.

``` bash
bind -n M-s split-window -c '#{pane_current_path}'
bind -n M-v split-window -h -c '#{pane_current_path}'
bind -n M-X kill-pane
```

> 🗒️ note that  '#{pane_current_path}'will keep the split in the same directory
> as it's parent, without this it will default to your home directory.


https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post
