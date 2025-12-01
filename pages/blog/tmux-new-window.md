---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux', 'tmux']
title: tmux new-window
date: 2021-07-24T23:51:21
published: true

---

[https://youtu.be/YRPZBv-iYyE](https://youtu.be/YRPZBv-iYyE){.youtube-embed}

New window as it sounds makes new windows in tmux.  Windows are kind of like
tabs.  They are another screen within your sessions that you can name and make
new panes in.

Default key bindings for creating and navigating windows in tmux.

``` bash
bind-key          c new-window
bind-key          p previous-window
bind-key          n next-window
```

As always I have rebound these keys because I generally prefer a single
keystroke over the prefix plus keybinding approach that tmux gives by default.

``` bash
#――windows――――――――――――――――――――――――――――――――――――――
bind -n M-c new-window -c '#{pane_current_path}'
bind -n M-p previous-window
bind -n M-n next-window
```

When I started using tmux I did almost everything in one giant session with
many panes and windows.  It became a nightmare to manage and quickly get
between two sets work efficiently.  This year I leaned in on sessions quite
heavily.  Checkout this 👇 post to see that workflow in depth.

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post
