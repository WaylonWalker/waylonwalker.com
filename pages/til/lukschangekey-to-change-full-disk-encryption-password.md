---
date: 2026-09-01T21:51:16Z
templateKey: til
title: "Lukschangekey to change full disk encryption password"
tags:
  - "linux"
published: true

---

I'm playing with omarchy on an old laptop and decided I want to share it with my kids without sharing what I also set up as my sudo password.

``` bash
Lsblk -f
```

Look for the one labeled crypto_LUKS

``` bash
Sudo cryptsetup luksChangeKey /dev/nvme0n1p2
```

Then you will be asked for your sudo password, previous full disk encryption password, then the new one twice.

Now my laptop can be shared without sharing my private `sudo` password.