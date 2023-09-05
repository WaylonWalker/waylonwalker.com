---
date: 2022-10-17 08:55:26
templateKey: til
title: localstack status permission
published: true
tags:
  - aws

---

I ran into an issue where I was unable to ask localstack for its status. I
would run the command and it would tell me that it didn't have permission to
read files from my own home directory.  Let's fix it

## The issue

I would run this to ask for the status.

``` bash
localstack status
```

And get this error

``` bash
PermissionError: [Errno 13] Permission denied: '/home/waylon/.cache/localstack/image_metadata'
```

## What happened

It dawned on me that the first time I ran localstack was straight docker, not
the python cli.  When docker runs it typically runs as root unless the
Dockerfile sets up a user and group for it.

!["cell shaded, long, full body, shot of a cybernetic blue soldier with glowing pink eyes, llustration, post grunge, cinebatic dramatic atmosphere, sharp focus, pink glowing volumetric lighting, concept art by josan gonzales and wlop, by james jean, Victo ngai, David Rubín, Mike Mignola, Laurie Greasley, highly detailed, sharp focus,alien,Trending on Artstation, HQ, deviantart, art by artgem" -s50 -W832 -H416 -C12.0 -Ak_lms -S3517264680 ](https://stable-diffusion.waylonwalker.com/000364.3517264680.webp)

## How to fix it

If you have sudo access to the machine you are on you can recursively change
ownership to your user and group.  I chose to just give myself ownership of my
whole `~/.cache directory` you could choose a deeper directory if you want.  I
feel pretty safe giving myself ownership to my own cache directory on my own
machine.

``` bash
whoami
# waylon

chown -R waylon:waylon ~/.cache
```

## Now it's working

Running localstack status now gives me a nice status message rather than an
error.

``` bash
❯ localstack status
┌─────────────────┬───────────────────────────────────────────────────────┐
│ Runtime version │ 1.2.1.dev                                             │
│ Docker image    │ tag: latest, id: dbbfe0ce0008, 📆 2022-10-15T00:51:03 │
│ Runtime status  │ ✖ stopped                                             │
└─────────────────┴───────────────────────────────────────────────────────┘
```
