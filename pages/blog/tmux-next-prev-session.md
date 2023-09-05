---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux next/prev session
date: 2021-08-04T09:03:09
published: true

---

https://youtu.be/8kZnjHPYnKU

Now that we are splitting up work into their own sessions, lets talk about how
to navigate between them without the command line.  Navigating sessions is what
kept me using a too many splits and windows workflow for far too long.  It was
rough, I was always tripping over panes and windows until I got too frustrated
and just ran `tmux kill-server`  to start on a new blank slate.

``` bash
bind -n M-P switch-client -p
bind -n M-N switch-client -n
```

https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
