---
date: 2022-02-18 16:17:26.075533
templateKey: til
title: Run glances without install with pipx
tags:
  - python

---

Glances is a fully featured system monitoring tool written in python.  Out of
the box it's quite similar to htop, but has quite a few more features, and can
be ran without installing anything other than `pipx`, which you should already
have installed if you do anything with python.

``` bash
pipx run glances
```

Once you run this you will be in a tui application similar to htop.  You can
kill processes with k, use left and right arrows to change the sorting column,
and up and down to select different processes.

![running pipx run glances on my ubuntu 21.10 machine inside the kitty terminal](https://images.waylonwalker.com/pipx-run-glances.png)

## Links

* [pipx](https://pipx.pypa.io/stable/)
* [website](https://nicolargo.github.io/glances/)
* [docs](https://glances.readthedocs.io/en/latest/index.html)
* [github](https://github.com/nicolargo/glances)
