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

## Why

{.bg-blue-900 .border-r-8 .border-black .rounded-xl .max-w-xl .p-6 .font-bold}
Don't we have stow?

{.bg-green-900 .border-l-8 .border-black .rounded-xl .max-w-xl .p-6 .ml-auto .mr-0 .font-bold}
Ya, thats not enough.

{.bg-blue-900 .border-r-8 .border-black .rounded-xl .max-w-xl .p-6 .font-bold}
Why not??

{.bg-green-900 .border-l-8 .border-black .rounded-xl .max-w-xl .p-6 .ml-auto .mr-0 .font-bold}
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

``` bash
# nvim-manager
export NVIM_MANAGER_GITHUB_REPO=https://github.com/WaylonWalker/devtainer
export NVIM_CONFIG_PATH=nvim/.config/nvim
export NVIM_MANAGER_INSTALL_DIR=$HOME/.config
export NVIM_MANAGER_PREFIX="nvim-waylonwalker-"
export NVIM_APPNAME=${NVIM_MANAGER_PREFIX}v0.0.1
```

> Note I like installer by jpillora, I self host it for my own security, but
> feel free to download from GH if it makes you feel safer.

## Give it a Star

I'd appreciate a star if you find this app useful.

<https://github.com/waylonwalker/nvim-manager>
