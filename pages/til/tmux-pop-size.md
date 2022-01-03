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
tmux popup -h 100% -w 100% -x 0% figlet "Hello"
# 75% centered popup
tmux popup -h 100% -w 75% -x 0% figlet "Hello"
# 75% popup on left side
tmux popup -h 100% -w 75% -x 0% figlet "Hello"
```

![example video running these commands](https://images.waylonwalker.com/tmux-popup-position.gif)
