---
date: 2026-01-01 10:14:17
templateKey: til
title: light mode screen recording
published: true
tags:
  - ffmpeg
  - dev

---



I saw this tip from
[Cassidoo](https://cassidoo.co/post/ffmpeg-dark-light/)
and had to try it out for myself.  I kicked on a
screen recording right from where my terminal
was, converted it, and it actually looks pretty
good.


``` bash
ffmpeg \
   -i screenrecording-2026-01-01_10-10-49.mp4 \
   -vf "negate,hue=h=180,eq=contrast=1.2:saturation=1.1" \
   screenrecording-2026-01-01_10-10-49-light.mp4
```

![](https://dropper.waylonwalker.com/file/1c53dbcb-4b84-4e94-9f04-a42986ab3fa1.mp4)

> Dark Mode

![](https://dropper.waylonwalker.com/file/de4e3378-6df2-45b1-84d5-0cc773ceb3c5.mp4)

> Light Mode

There are a few unsettling things about it, but
overall I feel like it was a success.

