---
templateKey: blog-post
tags: ["cli", "linux", "tmux"]
title: tmux detach
date: 2021-08-01T23:51:21
published: true
---

[https://youtu.be/A1qx3tNKDdA](https://youtu.be/A1qx3tNKDdA){.youtube-embed}

tmux detach is a handy tmux command that will quit your current session while
keeping it running. The full name of the comamnd is `detach-client`, `detach`
is a shorthand.

default keybinding

```bash
bind-key          d detach-client
```

I have mine bound to `mod+d` where mod is alt.

```bash
bind -n M-d detach-client
```

[https://waylonwalker.com/tmux-nav-2021/](https://waylonwalker.com/tmux-nav-2021/){.hoverlink}

> for more information on how I navigate tmux, check out this full post

Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
