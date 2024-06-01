---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux',]
title: tmux break-pane
date: 2021-07-26T23:51:21
published: true

---

[https://youtu.be/ICL609F2xnc](https://youtu.be/ICL609F2xnc){.youtube-embed}

Break-pane is a handy tmux command when your layout gets too cramped and you
want to just move a split into its own window.  Calling `break-pane` does
exactly that, it creates a `new-window` for you and moves your currently
selected split into that window

Default key binding for `break-pane`

``` bash
bind-key          ! break-pane
```

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post
