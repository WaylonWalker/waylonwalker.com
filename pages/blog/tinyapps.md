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

[![screenshot of https://clock.wayl.one](http://shots.waylonwalker.com/shot/?url=https://clock.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://clock.wayl.one)

## Timer

A simple timer that counts down from thet set time.

[![screenshot of https://timer.wayl.one](http://shots.waylonwalker.com/shot/?url=https://timer.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://timer.wayl.one)

## Stopwatch

This is the one that inspired it all, I need to run a few stopwatches at work,
and chose to just do it right in the google search with a few tabs running.

[![screenshot of https://stopwatch.wayl.one](http://shots.waylonwalker.com/shot/?url=https://stopwatch.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://stopwatch.wayl.one)

## Dice

A simple dice roller, this one is the one that I decided to start adding `?`
for help.

[![screenshot of https://dice.wayl.one](http://shots.waylonwalker.com/shot/?url=https://dice.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://dice.wayl.one)

## UUID

It displays a uuid, thats it.  <kbd>ctrl</kbd> + <kbd>c</kbd> to copy.

[![screenshot of https://uuid.wayl.one](http://shots.waylonwalker.com/shot/?url=https://uuid.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://uuid.wayl.one)

## b64

Today i spent some time on [b64](b64.wayl.one), it is a base64 decoder/encoder.
Just start tying to enter text, or paste, escape to deselect the text box, d to
decode, e to encode, ? for help.  It took a bit to get all of the keymaps right
with the differnt modes and make sure that for instance you don't keep typing
in the input box while in help mode, or decode/encode while in the input box.

[![screenshot of https://b64.wayl.one](http://shots.waylonwalker.com/shot/?url=https://b64.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://b64.wayl.one)

## PocketCal

This one is not mine, it's made by [Cassidy
Williams](https://cassidoo.co/post/pocketcal-build-log/)), but is within the
ethos and deserves a mention here.  Its a single page calendar that is a static
site completely rendered on the front end, data is stored in the url as you
interact with it.  None of your data goes to a server.

[![screenshot of https://pocketcal.com](http://shots.waylonwalker.com/shot/?url=https://pocketcal.com&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://pocketcal.com)

## qrcode

Today I wanted to finish an article that I was on afk and It killed me to get
it from my work computer to my phone, so I made a qrcode generator.  Paste in
or type in your message and it shows up as a qr code live.  This one needed an
event listener for window resize since the library creates a rigid canvas qr
code that does not fit on the screen once you create it then resize the window.

[![screenshot of https://b64.wayl.one](https://shots.waylonwalker.com/shot/?url=https://qrcode.waylonwalker.com/?text=https://waylonwalker.com/replacing-google-search-apps-with-self-hosted-web-apps%2F%3Ftext%3Dhttps%3A%2F%2Fshots.waylonwalker.com%2F&width=450&height=500)](https://qrcode.waylonwalker.com/?text=https://waylonwalker.com/replacing-google-search-apps-with-self-hosted-web-apps/)

I even added query params to pass hex codes in for `color` and `bg`.

[![screenshot of https://b64.wayl.one](https://shots.waylonwalker.com/shot/?url=https://qrcode.waylonwalker.com/?text=https://waylonwalker.com/replacing-google-search-apps-with-self-hosted-web-apps%2F%3Ftext%3Dhttps%3A%2F%2Fshots.waylonwalker.com%2F%26color%3Dff69b4%26bg%3Dffcc00&width=450&height=500)](https://qrcode.waylonwalker.com/?text=https://waylonwalker.com/replacing-google-search-apps-with-self-hosted-web-apps/)
