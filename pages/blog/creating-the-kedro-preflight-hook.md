---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: creating the kedro-preflight hook
date: 2020-05-10T07:12:00.000+00:00
status: published
description: Kedro Hooks Intro - kedro hooks are an exciting upcoming feature of kedro
  `0.16.0`.  They allow you to hook into `catalog_created`,`pipeline_run`, and `node_run`(nouns).
  With a `before`, or `after` (adjective).  This really reminds me of reacts lifecycle
  hooks, that let you hook into various state of react web components.  This is going
  to make kedro so extendable by the community.  I am super pumped to see what the
  community is able to do with this ability.
cover: "/static/kedro-hooks.png"

---
kedro hooks are an exciting upcoming feature of kedro `0.16.0`.  They allow you to hook into `catalog_created`,`pipeline_run`, and `node_run`(nouns). With a `before`, or `after` (adjective).  This really reminds me of reacts lifecycle hooks, that let you hook into various state of react web components.  This is going to make kedro so extendable by the community.  I am super pumped to see what the community is able to do with this ability.


https://waylonwalker.com/what-is-kedro

> If you are completely unsure what kedro is be sure to check out my what is kedro post

## Docs
_a work in progress_

As this is a part of an upcoming release you will need to look in the `latest` docs, **not** `stable` and you will find a [15_hoooks](https://kedro.readthedocs.io/en/latest/04_user_guide/15_hooks.html?highlight=hooks) page.  As these docs are still in development they are not very complete at this point and do require a bit more existing `kedro` knowledge to understand.  I am sure they will get much better as we approach the realease of hooks.

> This doesn't mean that we can't still install the latest/unstable version and have some fun learning!

## Installation
_Straight from GitHub_

As this is part of an upcoming release you will need to get the library straight from github.  Since this is not a stable release of `kedro` I cannot express the importance of using a virtual environment enough.  Trying to install this version in the same place that you are trying to develop a pipeline potentially break your existing working development environment.

``` bash
conda create -n kedro0160 -y
conda activate kedro0160 # may also be source activate kedro0160 or activate kedro0160
pip install git+https://github.com/quantumblacklabs/kedro.git
pip install colorama
```

> **note** the version is still somewhere between `0.15.9` and `0,16.0`.  `kedro.__version__` will still be `0.15.9` and wiill not roll until the official release.

## Create a sample project

> ### Kedro new
> For more details check out my full post on [kedro new](https://waylonwalker.com/knew)

For this post I really just want a working pipeline as fast as possible.  For this I am going to use iris pipeline that is generated from the `kedro new` command in the cli.  It's **important** that you answer `y` to create an example pipeline.

> ### Hold On ✋
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
 [New Kedro Project]: Kedro Hooks
Repository Name:
================
Please enter a directory name for your new project repository.
Alphanumeric characters, hyphens and underscores are allowed.
Lowercase is recommended.
 [kedro-hooks]:
Python Package Name:
====================
Please enter a valid Python package name for your project package.
Alphanumeric characters and underscores are allowed.
Lowercase is recommended. Package name must start with a letter or underscore.
 [kedro_hooks]:
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

Before we start developing any hooks lets make sure everything is setup correctly by running the pipeline with `kedro run`.

``` bash
kedro run
```
## Let's make a hook

_getting to the meat of the post_

Now that we have a project scaffolded up and running we can develop a hook for it.  As far as I can tell hooks can be implemented one of **two ways**.  As a **function** inside of a module, then import that module and pass it into the hooks list, or implemented as a method on a **class**, then the class is passed into the hooks list.  Either method must follow the naming convention with the `@hook_impl` decorator.  Each module/class can implement more than one hook, but not more than one of the same type. One of each kind will be created below.

### Full list of hooks available

> `before_catalog_created`
>
> `after_catalog_created`
>
> `before_pipeline_run`
>
> `after_pipeline_run`
>
> `before_node_run`
>
> `after_node_run`

## debug_hook (class)
_quick and dirty_


I highly recommend this as your first hook.  It's super easy to make and lets you explore the arguments passed into the hook.  For this one I am going to pop the following class right into `kedro-hooks/src/kedro-hooks/run.py`, remember that I chose `kedro-hooks` as my project name.  Your path might be slightly different.  If you wanted to make a real hook it might make sense to put it in its own module, but for simplicity of your first hook you can put it directly in the same module that it gets implemented.

``` python
class debug_hook:
    @hook_impl
    def before_pipeline_run(run_params, pipeline, catalog):
        "pops into a debugger before pipeline run"
        print('I hooked in right before the pipeline run')
        breakpoint()
```


It is really that easy to create a kedro hook!  Now lets apply it to our project.  All we need to do is add one line (`hooks = [debug_hook]`) to the existing `ProjectContext` class within `kedro-hooks/src/kedro-hooks/run.py`.  Once we do that our `ProjectContext` will look like this.

``` python
class ProjectContext(KedroContext):
    """Users can override the remaining methods from the parent class here,
    or create new ones (e.g. as required by plugins)
    """

    project_name = "kedro-hooks"
    # `project_version` is the version of kedro used to generate the project
    project_version = "0.15.9"
    package_name = "kedro-hooks"

    hooks = [ debug_hook ] # 👈 This is where you implement the hook

    def _get_pipelines(self) -> Dict[str, Pipeline]:
        return create_pipelines()
```

Run it!  While you are in the debugger, explore what the `run_params`, `pipeine`, and `catalog` arguments give you.  This will give you some insight to what to expect when creating your next hook.


## preflight hook (module)
_giving it a bit more flair_

Create a new file `kedro-hooks/src/kedro-hooks/preflight.py` and place the following content into the file.  This will raise a `DataSetNotFoundError` before wasting time running any of the pipeline.  This could be useful to save some developer time for long running pipelines by warning them that they don't have all of the raw data they need before running.


``` python
# kedro-hooks/src/kedro-hooks/preflight.py
from kedro.hooks import hook_impl
from kedro.io.core import DataSetNotFoundError
from colorama import Fore
import textwrap


@hook_impl
def before_pipeline_run(run_params, pipeline, catalog):
    missing_input = [i for i in pipeline.inputs() if not getattr(catalog.datasets, i)._exists()]
    if len(missing_input) != 0:
        raise DataSetNotFoundError(textwrap.dedent(f'''

    {Fore.LIGHTBLACK_EX}――――――――  {Fore.RED}PREFLIGHT ERROR {Fore.LIGHTBLACK_EX}―――――――――
    {Fore.RESET} preflight of pipeline failed due to {Fore.YELLOW}missing datasets
    {Fore.BLUE} {missing_input}{Fore.RESET}
    '''))
```

Once we are happy with this hook, it can live anywhere.  It can be a module inside our project.  It can be a separate libarary that gets handed out as a back ally wheel, or we can even publish it as its own package to pypi so that anyone can easily pip install it.

### One Step Back
_a bit of explanation of preflight_

If you are not familiar, `pipeline.inputs()` gives us all of the edge inputs into the pipeline.  kedro does also have a `pipeline.all_inputs()` that tells us all of the edge and internal pipeline inputs that will be called throughout the pipeline run.  For this hook we are just concerned with the edge inputs as internal inputs will be generated during the run.

Also each one of the kedro datasets have an `_exists()` method attached to them to check if the dataset exists or not.  For a more robust implementation of `preflight` it would probably be best to ignore `AttributeError`s, i.e the dataset type does not have an implementation of `_exists`.  It would probably also be a good idea to filter for types such as `SQLQueryDataSet`s that assume `_exists` is False by default.

##  Ideas

Now that the juices are flowing what ideas do you have for `kedro` hooks?
