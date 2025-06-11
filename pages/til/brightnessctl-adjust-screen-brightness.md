---
date: 2025-06-11 08:42:36
templateKey: til
title: brightnessctl adjust screen brightness
published: true
tags:
  - linux

---

Today I discovered `brightnessctl` to adjust the screen brightness on my
AwesomeWM machine.  Its a command line utility that you can use to adjust the
brightness of your screen.  A command line interface like this gives you the
ability to bind keys with something like [[xbindkeys]] or your window manager
configuration.


``` bash
sudo apt install brightnessctl
# or 
paru -S brightnessctl
```

Now that you have it installed you can use it to adjust the brightness of your
screen, this worked particularly well for my laptop screen, I don't think this
works for monitors, in my experience they are usually controlled by the built
in osd.

``` bash
# Increase brightness by 10%
brightnessctl set +10%
# Decrease brightness by 10%
brightnessctl set 10%-
# Set brightness to 50%
brightnessctl set 50%
# Set brightness to 100%
brightnessctl set 100%
```

!!! note
    on my machine I had to use `sudo` to run the command, otherwise I got the following error:

    ``` bash
    Can't modify brightness: Permission denied

    You should run this program with root privileges.
    Alternatively, get write permissions for device files.
    ```
