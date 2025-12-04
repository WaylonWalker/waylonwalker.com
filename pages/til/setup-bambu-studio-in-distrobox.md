---
date: 2025-12-06 21:17:39
templateKey: til
title: setup bambu-studio in distrobox
published: true
tags:
  - linux

---

[[ gpus-are-awesome ]] and I need one for Bambu Studio to be usable in a
distrobox.  Adding the `--nvidia` flag to `distrobox create` bind mounts the
nvidia `/dev/` devices and sets up the necessary environment variables.  Once
we are in there are a couple of packages to install to make it work.

``` bash
distrobox create --name bambu-studio --image archlinux:latest --nvidia
distrobox enter bambu-studio
sudo pacman -S nvidia-utils lib32-nvidia-utils vulkan-icd-loader
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

