---
date: 2022-09-26 06:15:24
templateKey: til
title: django disallowed host
status: 'published'
tags:
  - python
  - django
  - webdev

---

I am continuing my journey into django, but today I am not at my workstation. I
am ssh'd in remotely from a chromebook.  I am fully outside of my network, so I
can't access it by localhost, or it's ip.  I do have cloudflared tunnel
installed and dns setup to a `localhost.waylonwalker.com`.

## Settings

I found this in `settings.py` and yolo, it worked first try.  I am in from my
remote location, and even have auth taken care of thanks to cloudflare.  I am
really hoping to learn how to setup my own auth with django as this is one of
the things that I could really use in my toolbelt.

``` python
ALLOWED_HOSTS = ['localhost.waylonwalker.com']
```

!["cell shaded long shot of a cybernetic blue bald soldier with glowing blue eyes as Borderlands 3 concept art, llustration, post grunge, concept art by josan gonzales and wlop, by james jean, Victo ngai, David Rubín, Mike Mignola, Laurie Greasley, highly detailed, sharp focus,alien,Trending on Artstation, HQ, deviantart, art by artgem" -s50 -W832 -H416 -C7.5 -Ak_lms -S3422093952 ](https://stable-diffusion.waylonwalker.com/000321.3422093952.webp)
