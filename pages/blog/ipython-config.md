---
templateKey: blog-post
tags: ['python']
title: Ipython-Config
date: 2020-12-20T00:00:00
status: published
description: ''
cover: "/static/ipython-config.png"

---

I use my ipython terminal daily.  It's my go to way of running python most of
the time.  After you use it for a little bit you will probably want to setup a
bit of your own configuration.


## install ipython

Activate your virtual environment of choice and pip install it.  Any time you
are running your project in a virtual environment, you will need to install
ipython inside it to access those packages from ipython.


```bash
pip install ipython
```

> You are using a virtual environment right? Virtual environments like venv or
> conda can save you a ton of pain down the road.

## profile_default

When you install ipython you start out with no config at all.  Runnign `ipython
profile create` will start a new profile called `profile_default` that contains
all of the default configuration.

```
ipython profile create
```

This command will create a directory `~/.ipython/profile_default`

## multiple configurations

You can run multiple configurations by naming them with `ipython profile create
[profile_name]` This command will create a directory
`~/.ipython/[profile_name]`

```
ipython profile create my_profile
ipython --profile=my-profile
```

## startup

Inside the profile there will be a startup directory
`~/.ipython/profile_default/startup`.  Ipython will execute each of the files
in this directory on startup.  This is particularly handy to create custom
prompts, search, or import packages automatically for certian profiles.


https://waylonwalker.com/custom-ipython-prompt

> This post creates a custom ipython prompt by creating a
> `~/.ipython/profile_default/startup/prompt.py` file.

## ipython_config.py


There are tons of options that are in the `ipython_config.py` file.  My
favorite is to automatically enable my favorite magic command autoreload.

https://waylonwalker.com/autoreload-ipython

``` python
c.InteractiveShellApp.extensions = ['autoreload'
c.InteractiveShellApp.exec_lines = []'%autoreload 2']
c.InteractiveShellApp.exec_lines.append('print("Warning: disable autoreload in ipython_config.py to improve performance.")')
```
