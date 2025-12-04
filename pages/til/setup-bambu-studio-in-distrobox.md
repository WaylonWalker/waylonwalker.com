---
date: 2025-12-06 21:17:39
templateKey: til
title: setup bambu-studio in distrobox
published: true
tags:
  - linux

---

[[ gpus-are-awesome ]]

``` bash
distrobox enter bambu-studio
nvidia-smi
glxinfo | gprep OpenGL
sudo pacman -Syu --needed base-devel git
git clone https://aur.archlinux.org/paru-bin.git
cd paru-bin
makepkg -si
paru -S bambustudio-bin

bambu-studio

distrobox-export --app bambu-studio
```

