---
date: 2022-02-19 16:25:49.548226
templateKey: til
title: Glances webui with pipx
tags:
  - python

---

Glances has a pretty incredible webui to view system processes and information
like htop, or task manager for windows.

The nice thing about the webui is that it can be accessed from a remote system.
This would be super nice on something like a raspberry pi, or a vm running in
the cloud.  Its also less intimidating and easier to search if you are not a
terminal junky.

## install

You will need to install glances to use the glances webui.  We can still use
`pipx` to manage our virtual environment for us so that we do not need to do so
manually or run the risk of globally installed package dependency hell.

``` bash
pipx install glances
pipx inject glances "glances[web]"
```

You will be presented with this success message.

``` bash
  injected package glances into venv glances
done! ✨ 🌟 ✨
```

## running the webui

Now that you have glances installed you can run it with the `-w` flag to run
the webui.

``` bash
glances -w
```

This will present you with the following success message.

``` bash
Glances Web User Interface started on http://0.0.0.0:61208/
```

## Open it in your browser

Now that its running you can open your web browser to `localhost:61208` and be
presented with the glances webui.

![running the glances webui on my system](https://images.waylonwalker.com/glances-w.png)

## Links

* [pipx](https://pypa.github.io/pipx/)
* [website](https://nicolargo.github.io/glances/)
* [docs](https://glances.readthedocs.io/en/latest/index.html)
* [github](https://github.com/nicolargo/glances)
