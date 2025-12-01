---
date: 2024-06-25 18:23:41
templateKey: til
title: playerctl fixes arch media keys
published: true
tags:
  - linux

---

I've long had issues with my qmk keyboard media keys on my arch install, I
always thought it was on the keyboard end.  Today I learned that playerctl
fixes this.

``` bash
paru -S playerctl
```

Once it is installed all of my media keys started working right away.

I played around with it a bit more and came up with a way to display the
current playing title in my notifictations.

```bash
notify-send "`playerctl metadata --format '{{lc(status)}}:{{artist}}-{{album}}-{{title}}'`"
```
