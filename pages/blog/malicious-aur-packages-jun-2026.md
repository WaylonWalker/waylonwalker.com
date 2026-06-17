---
date: 2026-06-16 20:27:26
templateKey: blog-post
title: Malicious Aur Packages Jun 2026
tags:
  - linux
published: True

---

Recent Arch linux vulnerabilities are a good reminder of a few things.

1. AUR is not the official package repo
2. The AUR is community driven
3. AUR packages are not always safe

The first thing I'm doing to stop myself from running any aur updates
automatically is removing any arch helper.

``` bash
sudo pacman -Rns yay paru paru-bin
```

Currently the reported vulnerabilities are supply chain attacks limited to the
aur, keep your arch system up do date, **BUT** do not update packages from the
AUR right now.  In fact I'm auditing my aur usage and removing anything I have
not used in awhile.

Here is a nice script I'm using to walk through my packages and get rid of
things I installed and probably don't need anymore.

``` bash
pacman -Qemq |
  fzf -m --preview '
    echo "== package =="
    pacman -Qi {} 2>/dev/null
    echo
    echo "== required by =="
    pacman -Qi {} 2>/dev/null | grep "Required By"
  ' |
  xargs -r -o sudo pacman -Rns
```

Supply chain attacks are getting real scary in 2026, maybe we should listen to
Ginger Bill a bit closer.
