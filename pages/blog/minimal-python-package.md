---
templateKey: blog-post
tags: ['python']
title: Minimal Python Package
date: 2021-01-10T00:00:00
status: published

---

What does it take to create an installable python package that can be hosted on pypi?


## What is the minimal python package

* setup.py
* my_module.py


This post is somewhat inspired by the bottle framework, which is famously created as a single python module.  Yes, a whole web framework is written in one file.

## Directory structure

``` bash

.
├── setup.py
└── my_pipeline.py
```


## setup.py

``` python
from setuptools import setup

setup(
    name="",
    version="0.1.0",
    py_modules=["my_pipeline", ],
    install_requires=["kedro"],
)
```

## name

The name of the package can contain any letters, numbers, "_", or "-".  Even if it's for internal/personal consumption only I usually check for discrepancy with pypi so that you don't run into conflicts. 

> Note that pypi treats "-" and "_" as the same thing, beware of name clashes

## version

This is the version number of your package.  Most packages follow
[semver](semver.org).  At a high level its three numbers separated by a `.` that follow the format `major.minor.patch`.  It's a common courtesy to only break APIs on major changes, new releases on minor, and fixes on patch.  This can become much more blurry in practice so checkout [semver.org](https://semver.org/).

## py_modules

Typically most packages use the `packages` argument combined with
`find_packages`, but for this minimal package, we are only creating one `.py` file.

## Using packages instead

``` python
from setuptools import setup, find_packages

setup(
    name="",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["kedro"],
)
```


## install_requires
These are your external dependencies that come from pypi.  They go in this list but are often pulled in from a file called `requirements.txt`.  Other developers may look for this file and want to do a `pip install -r
requirements.txt`.

## Clean?

One thing to be careful of here is that everything sits at the top level API, when you users import your module and hit tab they are going to see a lot of stuff unless you hide all of your internal functions behind an `_`.

## Minimal

Can you create a python package with less than two files and less than 8 lines? Should you?  I really like a minimal point to get started from for quick and simple prototypes.  You can always pull a more complicated `cookiecutter` template later if the project is successful.
