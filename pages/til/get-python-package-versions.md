---
date: 2022-07-29 15:48:36
templateKey: til
title: get the version of any python package | python api
status: 'draft'
tags:
  - python

---

A common meta thing that I need in python is to find the version of a package.
Most of the time I reach for `package_name.__version__`, but that does not
always work.

## but not all projects have a `__version__`

In searching the internet for an answer nearly every one of them pointed me to
`__version__`.  This works for most projects, but is simply a convention, its
not required.  Not all projects implement a `__version__`, but most do.  I've
never seen it lie to me, but there is nothing stopping someone from shipping
mismatched versions.

## If you maintain a project ship a `__version__`
_I appreciate it_

While its not required its super handy and easy for anyone to remember off the
top of their head.  It makes it easy to start debugging differences between
what you have vs what you see somewhere else. You can do this by dropping a
`__version__` variable inside your  `__init__.py` file.

```
## __init__.py
__version__ = 1.0.0
```

## SO
_stack overflow saves the day_

Special thanks to this
[Stack Overflow post](https://stackoverflow.com/questions/20180543/how-do-i-check-the-versions-of-python-modules/32965521#32965521)
for answering this question for me.

## So what do you do...
_importlib_

Your next option is to reach into the package metadata of the package that you
are interested in, and this has changed over time as highlighted in the stack
overflow post.

for Python >= 3.8:

```
from importlib.metadata import version

version('markata')
# `0.3.0.b4`
```

I only really use python >= 3.8 these days, but if you need to implement it for
an older version check out the stack overflow post.

## Another option..
_use the command line_

Another common option uses pip at the command line.

```bash
❯ pip show markata
Name: markata
Version: 0.3.0b4
Summary: Static site generator plugins all the way down.
Home-page: https://markata.dev
Author: Waylon Walker
Author-email: waylon@waylonwalker.com
License: MIT
Location: /home/waylon/git/waylonwalker.com/.venv/lib/python3.11/site-packages
Requires: anyconfig, beautifulsoup4, checksumdir, diskcache, feedgen, jinja2, more-itertools, pathspec, pillow, pluggy, pymdown-extensions, python-frontmatter, pytz, rich, textual, toml, typer
Required-by:
```

And if the package implements a command line its common to ship a version
command such as `--version` or `-V`.

``` bash
❯ markata --version
Markata CLI Version: 0.3.0.b4
```

## Why did I need to do this?

Well we have a cli tool that wraps around piptools and we wanted to include the
version of piptools in the comments that it produces dynamically.  This is why
I wanted to dynamically grab the version inside python without shelling out to
`pip show`.  Now along with the version of our internal tool you will get the
version of `piptools` even though `piptools` does not ship a `__version__`
variable.

## Fin

In the end, I am glad I learned that its so easy to use the more accurate
package metadata, but still appreciate packages shipping `__version__` for all
of us n00b's out here.
