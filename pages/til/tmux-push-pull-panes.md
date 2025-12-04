---
date: 2022-12-04 13:25:54
templateKey: til
title: tmux push/pull panes
status: 'draft'
tags:
  - cli
  - tmux

---

Moving panes between tmux sessions is something that makes tmux a very flexible
and powerful tool.  I don't need this feature very often, but it comes in
clutch when you need it.

## Pull a pane from any other session

Using `choose-window` I was able to come up with a way to select any pane
withing any other session and join it into my current session.

``` bash
# Choose a pane to join in horizontally
bind f choose-window -Z 'join-pane -h -s "%%"'
```

## Push/Pull from scratch

I've long had this one in my tmux config, I always have a "scratch" session
that I'm running, I often use for looking at things like `k9s` accross repos
within a popup.

This use case puts a pane into the scratch session, then pulls it back out.  I
will use this to move a pane between sessions in the rare cases I need to do
this.

``` bash
# push the active pane into the scratch session horizonally
bind -n M-f join-pane -ht scratch
# pull the last active pane from the scratch session horizonally into this session
bind -n M-F join-pane -hs scratch
```
