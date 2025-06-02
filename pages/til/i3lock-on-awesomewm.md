---
date: 2025-06-02 14:40:56
templateKey: til
title: i3lock on AwesomeWM
published: true
tags:
  - linux
  - awesomewm

---

`i3lock` is a fantastic lockscreen for tiling window managers.

If you are using a tiling window manager within a public space you need to add
a lockscreen.  I have one machine that I take with me to a public space.  Its
secure enough that I can leave it, but not secure enough that I want to leave
it unlocked.  So when I need to leave it behind for the restroom I need to lock
it up.


``` bash
paru -S i3lock
# or
apt install i3lock
```

Now that you have `i3lock` installed lets lock that screen.

``` bash
# lock it with a pure white flashbang
i3lock

# lock it with a black background
i3lock -c 000000

# lock it with a custom color
i3lock -c 2e1330

# lock it with a wallpaper
i3lock -c 000000 ~/Pictures/Wallpapers/mywallpaper.png
```

You can use your window manager or something more generic like xbindkeys to set
a hotkey. This way you don't have to open a terminal and type out the command
every time you leave your desk.  You can just press something like `SUPER+L`
like you would on other OS's.
