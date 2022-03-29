---
date: 2022-02-20 16:25:49.548226
templateKey: til
title: Glances webui with pipx
tags:
  - python

---

## Is it a fluke?

## Site Down

``` python
Run markata build --no-pretty
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.12/x64/bin/markata", line 33, in <module>
    sys.exit(load_entry_point('markata==0.1.0', 'console_scripts', 'markata')())
  File "/opt/hostedtoolcache/Python/3.8.12/x64/bin/markata", line 25, in importlib_load_entry_point
    return next(matches).load()
  File "/opt/hostedtoolcache/Python/3.8.12/x64/lib/python3.8/importlib/metadata.py", line 77, in load
    module = import_module(match.group('module'))
  File "/opt/hostedtoolcache/Python/3.8.12/x64/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 961, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 843, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/opt/hostedtoolcache/Python/3.8.12/x64/lib/python3.8/site-packages/markata/__init__.py", line 25, in <module>
    from markata.cli.plugins import Plugins
  File "/opt/hostedtoolcache/Python/3.8.12/x64/lib/python3.8/site-packages/markata/cli/__init__.py", line 1, in <module>
    from .cli import app, cli, make_layout, run_until_keyboard_interrupt
  File "/opt/hostedtoolcache/Python/3.8.12/x64/lib/python3.8/site-packages/markata/cli/cli.py", line 3, in <module>
    import typer
  File "/opt/hostedtoolcache/Python/3.8.12/x64/lib/python3.8/site-packages/typer/__init__.py", line 12, in <module>
    from click.termui import get_terminal_size as get_terminal_size
ImportError: cannot import name 'get_terminal_size' from 'click.termui' (/opt/hostedtoolcache/Python/3.8.12/x64/lib/python3.8/site-packages/click/termui.py)
```

## Check pypi

![click 8.1.0 release date on pypi](https://images.waylonwalker.com/click-8-1-0-release-date.png)

## pin it and push


``` txt
click<8.1.0
```

## watch ci

## raise issue
