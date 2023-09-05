---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux has-session
date: 2021-08-09T09:03:09
published: true

---

https://youtu.be/XucVVgGmesM

I see you there, trying to script out your tmux layouts. Tryig to get each
project setup just perfect with a script, but you keep stumbling over yourself
with `duplicate session` error messages

The `has-session` tmux command is a handy tool to prevent this `duplicate
session` error message when scripting your tmux layouts.

## command line

The command is pretty straight forward, you simply ask tmux if the session name
you are looking for exists.

``` bash
tmux has-session -t "waylonwalker_com"
```

https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
