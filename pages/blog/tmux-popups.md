---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux']
title: tmux popups
date: 2021-07-14T23:51:21
published: true

---

<https://youtu.be/2I8fB28zfB4>

Tmux-popups are a great feature that is relatively new to tmux, many repos such
as the standard ubuntu repos do not have it.   Popups came in 3.2a, if your
package manager does not have it, you can follow the [tmux's install
instructions](https://github.com/tmux/tmux#installation) to build from source.

``` bash
# open a popup scratchpad
bind -n M-g display-popup -E "tmux new-session -A -s scratch"
```

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post

I use popups quite a bit in my workflow to ssh into another machine for a short
period, or make a new project with a template.
