---
date: 2022-07-16 08:43:17
templateKey: til
title: Manage your displays with xrandr manager
published: false
tags:
  - python
  - linux
---

![a stable diffusion done with a111 web ui](https://images.waylonwalker.com/9cd8d65495366b8d57d805ca0faf5fd5.webp)

xrandr is a great cli to manage your windows in a linux distro using x11, which
is most of them. The issue is that I can never remember all the flags to the
command, and if you are using it with something like a laptop using a dock the
names of all the displays tend to change every time you redock. This makes it
really hard to make scripts that work right every time.

## Homepage

Check out the
[deresmos/xrandr-manager](https://github.com/deresmos/xrandr-manager) for more
details on it.

## installation

xrander-manager is a python cli application that is simply a nice interface
into xrandr. So you must have xrandr already installed, which is generally
just there on any x11 window manager, I've never had to install it.

As with any python cli that is indended to be used as a global/system level cli
application I always install them with pipx. This automates the process of
creating a virtual environment for xrandr-manager for me, and does not clutter
up my system packages with its dependencies that may eventually clash with
another that I want to use.

```
# prereqs (xrandr, pipx)
pipx install xrandr-manager
```

## set main monitor

First if your main display is not set to the correct monitor set your main
display first.

```
xrandr-manager -m HDMI-0
xrandr-manager -m DP-0
```

## prompt mode

If you dont know the name of your monitors and and don't want to dig through
xrandr, you can just run `--prompt` and tab complete to fill set your main
display.

```
xrandr-manager --prompt
```

## direction

This is what I most often use xrandr-manager for. Once you have the main
display set you can tell it where to put the other monitor. I've only tried
this with two monitors, I have no idea what happens with more monitors.

```
xrandr-manager -d right
xrandr-manager -d left
xrandr-manager -d above
xrandr-manager -d below
```

## mirror

One thing that I always need to jump through hoops to do is mirror.
Occasionally I want to mirror so that more people can see the screen while we
are split screen gaming. This has seemed like a pain in any other xrandr
utility, but trivial in xrandr-manager.

```
xrandr-manager --mirror
```

## It logs out the xrandr command

One nice thing about xrandr-manager is that it echos out the xrandr command
that it's running. This is nice because you can toss this behind a hotkey or an
init script.

## Guis

Ya there are guis that do this. I've had good luck with arandr. It's more
intuitive to drag windows around like what you would do in windows. Every once
in awhile it messes up and my polybar overlaps my windows, or my windows end up
only on half the screen.

There are also graphics card specific utilities, Ive used nvidia x server
settings and it mostly works similar to arandr.
