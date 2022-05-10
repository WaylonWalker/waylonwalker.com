---
date: 2022-05-11 22:03:30
templateKey: til
title: qutebrowser clean up all status bars
tags:
  - python
  - linux
  - python

---

I really like the super clean look of no status menus, no url bar, no bookmarks
bar, nothing.  Don't get me wrong these things are useful, but honestly they
take up screen real estate and I RARELY look at them.  What I really want is a
toggle hotkey.  I found this one from one of DT's youtube video's.  I can now
tap `xx` and both the status bar at the botton and the address bar at the top
disappear.

``` python
# ~/.config/qutebrowser/config.py

config.bind("xb", "config-cycle statusbar.show always never")
config.bind("xt", "config-cycle tabs.show always never")
config.bind(
    "xx",
    "config-cycle statusbar.show always never;; config-cycle tabs.show always never",
)
```
