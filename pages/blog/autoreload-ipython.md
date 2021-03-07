---
templateKey: blog-post
title: Autoreload in Ipython
date: 2019-09-08T05:00:00.000+00:00
status: published
description: Autoreload in python
cover: "/static/autoreload-ipython.png"
related_post:
# - src/pages/blog/readme_tables.md
tags:
- python

---
# Autoreload in Ipython

I have used `%autoreload` for several years now with great success and 🔥 rapid reloads.  It allows me to move super fast when developing libraries and modules.  They have made some great updates this year that allows class modules to be automatically be updated.

## What I like about autoreload

🔥 Blazing Fast

💥 Keeps me in the comfort of my text editor

👏 Allows me to use Jupyter when I need

👟 Extremely Reliable

One of the biggest benefits that I find is that it shortens the distance between my module/library code and test code inside of a terminal/notebook.  Now I primarily use jupyter notebooks for the presentation aspect.  I develop code from the comfort of my editor with all of the tools I have setup, and run the functions in a notebook to get the output.  From there I might do some aggregations or plots, but the 🥩 meat of development is done outside of jupyter.

> Now I primarily use jupyter notebooks for the presentation aspect.

## Enabling Autoreload

📐 _config_

This is a short script that I use to setup ipython so that it automatically reloads modules.  This allows me to use a separate terminal and editor, and keep data in memory while developing functions.

```bash
ipython profile create
```

Then edit the created file `~/.ipython/profile_default/ipython_config.py`.

```python
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
c.InteractiveShellApp.exec_lines.append('print("Warning: disable autoreload in ipython_config.py to improve performance.")')
```

## According to the docs

[autoreload caveates](https://ipython.org/ipython-doc/3/config/extensions/autoreload.html#caveats "IPython caveats")

> Some of the known remaining caveats are:
>
> Replacing code objects does not always succeed: changing a @property in a class to an ordinary method or a method to a member variable can cause problems (but in old objects only).
> Functions that are removed (eg. via monkey-patching) from a module before it is reloaded are not upgraded.
> C extension modules cannot be reloaded, and so cannot be autoreloaded.

## So what can gets updated??

🤲 _Nearly everything..._

* new/updated functions
* new/updated functions
* new/updated class methods
* new/updated class attributes

## What does not get updated

🔄 _needs restart_

**config** files that are side loaded with modules typically do not get updated in my experience, and I tend to restart the session.

**init** class methods do not get reran, but the session does not need to be reloaded.  The class instance will just need to be re-instanciated.

## Testing out the capabilities

💨 _Watch_ it go

Here is a gif of me taking autoreload out for a test drive.  When creating the session test_autoreload.py does not even exist. From there new functions, classes, attributes, and methods are added in the file and all live reload into ipython.

![](/test_autoreload4.gif)
_for more gifs like these follow me on twitter_ [_@waylonwalker_](https://twitter.com/_WaylonWalker)

## What About Jupyter Notebooks????

💥 _Exactly the Same_

Since jupyter uses ipython in be background Jupyter will use the same `ipython_config.py` file to have autoreload enabled by default.

![](/test_autoreload_jupyter.gif)
_for more gifs like these follow me on twitter_ [_@waylonwalker_](https://twitter.com/_WaylonWalker)

## Go use it now

Take the splash into rapid development of python functions with minimal distance between your modules/library and your ipython/jupyter session.
