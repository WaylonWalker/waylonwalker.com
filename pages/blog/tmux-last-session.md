---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux']
title: tmux last session
date: 2021-07-16T23:51:21
published: true

---

[https://youtu.be/RB87EEnnMnU](https://youtu.be/RB87EEnnMnU){.youtube-embed}

An ultimate productivity key-binding in tmux is one to switch to the last session.  I use this to quickly get between sessions really quick.  Often I am working and need to lookup a quick note, or copy something into my notes, then get back to where I was quickly.

``` bash
bind -n M-b switch-client -l
```

I think of this hub and spoke model, and use `last-session` to quickly drive it.

![hub and spoke](https://images.waylonwalker.com/tmux-nav-hub-spoke.png)

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post
