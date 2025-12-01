---
date: 2024-07-25 12:51:29
templateKey: til
title: convert mp4 for twitter with ffmpeg
published: true
tags:
  - bash

---

I've had a couple of uploads to twitter fail recently and has been a pain.  I
tried some online converters for convenience, but none of them worked.  I
reached out to chatgpt and found succeess with this ffmpeg command.

``` bash
ffmpeg -i input.mp4 \
  -vf "scale=trunc(oh*a/2)*2:min(720\,trunc(ih*a/2)*2)" \
  -c:v libx264 -profile:v high -level:v 4.1 \
  -b:v 3500k -maxrate 3500k -bufsize 7000k \
  -pix_fmt yuv420p \
  -c:a aac -b:a 128k -ar 44100 \
  -movflags +faststart \
  output.mp4
```
