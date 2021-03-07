---
templateKey: hot-tip
tags: [bash]
title: Scripting Tmux Layouts
date: 2020-12-13T00:00:00
status: draft
description: ''
cover: "/static/scripting-tmux-layouts.png"

---


This is how I script a tmux layout

``` bash
 bash -c "tmux new-session -t 'editor' -d;\
    tmux split-window -v 'zsh';
    tmux send-keys nvim Space /src/ Space +GFiles C-m; \
    tmux rotate-window; \
    tmux select-pane -U; \
    tmux -2 attach-session -d
    "
```
