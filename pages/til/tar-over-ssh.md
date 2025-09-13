---
date: 2025-09-13 10:50:42
templateKey: til
title: tar over ssh
published: true
tags:
  - bash
  - linux
  - homelab

---

Today I learned how to use tar over ssh to save hours in file transfers.  I
keep all of my projects in ~/git (very creative I know, I've done it for years
and haven't changed).  I just swapped out my main desktop from bazzite to
hyprland, and wanted to get all of my projects back.  Before killing my
bazzite install I moved everything over (16GB of many small files), it took
over 14 hours, maybe longer.  I had started in the morning and just let it
churn.

This was not going to happen for re-seeding all of my projects on my new
system, I knew there had to be a better way, I looked at rsync, but for seeding
I ran into this tar over ssh technique and it only took me 6m51s to pull all of
my projects off of my remote server.

``` bash
ssh user@192.168.1.100 'tar -C /tank/git -cpf - .' \
  | tar -C "$HOME/git" -xpf -
```


