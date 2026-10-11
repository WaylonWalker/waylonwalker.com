---
date: 2026-09-01T21:51:16Z
templateKey: til
title: "Lukschangekey to change full disk encryption password"
tags:
  - "linux"
published: true
authors:
  - waylon
  - id: gpt-6-luna
    role: copy editor
    details: "Corrected spelling and grammar with GPT-6 Luna."
---

I'm playing with omarchy on an old laptop and decided I want to share it with my kids without sharing what I also set up as my sudo password.

``` bash
lsblk -f
```

Look for the one labeled crypto_LUKS

``` bash
sudo cryptsetup luksChangeKey /dev/nvme0n1p2
```

Then you will be asked for your sudo password, previous full disk encryption password, then the new one twice.

Now my laptop can be shared without sharing my private `sudo` password.