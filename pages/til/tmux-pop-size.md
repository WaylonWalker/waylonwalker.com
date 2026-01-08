---
date: 2022-01-05 17:37:26.947238
templateKey: til
title: Tmux Pop size
tags:
  - tmux
  - linux
  - bash

---

tmux popups can be sized how you like based on the % width of the
terminal on creation by using the flags (h, w, x, y) for height, width,
and position.

``` bash
# normal popup
tmux popup figlet "Hello"
# fullscreen popup
tmux popup -h 100% -w 100% figlet "Hello"
# 75% centered popup
tmux popup -h 100% -w 75% figlet "Hello"
# 75% popup on left side
tmux popup -h 100% -w 75% -x 0% figlet "Hello"
```

<video autoplay="" controls="" loop="true" muted="" playsinline="" width="100%" class="rounded-xl border-pink-900 border-2">
     <source
      src="https://dropper.waylonwalker.com/api/file/c0e80bc5-a03d-40ad-a431-20436b82cf3b.mp4"
      type="video/mp4">
     Sorry, your browser doesn't support embedded videos.
</video>

> example running these commands
