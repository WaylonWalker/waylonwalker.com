---
date: 2026-06-29 08:39:59
templateKey: til
title: fixing a corrupt zshrc
published: true
tags:
  - bash
  - zsh
  - linux

---

This morning I had a machine crash on me and came back to an error.

!!! Warning "Error"

    zsh: corrupt history file /home/u_walkews/.zsh_history

Dammit I don't want to redo my shell history, I checked with a clanker and they
came up with this solution using `strings` that only prints printable
characters.

``` bash
cp ~/.zsh_history ~/.zsh_history.bak
mv ~/.zsh_history ~/.zsh_history.corrupt
touch ~/.zsh_history
chmod 600 ~/.zsh_history
strings ~/.zsh_history.corrupt > ~/.zsh_history
chmod 600 ~/.zsh_history
```
