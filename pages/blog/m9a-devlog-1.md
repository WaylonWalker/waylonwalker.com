---
date: 2025-05-11 09:33:44
templateKey: blog-post
title: m9a devlog 1
tags:
  - python
  - markata
  - textual
  - tui
published: True

---

It's sad to see textualize.io close the doors, but textual is still alive and
maintained as a n open source project.  I tried to use it very early, and
struggled, this was before docs and tutorials really existed, before a lot of
the widgets and components existed.  Then as we all do I got busy and moved on
to other things in life and did not have the capacity to build TUIs.

## I like tuis

I like tuis, I like staying in the terminal.  I use
[lf](https://github.com/gokcehan/lf) daily to move files around when I
want something more than `mv` and `cp`.  I use
[k9s](https://github.com/derailed/k9s) hourly to monitor and manage my
kubernetes cluster.

## Are they worth the effort??

As awesome as tui's are, they are more effort to build, and less automatable.
I feel like the first stage into automation of a project really needs to be a
good cli, and this is often good enough for the project and I move on.

## m9a (em - nine - ah)

_inspired by k9s_

Like I said I really like k9s and use it all the time, It really makes running
kubectl commands a breeze and much less verbose.  I don't know how useful this
will be, but as a learning exercise I am working on a k9s experience for my
blog generator [[ markata ]].

![m9a-1.webm](https://dropper.wayl.one/api/file/1d409101-1024-490c-9dd0-3a6f7f42a708.webm)

## Learning

So far this is just for learning and not quite the most useful thing, I am not
sure if there is a way to do it, but I am interested in the idea of some sort
of framework (maybe just widgets) that can more easily turn pydantic objects
into this kind of tui.  I don't quite know how it would work, or if it could
work, for now just exploring the idea, and I think I hit a fairly crude clone
of k9s so far.
