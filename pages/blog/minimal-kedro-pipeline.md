---
templateKey: blog-post
tags: ['python', 'kedro', 'data']
title: Minimal Kedro Pipeline
date: 2021-01-20T00:00:00
status: published

---

How small can a minimum kedro pipeline ready to package be?  I made one within 4 files that you can pip install.  It's only a total of 35 lines of python, 8 in `setup.py` and 27 in `mini_kedro_pipeline.py`.

# Minimal Kedro Pipeline

I have everything for this post hosted in this [gihub repo](https://github.com/WaylonWalker/mini-kedro-pipeline), you can fork it, clone it, or just follow along.

## Installation

``` bash
pip install git+https://github.com/WaylonWalker/mini-kedro-pipeline
```

## Caveats

This repo represents the minimal amount of structure to build a kedro pipeline that can be shared across projects.  Its installable, and drops right into your `hooks.py` or `run.py` modules.  It is not a runnable pipeline.  At this point
I think the config loader requires to have a logging config file.

This is a sharable pipeline that can be used across many different projects.

## Usage

``` python
# hooks.py

import mini_kedro_project as mkp

class ProjectHooks:
    @hook_impl
    def register_pipelines(self) -> Dict[str, Pipeline]:
        """Register the project's pipeline.

        Returns:
            A mapping from a pipeline name to a ``Pipeline`` object.

        """

        return {"__default__": Pipeline([]), "mkp": mkp.pipeline}
```

## Implemantation

This builds on another post that I made about creating the minimal python package.  I am not sure if it should be called a package, it's a module, but what do you call it after you build it and host it on pypi?

https://waylonwalker.com/minimal-python-package/

## Directory structure

``` bash
.
├── .gitignore
├── README.md
├── setup.py
└── my_pipeline.py
```

## setup.py

This is a very minimal `setup.py`.  This is enough to get you started with a package that you can share across your team.  In practice, there is a bit more that you might want to include as your project grows.

``` python
from setuptools import setup

setup(
    name="MiniKedroPipeline",
    version="0.1.0",
    py_modules=["mini_kedro_pipeline"],
    install_requires=["kedro"],
)
```

## mini_kedro_pipeline.py

The mini kedro pipeline looks like any set of nodes in your project.  Many projects will separate nodes and functions, I prefer to keep them close together.  The default recommendation is also to have a `create_pipelines` function that returns the pipeline.

This pattern creates a singleton, if you were to reference the same pipeline in multiple places within the same running interpreter and modify the one you would run into issues.  I don't foresee myself running into this issue, but maybe as more features become available I will change my mind.

``` python
"""
An example of a minimal kedro pipeline project
"""
from kedro.pipeline import Pipeline, node

__version__ = "0.1.0"
__author__ = "Waylon S. Walker"

nodes = []


def create_data():
    "creates a dictionary of sample data"
    return {"beans": range(10)}


nodes.append(node(create_data, None, "raw_data", name="create_raw_data"))


def mult_data(data):
    "multiplies each record of each item by 100"
    return {item: [i * 100 for i in data[item]] for item in data}


nodes.append(node(mult_data, "raw_data", "mult_data", name="create_mult_data"))

pipeline = Pipeline(nodes)
```

## Share your pipelines

Go forth and share your pipelines across projects.  Let me know, do you share pipelines or catalogs across projects?
