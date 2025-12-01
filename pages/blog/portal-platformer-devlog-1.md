---
date: 2025-04-28 19:56:58
templateKey: blog-post
title: portal-platformer-devlog-1
tags:
  - python
  - python
  - python
published: True

---

Here is the current state of my platformer yet to really be named, I want to
make something in between hollow knight and portal.


## Starting

I made one once in make code arcace on a pybadge.  It was quick and dirty, but
fun to work on.  It had the basic of blocks that I could move, blocks i could
put a portal onto, and a goal for each level.  Some levels you can just walk
through and some levels required you to really think about where to place the
portal.

## History

So this version of the game is a least 2 years in the making, I open it every
few months give it a day or two and move on.  Its mostly something that I work
on with my son.  He really likes to jump around on projects so its hard to make
real progress on something, but we are hitting an age where he is able to come
back to projects a little better.

All of this is built in python, and mostly before vibe coding was a thing, its
mostly me trying to get out ideas as quick as my son is spitting out the the
next idea.

## Coyote

It includes a few frames of coyote so it feels a bit more like most games.

!! Note
    If you are unfamiliar with the term coyote in platformers it allows you to
    jump for a few frames after falling off a platform, like wiley coyoyte in
    Luney Toons.

## Wall slide/jump

Wall slide and jump work, but so is wall climb as an unintended side effect.
When you are touching a wall, your fall speed is halved.

## Levels and loader

There is a crude level loader that loads json levels with pydantic.  No editor
yet, just hand editing levels with json.

## Checkpoints

It makes checkpoints, when you die, you go back to your last checkpoint.
Checkpoints can be invisible, and have a link that turns them into a door to
another level.

![66c5b984-5450-48ee-9978-00fec4815807.mp4](https://dropper.wayl.one/api/file/66c5b984-5450-48ee-9978-00fec4815807.mp4)


## no art

There is no art yet, just the skin of a platformer, levels, checkpoints, and
coyote.  No portals, but there is a pointer with a janky box that covers my
lighting.
