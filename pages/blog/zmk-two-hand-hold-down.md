---
date: 2025-09-17 20:04:36
templateKey: blog-post
title: zmk two hand hold down
tags:
  - python
published: True

---

I don't know about you, but I don't re-flash my keyboard enough to ever remember
where I put the bootloader.  Sometimes its  the last thing I think about in a
refactor and I end up cornering myself into a place where I cant get into that
layer anymore.  I've started putting hardware switches on my newer builds, but
some older builds don't have a hardware one, so it requires disassembly and
jumping the microcontroller.  Even when I have one though, I gotta flip my
board over and its annoying sometimes, so I prefer to have a keystroke for it.

## Two Hand hold down

What I've landed on recently is the idea of a two hand hold down combo for the
bootloader.  These combos are ones that there is no way I can hit without
picking my hands up from their normal homerow position and pressing four keys
simultaneously with pointer and thumbs.

Here are some example layouts from [keymap-editor](https://nickcoutsos.github.io/keymap-editor/)

![screenshot-2025-09-17T01-06-16-427Z.png](https://dropper.wayl.one/api/file/fd4d31aa-b151-4bce-b411-8e4480898b83.png)

> 40% layout - similar to corne

![screenshot-2025-09-17T01-05-02-298Z.png](https://dropper.wayl.one/api/file/74626408-cb1e-43bd-8c4c-7fb2abb16ea2.png)

> Here it is on my Son's 3x5 macropad


![screenshot-2025-09-17T01-05-30-687Z.png](https://dropper.wayl.one/api/file/8afdd2cd-c362-40cb-b9ef-9cd70ba4b0cb.png)
> Here it is on my 3x3 macropad

## Timing

You can even give it a long prior timeout to really make sure that its not an
accidental hit.

![screenshot-2025-09-17T01-10-22-100Z.png](https://dropper.wayl.one/api/file/4a0c7dc0-f096-4be2-9b4d-e89cb787179a.png)

