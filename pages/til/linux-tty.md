---
date: 2022-04-08 13:46:25.768509
templateKey: til
title: A TTY Can Save Your Bacon
tags:
  - linux
  - linux
  - linux

---

I recently was unable to boot into my home Linux Desktop, it got stuck at
diskcheck `fsck`.  I found that I was able to get in to a tty through a hotkey.

https://twitter.com/_WaylonWalker/status/1512281106120384519

## What's a TTY?

There's probably more to it, but to me its a full screen terminal with zero
gui, not even your gui fonts.  It does log into your default shell so if you
have a comfy command line setup it will be here for you even though it looks
much different without fonts and full colorspace.

## Normal setup

Normally you have 6 TTY's running, the first is dedicated to your desktop
manager, which is your login screen it might be something like gdm or lightdm.

* ctrl+alt+F1: login screen
* ctrl+alt+F2: Desktop
* ctrl+alt+F3: TTY 3
* ctrl+alt+F4: TTY 4
* ctrl+alt+F5: TTY 5
* ctrl+alt+F6: TTY 6

In my case the desktop manager neverstarted, so ctrl+alt+F1 brought me into a tty.

## What happened??

Well after getting back in and having some time to reflect, I think my Desktop
manager was installed or just broken, possibly during a update I ran a few days
prior.

I tried a bunch of things like switching to lightdm, and manually running startx.

## Getting back in

The final commands that ended up getting me back in were installing and starting gdm3.

``` bash
sudo apt install gdm3
sudo systemctl start gdm3
```
