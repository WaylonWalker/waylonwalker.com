---
date: 2025-01-12 21:14:19
templateKey: blog-post
title: nvim-manager
tags:
  - vim
  - nvim
  - linux
  - python
published: True

---

I recently built a cli application as a nearly-one-shot-app called
[nvim-manager](https://github.com/waylonwalker/nvim-manager). It manages your
nvim dotfiles install.

![screenshot-2025-01-31T21-21-40-707Z.png](https://dropper.waylonwalker.com/api/file/20f800f1-64a6-43a3-93eb-e805b07d86b1.png){.more-cinematic}

## Why

{.chat-left}
Don't we have stow?

{.chat-right}
Ya, thats not enough.

{.chat-left}
Why not??

{.chat-right}
Inevitably shit goes sideways and I break my vim install.

## How is nvim manager any better

nvim-manager allows you to install pinned versions of your dotfiles, your
friends dotfiles, and distros in ~/.config.  This allows you to have stable
versions that will not break installed while you change things.

I'm sure most of us have experienced the pain of installing one plugin, only to
update all of your plugins and break something.

Or, you have small changes on every machine you use, because they are all just
a bit different and now you have big merge conflicts to deal with.

All of this aside you can install a distro to get you by, or a known working
version of your own dotfiles.

## So all these versions in ~/.config

ya, thats the magic of `NVIM_APPNAME`, I can boot up any of these intalled
working versions in an instant with `NVIM_APPNAME=nvim-waylonwalker-v0.0.1
nvim`.  I can still cowboy up and break my main install, but as long as I am
diligent to keep these installs untouched I will always have a version to fall
back to in that moment of need.

## So what do I need to do?

1. start tagging your dotfiles as you hit stable versions
1. Install `curl https://i.jpillora.com/waylonwalker/nvim-manager | bash`
1. Add some env variables to your shell startup (~/.bashrc or ~/.zshrc for example)
1. Install that pinned version of your dotfiles `nvim-manager install v0.0.1`
1. Install a distro `nvim-manager install --distro astronvim`

Here are those environment variables I was talking about, set them to use your
dotfiles repo, name it what you like, and set your NVIM_APPNAME if you want to
default to a stable `nvim` and force yourself to `unset NVIM_APPNAME` to live
on the edge.

## Install nvim-manager

``` bash
apt install curl git unzip
curl https://i.jpillora.com/MordechaiHadad/bob | bash
bob install nightly
bob use nightly
ln -s ~/.local/share/bob/nvim-bin/nvim ~/.local/bin
curl https://i.jpillora.com/waylonwalker/nvim-manager | bash
```

## Install your own dotfiles

Setup with the following environment variables.

``` bash
# nvim-manager
export NVIM_MANAGER_REPO=https://github.com/WaylonWalker/devtainer
export NVIM_CONFIG_PATH=nvim/.config/nvim
export NVIM_MANAGER_INSTALL_DIR=$HOME/.config
export NVIM_MANAGER_PREFIX="nvim-waylonwalker"
export NVIM_APPNAME=${NVIM_MANAGER_PREFIX}-v0.0.1
```

``` bash
nvim-manager install v0.0.1
nvim
```

> Note I like installer by jpillora, I self host it for my own security, but
> feel free to download from GH if it makes you feel safer.

## Ubuntu Container Speedrun

Here is a speedrun to getting nvim up and running in an ubuntu container.

``` bash
set -euxo
mkdir -p ~/.local/bin
export PATH=$PATH:~/.local/bin
apt update
apt install curl git unzip -y
curl -LsSf https://astral.sh/uv/install.sh | sh
curl https://i.jpillora.com/MordechaiHadad/bob | bash
mv bob ~/.local/bin
bob install nightly
bob use nightly
ln -s ~/.local/share/bob/nvim-bin/nvim ~/.local/bin
curl https://i.jpillora.com/waylonwalker/nvim-manager | bash
mv nvim-manager ~/.local/bin
export NVIM_MANAGER_REPO=https://github.com/WaylonWalker/devtainer
export NVIM_CONFIG_PATH=nvim/.config/nvim
export NVIM_MANAGER_INSTALL_DIR=$HOME/.config
export NVIM_MANAGER_PREFIX="nvim-waylonwalker"
export NVIM_APPNAME=${NVIM_MANAGER_PREFIX}-v0.0.1
nvim-manager install v0.0.1
nvim-manager install --distro lazyvim
nvim-manager install --distro astronvim
nvim-manager install --distro nvchad
nvim-manager install --distro kickstart
nvim-manager install --distro lunarvim

# plugins like treesiter need gcc and make
apt install gcc make -y
export TZ="America/Chicago"
export DEBIAN_FRONTEND=noninteractive
apt update
apt install tzdata -y
ln -fs /usr/share/zoneinfo/$TZ /etc/localtime
dpkg-reconfigure -f noninteractive tzdata
# Some of the mason installs need npm
apt install nodejs npm -y
# plugins like telescope require ripgrep
apt install fzf ripgrep -y
```

## Give it a Star

I'd appreciate a star if you find this app useful.

<https://github.com/waylonwalker/nvim-manager>
