---
date: 2022-02-20 16:38:42.811882
templateKey: til
title: Glances can watch docker processes
tags:
  - python

---

## install

You will need to install glances to use the glances webui.  We can still use
`pipx` to manage our virtual environment for us so that we do not need to do so
manually or run the risk of globally installed package dependency hell.

``` bash
pipx install glances
pipx inject glances "glances[docker]"
```

You will be presented with this success message.

``` bash
  injected package glances into venv glances
done! ✨ 🌟 ✨
```

## results

![running glances with docker installed will show your docker processes](https://images.waylonwalker.com/glances-docker.png)


## Links

* [glances docker](https://glances.readthedocs.io/en/catest/docker.html)
* [pipx](https://pypa.github.io/pipx/)
* [website](https://nicolargo.github.io/glances/)
* [docs](https://glances.readthedocs.io/en/latest/index.html)
* [github](https://github.com/nicolargo/glances)
