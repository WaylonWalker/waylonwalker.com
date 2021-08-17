---
templateKey: blog-post
tags: ['kedro', 'python']
title: Kedro New
date: 2021-08-18T20:40:45
status: published

---

https://youtu.be/uqiv5LAiJe0

Kedro new is simply a wrapper around the cookiecutter templating library.  The
kedro team maintains a ready made template that has everything you need for a
kedro project.  They also maintain a few kedro starters, which are very similar
to the base template.

https://waylonwalker.com/what-is-kedro/

> Unsure what kedro is, Check out yesterdays post on What is Kedro.

## pipx

I reccomend using `pipx` when running kedro new.  `pipx` is designed for system
level cli tools so that you do not need to maintain a virtual environment or
worry about version conflicts, `pipx` manages the environment for you.

The kedro team does not reccomend `pipx` in their docs as they already feel
like there is a bit of a tool overload for folks that may be less familiar with

``` python
pipx kedro new
```

I like using `pipx` as it gives you better control over using a specific
version or always the latest version, unlike when you run what you have on your
system depends on when you last installed or upgraded.

## Kedro New

The kedro team also has a set of starters, by passing in `--starter` you can
start with a different template.  Here is an example with the kedro
spaceflights starter.

``` bash
pipx run kedro new --starter spaceflights

=============
Please enter a human readable name for your new project.
Spaces and punctuation are allowed.
 [New Kedro Project]: Spaceflights Complete

Repository Name:
================
Please enter a directory name for your new project repository.
Alphanumeric characters, hyphens and underscores are allowed.
Lowercase is recommended.
 [spaceflights-complete]:

Python Package Name:
====================
Please enter a valid Python package name for your project package.
Alphanumeric characters and underscores are allowed.
Lowercase is recommended. Package name must start with a letter
or underscore.
 [spaceflights_complete]:

Change directory to the project generated in /home/u_walkews/git/spaceflights-complete

A best-practice setup includes initialising git and creating a virtual environment before running ``kedro install`` to install project-specific dependencies. Refer to the Kedro documentation: https://kedro.readthedocs.io/
```

### Other versions of kedro with pipx

`pipx` not only ensures that you run  the latest version, it can also run a
very specific version.

``` bash
pipx run --spec kedro==0.16.6 kedro new
```

https://waylonwalker.com/kedro-environment/

> The next post in this series will help you create your virtual environment for your new kedro project.
