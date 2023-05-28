---
date: 2023-05-27 20:22:42
templateKey: til
title: setting up paru | installing from the AUR for the first time
status: published
tags:
  - linux
---

paru is an aur helper that allows you to use a package manager to install
packages from the aur.

## What's the Aur

The Aur is a set of community managed packages that can be installed on arch based distros.

## Why a helper?

paru just makes it easy, no clone and run makepkg. You can do everything paru
can do using the built in pacman installer.

## Manual Install from the Aur

You will need to manually instal pacman from the aur in order to get started.

```bash
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
```

## Installing packages with paru

Once setup you are ready to install packages from the AUR just like the core repos.

```
# you can update your system using paru
paru -Syu

# you can install packages from the AUR
paru -S tailscale
paru -S prismlauncher

# even core repo packages can be installed
paru -S docker
```

## Paru in Docker

Here is a snippet from my devtainer
[dockerfile](https://github.com/WaylonWalker/devtainer/blob/main/Dockerfile).
Where I use paru to install packages from the AUR inside of a dockerfile.

```bash
FROM archlinux

RUN echo '[multilib]' >> /etc/pacman.conf && \
    echo 'Include = /etc/pacman.d/mirrorlist' >> /etc/pacman.conf && \
    pacman --noconfirm -Syyu && \
    pacman --noconfirm -S base-devel git && \
    groupadd --gid 1000 devtainer && \
    useradd --uid 1000 --gid 1000 -m -r -s /bin/bash devtainer && \
    passwd -d devtainer && \
    echo 'devtainer ALL=(ALL) ALL' > /etc/sudoers.d/devtainer && \
    mkdir -p /home/devtainer/.gnupg && \
    echo 'standard-resolver' > /home/devtainer/.gnupg/dirmngr.conf && \
    chown -R devtainer:devtainer /home/devtainer && \
    mkdir /build && \
    chown -R devtainer:devtainer /build && \
    cd /build && \
    sudo -u devtainer git clone --depth 1 https://aur.archlinux.org/paru.git && \
    cd paru && \
    sudo -u devtainer makepkg --noconfirm -si && \
    sed -i 's/#RemoveMake/RemoveMake/g' /etc/paru.conf && \
    pacman -Qtdq | xargs -r pacman --noconfirm -Rcns && \
    rm -rf /home/devtainer/.cache && \
    rm -rf /build

USER devtainer
RUN sudo -u devtainer paru --noconfirm --skipreview --useask -S \
    bat \
    cargo \
    direnv \
    dua-cli \
    dust \
    fd

```

## Final Thoughts

There are other options out there, paru seemed to be the most supported at the
time I started using arch and there has been no other reason for me to change
it. It's treated me well for nearly a year now.
