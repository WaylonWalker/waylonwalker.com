---
title: '💭 python script is not found'
date: 2023-07-28T14:59:37
template: link
link: None
tags:
  - python
  - thoughts
  - thought
  - link
published: true

---

![[None]]

When setting up a new machine, vm, docker image you might be installing command line tools from places like pip.  They will often put executables in your `~/.local/bin` directory, but by default your shell is not looking in that directory for commands.

``` bash
  WARNING: The script dotenv is installed in '/home/falcon/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

To solve this you need to add that directory to your $PATH.


``` bash
export PATH=$PATH:~/.local/bin
```

To make this change permanant add this line to your shell's init script, which is likely something like `~/.bashrc` or `~/.zshrc`.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
