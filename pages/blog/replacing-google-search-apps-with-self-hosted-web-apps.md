---
date: 2025-05-22 14:31:29
templateKey: blog-post
title: tinyapps
tags:
  - self-hosted
  - slash
  - meta
published: True

---

I'm working on replacing my usage of google inline search apps with real apps,
these are ones that I create and host on my own homelab.  The first three that
I created are mostly chatgpt based, with a bit of hand edit after the fact,
uploaded to minio and become an app on my
[k8s-pages](https://github.com/waylonwalker/k8s-pages)

!!! Note renamed
    The original title of this post was "Replacing Google Search Apps With Self Hosted Web Apps"

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

## b64

Today i spent some time on [b64](b64.wayl.one), it is a base64 decoder/encoder.
Just start tying to enter text, or paste, escape to deselect the text box, d to
decode, e to encode, ? for help.  It took a bit to get all of the keymaps right
with the differnt modes and make sure that for instance you don't keep typing
in the input box while in help mode, or decode/encode while in the input box.

[![screenshot of https://b64.wayl.one](http://shots.wayl.one/shot/?url=https://b64.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://b64.wayl.one)
