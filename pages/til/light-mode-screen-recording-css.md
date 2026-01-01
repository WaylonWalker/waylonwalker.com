---
date: 2026-01-02 10:29:10
templateKey: til
title: light mode screen recording css
published: true
tags:
  - webdev

---

Yesterday I wrote about a way to do [[ light-mode-screen-recording ]] to
convert to light mode from dark mode with ffmpeg.  I was wondering if it could
be done entirely on the front end for web applications.  Turns out you can.
I'm sure there are limited wikis and site builders that don't allow adding
style like this, but it works if you can.

``` html
<video
    src="https://dropper.wayl.one/file/1c53dbcb-4b84-4e94-9f04-a42986ab3fa1.mp4?width=800"
    controls
    style="filter: invert(1) hue-rotate(180deg) contrast(1.2) saturate(1.1);"
    >
</video>
```

<video src="https://dropper.wayl.one/file/1c53dbcb-4b84-4e94-9f04-a42986ab3fa1.mp4?width=800" controls style="filter: invert(1) hue-rotate(0deg) contrast(1.2) saturate(1.1);" ></video>

> 0 deg hue rotate

<video src="https://dropper.wayl.one/file/1c53dbcb-4b84-4e94-9f04-a42986ab3fa1.mp4?width=800" controls style="filter: invert(1) hue-rotate(90deg) contrast(1.2) saturate(1.1);" ></video>

> 90 deg hue rotate

<video src="https://dropper.wayl.one/file/1c53dbcb-4b84-4e94-9f04-a42986ab3fa1.mp4?width=800" controls style="filter: invert(1) hue-rotate(180deg) contrast(1.2) saturate(1.1);" ></video>

> 180 deg hue rotate

<video src="https://dropper.wayl.one/file/1c53dbcb-4b84-4e94-9f04-a42986ab3fa1.mp4?width=800" controls style="filter: invert(1) hue-rotate(270deg) contrast(1.2) saturate(1.1);" ></video>

> 270 deg hue rotate

