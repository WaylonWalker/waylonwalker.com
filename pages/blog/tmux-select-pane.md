---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux']
title: tmux slect-pane
date: 2021-07-23T23:51:21
published: true

---

[https://youtu.be/CPZJZjN9YTY](https://youtu.be/CPZJZjN9YTY){.hoverlink}

These are my MOST often used keybindings that I use in tmux.  They allow me to
jump between splits with ease with a vim style layout.  I can hold mod and jump
between panes with a familiar arrow key.

``` bash
bind -n M-h select-pane -L
bind -n M-l select-pane -R
bind -n M-k select-pane -U
bind -n M-j select-pane -D
```

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post
