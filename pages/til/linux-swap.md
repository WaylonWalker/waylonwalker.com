---
date: 2022-03-18 13:29:49.002948
templateKey: til
title: Create a Swapfile on Your Linux Machine
tags:
  - linux

---


If you ever end up on a linux machine that just does not have enough ram to
suffice what you are doing and you just need to get the job done you can give
it some more swap.  You can look up reccomendations for how much swap you
should have this is more about just trying to get your job done when you are
almost there, but running out of memory on the hardware you have.

## make the /swap file

You can put this where you wish, for this example I am going to pop it into
`/swap`

```bash
sudo fallocate -l 4G /swap
sudo chmod 600 /swap
sudo mkswap /swap
sudo swapon /swap
```

## make sure that your swap is on

You can make sure that your swap is working by using the `free` command, I like
using the `-h` flag to get human readable numbers.

```bash
❯ free -h
               total        used        free      shared  buff/cache   available
Mem:            15Gi       5.5Gi       4.9Gi       458Mi       5.2Gi       9.3Gi
Swap:          4.0Gi          0B       4.0Gi
```

https://waylonwalker.com/reset-ipython

> I also used this trick in this article to give my python process a bit more oompf and get it on home.
