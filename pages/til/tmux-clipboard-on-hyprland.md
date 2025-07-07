---
date: 2025-07-06 20:45:47
templateKey: til
title: tmux clipboard on hyprland
published: true
tags:
  - python

---

Smooth clipboard settings for tmux is critical for my workflow.  I'm often
grabbing snippets of terminal output to paste into team chats, blog posts, or
llm prompts.  Admittedly, I'm often doing this with the mouse, unless it's
coming from neovim, which I generally do with motions.  Moving from an `xorg`
based setup to hyprland has required me to reconfigure my tmux clipboard
settings.  This is what I did.

First install wl-clipboard with paru.

``` bash
paru -S wl-clipboard
```

Next add this to your tmux config.  I've long had this config, but with only
the `xorg`/`xclip` setup, now this checks for wl-copy, uses it, or falls back to
my old `xclip` setup.

``` bash
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "bash -c 'command -v wl-copy >/dev/null && wl-copy || xclip -i -f -selection primary | xclip -i -selection clipboard'"
set-option -s set-clipboard off
bind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "bash -c 'command -v wl-copy >/dev/null && wl-copy || xclip -i -f -selection primary | xclip -i -selection clipboard'"
```
