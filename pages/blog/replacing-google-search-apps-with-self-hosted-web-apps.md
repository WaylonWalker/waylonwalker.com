---
date: 2025-05-22 14:31:29
templateKey: blog-post
title: replacing google search apps with self hosted web apps
tags:
  - self-hosted
published: True

---

I'm working on replacing my usage of google inline search apps with real apps,
these are ones that I create and host on my own homelab.  The first three that
I created are mostly chatgpt based, with a bit of hand edit after the fact,
uploaded to minio and become an app on my [k8s-pages](<https://github.com/waylonwalker/k8s-pages>

I'm leaning on [[web-wakelock]] to keep the screen on while these apps are
running, primarily clos, timer, and stopwatch.

## Clock

A large displya clock.

[![screenshot of https://clock.wayl.one](http://shots.wayl.one/shot/?url=https://clock.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://clock.wayl.one)

## Timer

A simple timer that counts down from thet set time.

[![screenshot of https://timer.wayl.one](http://shots.wayl.one/shot/?url=https://timer.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://timer.wayl.one)

## Stopwatch

This is the one that inspired it all, I need to run a few stopwatches at work,
and chose to just do it right in the google search with a few tabs running.

[![screenshot of https://stopwatch.wayl.one](http://shots.wayl.one/shot/?url=https://stopwatch.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://stopwatch.wayl.one)

## Dice

A simple dice roller, this one is the one that I decided to start adding `?`
for help.

[![screenshot of https://dice.wayl.one](http://shots.wayl.one/shot/?url=https://dice.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://dice.wayl.one)

## UUID

It displays a uuid, thats it.  <kbd>ctrl</kbd> + <kbd>c</kbd> to copy.

[![screenshot of https://uuid.wayl.one](http://shots.wayl.one/shot/?url=https://uuid.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://uuid.wayl.one)
