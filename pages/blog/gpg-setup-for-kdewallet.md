---
date: 2025-07-04 13:52:43
templateKey: blog-post
title: gpg setup for kdewallet
tags:
  - linux
published: False

---

I'm trying to setup gpg for kdewallet on archlinux with hyprland so that brave
shuts up.  I've tried this, but brave still complains about the wallet setup,
so this post is to be continued.

``` bash
sudo pacman -S gnupg
gpg --full-generate-key
# use RSA
# key length 4096
# passphrase
gpg --list-keys
```
