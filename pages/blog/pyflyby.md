---
templateKey: blog-post
tags: ['python',]
title: Develop Python Faster with automatic imports with pyflyby
date: 2021-12-04T11:34:47
status: Draft

---

This is not a flaky works half the time kind of plugin, its a seriously smooth
editiing experience.  I've just started using pyflyby and it is solid so far.
I have automatic imports on every save of a python file in neovim, and
automatic imports on every command in ipython.

## installation

```
pip install flybypy
```

## configuration setup with stow

If you're going to configure any of your tools the first thing you should do is
set it up with stow, seriously dont sleep on the stow.  If you don't have stow
installed or choose not to use stow you can skip this part.

```
cd ~/dotfiles
mkdir ipython
touch ipython/.pyflyby
stow ipython
```

## How to Configure pyflyby

`pyflyby` is configured simply by putting all of your import statements that you
want to automatically import into your `~/.pyflyby` file.  You can `import
pandas`, `from pandas import DataFrame`, or even `import pandas as pd`, and all
of these will work pretty much as expected.

``` python
# comments start with a #
# import your favorite libraries
import visidata as vd
import fsspec
import difflib
import s3fs
import seaborn as sns
import plotly


# also supports from imports
from rich.layout import Layout
from rich.live import Live

# duplicates are allowed
import plotly
import plotly

# duplicate names from different libraries are not allowed
import copy
from numpy import copy

```

## Commas are even supported

This following example will setup auto import for both DataFrame and Series,
they will both work separately.

``` python
from pandas import DataFrame, Series
```

> Even imports with a comma will be treated separately.

## installing flybypy

`flybypy` is hosted on pypi so you can install it using the pip command on any
machine that has python already installed.

``` bash
pip istall flybypy
```

## jupyter note!

I only really mention ipython here, but the same all applies to jupyter as
well.  I just really like ipython itself, c'mon its right there in the terminal
integrating with the rest of your terminal experience so well.


## ipython setup
_Automatically import python libraries in ipython with pyflyby_

The recommended way to setup `flybypy` from the docs is to run the following magic command


``` python
%load_ext flybypy
```

## ipython setup next level
_automatically import modules in python **without %load_ext**_

``` python
from IPython import get_ipython
import subprocess


ipython = get_ipython()

try:
    ipython.magic("load_ext pyflyby")
except ModuleNotFoundError:
    print("installing pyflyby")
    subprocess.Popen(
        ["pip", "install", "pyflyby"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).wait()
    ipython.magic("load_ext pyflyby")
```

## ipython auto import examples

``` python
df = pd.read_csv("https://waylonwalker.com/cars.csv")
[PYFLYBY] import pandas as pd
```

## Getting Help

```
Popen?
```

## Autocomplete
_This is next level python auto-import_

```
Pop<tab>
requests.<tab>
```


## What happens when a module is not installed

``` python
❯ pd?
[PYFLYBY] import pandas as pd
[PYFLYBY] Error attempting to 'import pandas as pd': ModuleNotFoundError: No module named 'pandas'
[PYFLYBY] Traceback (most recent call last):
[PYFLYBY]   File "/home/u_walkews/.local/lib/python3.8/site-packages/pyflyby/_autoimp.py", line 1610, in _try_import
[PYFLYBY]     exec_(stmt, scratch_namespace)
[PYFLYBY]   File "<string>", line 1, in <module>
[PYFLYBY] ModuleNotFoundError: No module named 'pandas'
Object `pd` not found.

❯ df = pd.read_csv("https://waylonwalker.com/cars.csv")
╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
│ <ipython-input-3-69b040434562>:1 in <module>                                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
NameError: name 'pd' is not defined

```



## nvim pyflyby setup
_automatically importing python modules in vim, neovim, nvim_


``` vim
function! s:PyPreSave()
    Black
endfunction

function! s:PyPostSave()
    execute "silent !tidy-imports --black --quiet --replace-star-imports --action REPLACE " . bufname("%")
    execute "e"
endfunction

:command! PyPreSave :call s:PyPreSave()
:command! PyPostSave :call s:PyPostSave()

augroup waylonwalker
    autocmd!
    autocmd bufwritepre *.py execute 'PyPreSave'
    autocmd bufwritepost *.py execute 'PyPostSave'
    autocmd bufwritepost .tmux.conf execute ':!tmux source-file %'
    autocmd bufwritepost .tmux.local.conf execute ':!tmux source-file %'
    autocmd bufwritepost *.vim execute ':source %'
augroup end
```
