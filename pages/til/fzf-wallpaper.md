---
date: 2022-01-20 01:17:26.193849
templateKey: til
title: fuzzy wallpaper with fzf
tags:
  - linux
  - cli
  - bash

---

I really appreciate that in linux anything can be scripted, including
setting the wallpaper.  So everytime I disconnect a monitor I can just
rerun my script and fix my wallpaper without digging deep into the ui
and fussing through a bunch of settings.

``` bash
feh --bg-scale ~/.config/awesome/wallpaper/my_wallpaper.png
```

> I set my default wallpaper with `feh` using the command above.

Leaning in on feh, we can use fzf to pick a wallpaper from a directory
full of wallpapers with very few keystrokes.

```
alias wallpaper='ls ~/.config/awesome/wallpaper | fzf --preview="feh --bg-scale ~/.config/awesome/wallpaper/{}" | xargs -I {} feh --bg-scale ~/.config/awesome/wallpaper/{}'
```

> I have mine alias'd to `wallpaper` so that I can quickly run it from
> my terminal.
