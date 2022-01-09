---
date: 2022-01-10 00:33:58.860604
templateKey: til
title: 2 minutes to stow
tags:
  - linux
  - cli
  - bash

---

Stow is an incredible way to manage your dotfiles.  It works by managing
symlinks between your dotfiles directory and the rest of the system.  You can
then make your dotfiles directory a git repo and have it version controlled.  In
my honest opinion, when I was trying to get started the docs straight into deep
detail of things I frankly don't really care about and jumped right over how to
use it.

When using stow its easiest to keep your dotfiles directory (you may name it
what you want) in your home directory, with application directories inside of
it.

Then each application directory should reflet the same diretory structure as you
want in your home directory.

## zsh

Here is a simple example with my zshrc.

``` bash
mkdir ~/dotfiles
cd ~/dotfiles
mkdir zsh
mv ~/.zshrc zsh
stow --simulate zsh
```

You can pass in the --simulate if you wish, it will tell you if there are going
to be any more errors or not, but it wont give much more than that.

```
WARNING: in simulation mode so not modifying filesystem.
```

Once your ready you can stow your zsh application.

```
stow zsh
```

## nvim

A slightly more complicated example is neovim since its diretory structure does
not put configuration files directly in your home directory, but rather at a
deeper level.

``` bash
mkdir ~/dotfiles/nvim/.config/nvim/ -p
cd ~/dotfiles
mv ~/.config/nvim/ ~/dotfiles/nvim/.config/nvim/
stow zsh
```

> !notice how the nvim directory inside of dotfiles is structured like it would
> be in your $HOME directory.
