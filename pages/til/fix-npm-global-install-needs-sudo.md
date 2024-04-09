---
date: 2024-04-11 13:28:17
templateKey: til
title: fix npm global install needs sudo
published: true
tags:
  - webdev

---

Each time I go to set up npm I am frustrated by the errors saying that I don't
have permission to `npm i -g <package>`, and it's frustrating.  And I forget
what I need to do to tell npm to install packages in a directory I own, and my
shell to look there so that I can use the executables.

``` bash
mkdir ~/.npm-global
export NPM_CONFIG_PREFIX=~/.npm-global
export PATH=$PATH:~/.npm-global/bin
```

For the fix to remain persistent you need to put these two lines in your shell
profile like `~/.bashrc` or `~/.zshrc`.

``` bash
export NPM_CONFIG_PREFIX=~/.npm-global
export PATH=$PATH:~/.npm-global/bin
```
