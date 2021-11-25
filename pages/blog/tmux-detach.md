---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux',]
title: tmux detach
date: 2021-07-32T23:51:21
status: published

---

https://youtu.be/A1qx3tNKDdA

tmux detach is a handy tmux command that will quit your current session while
keeping it running. The full name of the comamnd is `detach-client`, `detach`
is a shorthand.

default keybinding

``` bash
bind-key          d detach-client
```

I have mine bound to `mod+d` where mod is alt.

``` bash
bind -n M-d detach-client
```

https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
