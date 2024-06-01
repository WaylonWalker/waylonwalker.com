---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux']
title: tmux floating popups
date: 2021-07-15T23:51:21
published: true

---

[https://youtu.be/2ZqFDsJywt8](https://youtu.be/2ZqFDsJywt8){.youtube-embed}

Tmux popups are actually floating windows that you can drag around the screen.  They always open in the middle (by default) when you open them, no matter where you leave them.

Here are a couple of keybindings I use to open up popup windows.

``` bash
bind C-g display-popup -E "ta ~/git"
bind -n M-g display-popup -E "tmux new-session -A -s scratch"
```

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post
