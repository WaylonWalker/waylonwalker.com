---
date: 2026-07-12 11:02:28
templateKey: til
title: ^M for carriage return
published: false
tags:
  - linux
  - vim

---

I don't run into windows file endings very often, so when I see little `^M`'s
all over your file, I think "shit I know what these are and cant remember"
They represent the windows carriage return.

## Linux vs Unix Line Endings

The difference here is that Unix uses `\n` and Linux uses `\r\n`, going all the
way back to the typewriter it represents the two keys that a typist would have
to press to get a new line and return the carriage back to the beginning.

## Vim/Neovim

When I open up a file and see this garbage all over, its not cozy, I want them
gone, I dont want them all over my editor.  I'm not sure what this would look
like on windows, I haven't been able to afford a windows machine in years, but
its gross on my machine.

![131d6463-bcbb-4ee8-80aa-bb7355915eb9.webp](https://dropper.wayl.one/file/131d6463-bcbb-4ee8-80aa-bb7355915eb9.webp)

Remove them with a substitution command from normal mode.

``` vim
:%s/\r//g
```

![4c84c556-5d96-4df1-9324-217dfb2f951a.mp4](https://dropper.waylonwalker.com/file/4c84c556-5d96-4df1-9324-217dfb2f951a.mp4)
removing carriage returns with a substitution command

