---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux']
title: tmux prefix
date: 2021-07-18T23:51:21
published: true

---

[https://youtu.be/BMkpbfhbkKM](https://youtu.be/BMkpbfhbkKM){.hoverlink}

The prefix key is an essential part of tmux, by default all of tmux's
key-bindings sit behind a prefix.  This prefix is very similar to vim's leader
key. It is common for folks to change the default `C-b` (control b) to `C-a` or
if they are a vim user something to match their vim leader key.

``` bash
set -g prefix C-Space
bind Space send-prefix
```

A few of the essential default key-bindings.

```
%      vertical split
"      horizontal split
d      detach

up     select up one pane
down   select down one pane
right  select right one pane
left   select left one pane

t      clock
o      swap panes
c      create window
n      next window
p      previous window
```

A more complete list of key-bindings can be found in this gist <https://gist.github.com/mzmonsour/8791835>.

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post
