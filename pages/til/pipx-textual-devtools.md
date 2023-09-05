---
date: 2022-10-24 08:16:33
templateKey: til
title: pipx textual devtools
published: true
tags:
  - python

---

I really like having global cli command installed with pipx.  Since textual
`0.2.x` (the css release) is out I want to be able to pop into textual devtools
easily from anywhere.

!["rusting tape machine robot, cinematic lighting, detailed, cell shaded, 4 k, warm colours, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality" -s50 -W832 -H416 -C12.0 -Ak_lms -S2404332231](https://stable-diffusion.waylonwalker.com/000359.2404332231.webp)

## Pipx Install

You can pipx install textual.

``` bash
pipx install textual
```

But if you try to run any textual cli commands you will run into a
`ModuleNotFoundError`, because you need to install the optional `dev`
dependencies.

``` python
Traceback (most recent call last):
  File "/home/u_walkews/.local/bin/textual", line 5, in <module>
    from textual.cli.cli import run
  File "/home/u_walkews/.local/pipx/venvs/textual/lib/python3.10/site-packages/textual/cli/cli.py", line 4, in <module>
    import click
ModuleNotFoundError: No module named 'click'
```

## Pipx Inject

In order to install optional dependencies with `pipx` you need to first install
the library, then inject in the optional dependencies using the square bracket
syntax.

``` bash
pipx install textual
pipx inject textual 'textual[dev]'
```
