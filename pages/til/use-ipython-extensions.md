---
date: 2022-09-20 15:40:31
templateKey: til
title: I've made my ipython config too complicated, let's fix it.
status: 'draft'
tags:
  - python

---

When I am developing python code I often have a repl open alongside of it
running snippets ofcode as I go.  Ipython is my repl of choice, and I hace
tricked it out the best I can and I really like it.  The problem I recently
discovered is that I have way overcomplicated it.

## What Have I done??

So in the past the way I have setup a few extensions for myself is to add
something like this to my `~/.ipython/profile_default/startup` directory.  It
sets up some things like rich highlighting or in this example automatic
imports.  I even went as far as installing some of these in the case I didn't have them installed.

``` python
import subprocess

from IPython import get_ipython
from IPython.core.error import UsageError

ipython = get_ipython()

try:
    ipython.run_line_magic("load_ext pyflyby", "inline")
except UsageError:
    print("installing pyflyby")
    subprocess.Popen(
        ["pip", "install", "pyflyby"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).wait()
    ipython.run_line_magic("load_ext pyflyby", "inline")
    print("installing isort")
    subprocess.Popen(
        ["pip", "install", "isort"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
```

## What I missed?

I missed the fact that some of these tools like `pyflyby` and `rich` already
have an ipython extension maintained by the library that just works.  It's less
complicated and more robust to future changes in the library.  If anything ever
changes with these I will not have to worry about which version is installed,
the extension will just take care of itself.

## How to activate these.

The reccomended way is to add them to your
`~/.ipython/profile_default/ipython_config.py`

``` python
c.InteractiveShellApp.extensions.append('rich')
c.InteractiveShellApp.extensions.append('markata')
c.InteractiveShellApp.extensions.append('pyflyby')
```

The issue that I found with this is that you can end up with a sea of errors
flooding your terminal.  Personally I will know immediately if ipython is
working right or not and typically have scriped venv installs so I have
everything I need, so If I don't have everything it's probably for a reason and
I don't need an error message lighting up.

My way around this was to test if the module was importable and if it had a
`load_ipython_extension` attribute before appending it as an extension.

``` python
def activate_extension(extension):
    try:
        mod = importlib.import_module(extension)
        getattr(mod, "load_ipython_extension")
        c.InteractiveShellApp.extensions.append(extension)
    except ModuleNotFoundError:
        "extension is not installed"
    except AttributeError:
        "extension does not have a 'load_ipython_extension' function"


extensions = ["rich", "markata", "pyflyby"]
for extension in extensions:
    activate_extension(extension)

```

## My Change

If you want to see what I did to my config see [this commit](https://github.com/WaylonWalker/devtainer/commit/e83b65db8cc292e0de99f1089754e088d8e7e3ef).
