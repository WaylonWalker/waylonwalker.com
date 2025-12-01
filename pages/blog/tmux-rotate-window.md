---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux']
title: tmux rotate-window
date: 2021-07-22T23:51:21
published: true

---

[https://youtu.be/06z5qf81ofo](https://youtu.be/06z5qf81ofo){.youtube-embed}

Rotate window is the main way that I navigated tmux before I learned
`select-pane`.  It allows you to change your focused pane, or rotate the
position of the panes easily.

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

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post
