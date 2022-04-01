---
date: 2022-04-01 16:25:49.548226
templateKey: til
title: Did my site build just go down?
tags:
  - python

---

My personal Site build went down last week, and I was unable to publish a new
article.  This is the process I went through to get it back up and running
quickly.

## Is it a fluke?

Classic IT fix, rerun it and see if you get the same error.  Everyone is busy
and when you have your build go down you are probably busy doing something
else.  My first step is often to simply click rerun right from GitHub actions.
Sometimes this will fix it, and sometimes it doesn't.  It's an easy fix to run
in the meantime you are not focused on fixing it.

## Is GitHub having issues?

Also worth a check to see if GitHub is having a hiccup or not.  This error felt
pretty obviously not GitHub's fault, but it's a good one to check when you run
into a weird unexplainable error.

Check [github status](https://www.githubstatus.com/) for any downtime issues with actions.

## Build Down

Alright down to the error message I got.  The error is pretty obvious that
somewhere I am trying to import a non-existing module from click.

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

## Check pypi's release date of click

So the latest click was released just a few hours before this build.  This
feels like we are getting somewhere.  Either click did a poor job of issuing
deprecation warnings, or I was ignoring them in my build pipeline.

![click 8.1.0 release date on pypi](https://images.waylonwalker.com/click-8-1-0-release-date.png)

## pin it and push
_let's fix this build now_

To get the build up and running today so that we don't stop the flow of new
posts I am going to open my `requirements.txt` file, and pin under the version
that was just built.

``` txt
click<8.1.0
```

Since I am still busy doing other things that fixing this, and am pretty
confident that things were working before, I am just going to commit this and
ship it.

## watch ci

Coming back to actions a few minutes later shows the site is building
successfully without the same error as before.  New posts will now be flowing
to the site with the slightly older version of click.

## looking for an issue

Let's make sure that the issue is going to be resolved. After not being busy
and having time to investigate the issue, I can see that typer is the library
making the import to `get_terminal_size`.  Lets checkout its
[GitHub-repo](https://github.com/tiangolo/typer/) and make sure someone is
working on it.

By the time I go to the package that was having this issue there was already an
[issue](https://github.com/tiangolo/typer/issues/377) up, and PR waiting
approval.  I gave the Issue a reaction 👍 to signal that I also care, and
appreciate the issue author taking time to submit.
