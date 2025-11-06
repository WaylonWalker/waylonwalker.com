---
date: 2025-11-05 20:10:02
templateKey: blog-post
title: Mcat Anything
tags:
  - python
published: True

---

I've long looked for a way to cat anything in the terminal.   I'm am terminally
in the terminal.  I manage all of my projects, code, website, notes, files,
servers, infrastructure, almost everything from the terminal.  I occasionally
open a file manager, mostly at home, only so that I can browse images.

Compounding my issue, I'm a tmux user. It works great for me, and I barely have
to think about it at this point. The keybindings are second nature to me.  I
can go between server, terminal, nvim, and between projects instantly, no
loader, no lag, no animation, it just works for everything that really matters
to me for really getting things done.

## Mcat

`mcat` is a new tool that seems like it can cat anything in the terminal, code,
files, images, markdown, markdown with images, and even video, without leaving
tmux!

``` bash
mcat static/8bitcc.png
curl https://r.jina.ai/https://waylonwalker.com/store/ | mcat --theme dracula --md-image all
curl https://r.jina.ai/https://waylonwalker.com/shots/ | mcat --theme dracula
mcat ~/git/dropper/data/01b21044-0bf8-4b06-9db1-a002c0519df6.mp4
mcat ~/git/dropper/data/0e659c05-1c12-4524-aa54-ef52ba680865.webm
```

<!-- ![1fa2e162-deeb-4bb5-b1c5-961632abd452.mp4](https://dropper.wayl.one/api/file/1fa2e162-deeb-4bb5-b1c5-961632abd452.mp4) -->
![1fa2e162-deeb-4bb5-b1c5-961632abd452.webm](https://dropper.wayl.one/api/file/663a3793-6426-4b91-a7df-835540d16910.webm)

## But it doesn't always work

The keen eyed of you will notice the blank screen at the start of the demo
above, not sure what happened, but resizing the terminal fixed something.
Sometimes video comes up as an image, sometimes it core dumps, once even it
crashed my system...

The hope is there, I'll continue to use it occasionally, but right now it feels
like a novelty that is fun to look at when it works.  For now I'm going to
stick to my kitty/tmux combo that works even though they seem to hate each
other and I'm going to be happy just getting shit done.
