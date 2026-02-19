---
title: '💭 Taildrop · Tailscale Docs'
date: 2024-09-24T13:19:09
template: link
link: https://tailscale.com/kb/1106/taildrop?tab=linux
tags:
  - tailscale
  - thoughts
  - thought
  - link
published: true

---

![[https://tailscale.com/kb/1106/taildrop?tab=linux]]

Tailscale comes with a feature called taildrop that lets you _easily_ share files between machines on your tailnet.  If you have tailscale on ios/android it shows up as a share target when you try to share something, and you can pick the machine to share with.

What was not obvious to me was how to receive the file on linux.  The linux tailscale service does not automatically receive the file, which can be kinda nice that you can put it where you want, but was not obvious to me at first.  Use this command to receive files.

``` bash
sudo tailscale file get .
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
