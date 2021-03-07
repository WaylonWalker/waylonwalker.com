---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Create Configurable Kedro Hooks
date: 2020-05-23T05:00:00.000+00:00
status: published
description: There are two main ways to create kedro hooks, with modules and classes.  Each
  one still uses the same verbiage as the function/method names.  Class hooks seem
  a bit special as they give you a way to configure them so that they are a bit more
  generally useful.
cover: "/static/configurable-kedro-hooks.png"

---
There are two main ways to create kedro hooks, with modules and classes.  Each one still uses the same verbiage as the function/method names.

Class hooks seem a bit special as they give you a way to configure them so that they are a bit more generally useful.

> ### What is Kedro 🤔
>
> If you are completely unsure what kedro is be sure to check out my [what is kedro](https://waylonwalker.com/wike) post

## Installation

.create a new environment manager of choice.  Here I will use `conda`. Then we will install `kedro` from pypi.

``` bash
conda create -n kedro_class_hooks -y
conda activate kedro_class_hooks # may also be source activate kedro_class_hooks or activate kedro_class_hooks
pip install kedro
```

## Create a sample project

> ### Kedro new
>
> For more details check out my full post on [kedro new](https://waylonwalker.com/knew)

For this post I really just want a working pipeline as fast as possible.  For this I am going to use iris pipeline that is generated from the `kedro new` command in the cli.  It's **important** that you answer `y` to create an example pipeline.

> ### Hold On ✋
>
> Did you create a separate environment for this?  Please do.

``` bash
kedro new
```

After you run the `kedro new` command it will ask a series of questions.  👇 Here is how I answered them.

``` bash
Project Name:
=============
Please enter a human readable name for your new project.
Spaces and punctuation are allowed.
 [New Kedro Project]: Kedro Class Hooks
Repository Name:
================
Please enter a directory name for your new project repository.
Alphanumeric characters, hyphens and underscores are allowed.
Lowercase is recommended.
 [kedro-class-hooks]:
Python Package Name:
====================
Please enter a valid Python package name for your project package.
Alphanumeric characters and underscores are allowed.
Lowercase is recommended. Package name must start with a letter or underscore.
 [kedro_class_hooks]:
Generate Example Pipeline:
==========================
Do you want to generate an example pipeline in your project?
Good for first-time users. (default=N)
 [y/N]: y
Change directory to the project generated in /mnt/c/temp/kedro-hooks/
A best-practice setup includes initialising git and creating a virtual environment before running `kedro install` to install project-specific dependencies. Refer to the Kedro documentation: https://kedro.readthedocs.io/
```

### Install the Project

Next install the project itself and all of its dependencies with the `kedro install` command.

``` bash
cd kedro-hooks
kedro install
```

### 🏃‍♀️ Run the pipeline

Before we start developing any hooks lets make sure everything is set up correctly by running the pipeline with `kedro run`.

``` bash
kedro run
```

## class hook without `self`

A kedro class-based hook is a class with methods using the kedro lifecycle names, decorated with `@hook_impl`, If we create a class-based kedro hook without `self` in the method calls, we simply pass the hook class itself into the hooks list. And we are off.  Kedro will call each method as it hits that point in its lifecycle.  It will pass any of the possible arguments, see arguments below.  Each method has a different set of possible arguments.  You don't need to ask for all of them, but I did here so that you could see them.

``` python
from kedro.framework.hooks import hook_impl

class debug_hook:
    """debugs all kedro hook points"""

	@staticmethod
    @hook_impl
    def before_pipeline_run(run_params, pipeline, catalog):
        "pops into a debugger before pipeline run"
        print('I hooked in right before the pipeline run')
        if self.should_before_pipeline_run:
            breakpoint()

	@staticmethod
    @hook_impl
    def after_pipeline_run(run_params, pipeline, catalog):
        "pops into a debugger after pipeline run"
        print('I hooked in right after the pipeline run')
        breakpoint()

	@staticmethod
    @hook_impl
    def on_pipeline_error(error, run_params, pipeline, catalog):
        "pops into a debugger on pipeline error"
        print('I hooked into the pipeline during an error')
        breakpoint()

	@staticmethod
    @hook_impl
    def after_catalog_created(catalog, conf_catalog, conf_creds, feed_dict, save_version, load_versions, run_id):
        "pops into a debugger after catalog created"
        print('I hooked in right after the catalog created')
        breakpoint()

	@staticmethod
    @hook_impl
    def before_node_run(node, catalog, inputs, is_async, run_id):
        "pops into a debugger before node run"
        print('I hooked in right before the node run')
        breakpoint()

	@staticmethod
    @hook_impl
    def after_node_run(node, catalog, inputs, outputs, is_async, run_id):
        "pops into a debugger after node run"
        print('I hooked in right after the node run')
        breakpoint()

	@staticmethod
    @hook_impl
    def on_node_error(error, node, catalog, inputs, is_async, run_id):
        "pops into a debugger on node error"
        print('I hooked into the node during an error')
        breakpoint()
```

#### Implement the hook object

With this version of the hook it gets added to the `ProjectContext` as the class itself, not an instance.

``` python
class ProjectContext(KedroContext):
    """Users can override the remaining methods from the parent class here,
    or create new ones (e.g. as required by plugins)
    """

    project_name = "kedro_class_hooks"
    # `project_version` is the version of kedro used to generate the project
    project_version = "0.16.1"
    package_name = "kedro_class_hooks"

    hooks = [
        debug_hook
    ]
```

## Generalizing debug_hook

If we want to generalize the debug hook and make it a bit more re-usable across all of our projects, we can include the `self` argument, on each method and a `__init__` method in which we can configure our hook.  This will make the hook configurable.  We can now create an instance of the `debug_hook` class, and tell it which lifecycle points should trigger the debugger.

``` python
""" Kedro Debug Hook module """
from kedro.framework.hooks import hook_impl

class debug_hook:
    """ Kedro Debug Hook

    Opens a debugger at any hook-able point of your kedro projects lifecycle.
    debug_hook is applied by adding it to the pipeline and setting the desired
    debug points to true.

    Examples:

        >>> hooks = [debug_hook(should_debug_all=True)]
        >>> hooks = [debug_hook(should_debug_before_pipeline_run=True)]

    Args:
        should_debug_all (bool): overrides all points Defaults to False
        should_debug_before_pipeline_run (bool): opens a debugger
            before_pipeline_run if True Defaults to False
        should_debug_after_pipeline_run (bool): opens a debugger
            after_pipeline_run if True Defaults to False
        should_debug_on_pipeline_error (bool): opens a debugger
            on_pipeline_error if True Defaults to False
        should_debug_before_node_run (bool): opens a debugger
            before_node_run if True Defaults to False
        should_debug_after_node_run (bool): opens a debugger
            after_node_run if True Defaults to False
        should_debug_on_node_error (bool): opens a debugger
            on_node_error if True Defaults to False
        should_debug_after_catalog_created (bool): opens a debugger
            after_catalog_created if True Defaults to False

    """
    def __init__(
        self,
        should_debug_all=False,
        should_debug_before_pipeline_run=False,
        should_debug_after_pipeline_run=False,
        should_debug_on_pipeline_error=False,
        should_debug_before_node_run=False,
        should_debug_after_node_run=False,
        should_debug_on_node_error=False,
        should_debug_after_catalog_created=False,
    ):
        self.should_debug_before_pipeline_run = (
            should_debug_before_pipeline_run or should_debug_all
        )
        self.should_debug_after_pipeline_run = (
            should_debug_after_pipeline_run or should_debug_all
        )
        self.should_debug_on_pipeline_error = (
            should_debug_on_pipeline_error or should_debug_all
        )
        self.should_debug_before_node_run = (
            should_debug_before_node_run or should_debug_all
        )
        self.should_debug_after_node_run = (
            should_debug_after_node_run or should_debug_all
        )
        self.should_debug_on_node_error = should_debug_on_node_error or should_debug_all
        self.should_debug_after_catalog_created = (
            should_debug_after_catalog_created or should_debug_all
        )

    @hook_impl
    def before_pipeline_run(self, run_params, pipeline, catalog):
        "pops into a debugger before pipeline run"
        if self.should_debug_before_pipeline_run:
            breakpoint()

    @hook_impl
    def after_pipeline_run(self, run_params, pipeline, catalog):
        "pops into a debugger after pipeline run"
        if self.should_debug_after_pipeline_run:
            breakpoint()

    @hook_impl
    def on_pipeline_error(self, error, run_params, pipeline, catalog):
        "pops into a debugger on pipeline error"
        if self.should_debug_on_pipeline_error:
            breakpoint()

    @hook_impl
    def after_catalog_created(
        self,
        catalog,
        conf_catalog,
        conf_creds,
        feed_dict,
        save_version,
        load_versions,
        run_id,
    ):
        "pops into a debugger after catalog created"
        if self.should_debug_after_catalog_created:
            breakpoint()

    @hook_impl
    def before_node_run(self, node, catalog, inputs, is_async, run_id):
        "pops into a debugger before node run"
        if self.should_debug_before_node_run:
            breakpoint()

    @hook_impl
    def after_node_run(self, node, catalog, inputs, outputs, is_async, run_id):
        "pops into a debugger after node run"
        if self.should_debug_after_node_run:
            breakpoint()

    @hook_impl
    def on_node_error(self, error, node, catalog, inputs, is_async, run_id):
        "pops into a debugger on node error"
        if self.should_debug_on_node_error:
            breakpoint()
```

#### implement the hook instance

When `self` is used in the method calls we must pass an instance of the `debug_hook` into the hooks list, not the class itself.

``` python
class ProjectContext(KedroContext):
    """Users can override the remaining methods from the parent class here,
    or create new ones (e.g. as required by plugins)
    """

    project_name = "kedro_class_hooks"
    # `project_version` is the version of kedro used to generate the project
    project_version = "0.16.1"
    package_name = "kedro_class_hooks"

    hooks = [debug_hook(should_debug_all=True)]
```

## Final thoughts

Hooks are an amazing addition to the kedro framework that will allow the community to make big changes to how their kedro project gets ran without needing to change kedro itself.  Using a hook class with self can make them so much more configurable, and reusable across different projects without a lot of extra code. Personally I still really like the module method that we used in [kedro-preflight](https://waylonwalker.com/creating-the-kedro-preflight-hook/).
