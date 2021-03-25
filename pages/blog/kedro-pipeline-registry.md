---
templateKey: blog-post
tags: ['kedro', 'python']
title: Kedro pipeline_registry.py
date: 2021-03-20T00:00:00 
status: published

---

With the realease of `kedro==0.17.2` came a new module in the project template
`pipeline_registry.py`.  Here are some notes that I learned while playing with
this new module.

## migrating to `pipeline_registry.py`


* create a `src/<package-name>/pipeline_registry.py` file create a
* `register_pipelines` function in `pipeline_registry.py` that mirrors the
* register_pipelines method from your `hooks.py` module do not bring the
* `hook_impl` decorator remove register_pipelines method on your `ProjectHooks`
* class

You should now have something that looks like this in your
`src/<package-name>/pipeline_registry.py`.

``` python 
"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns: A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {"__default__": Pipeline([])}
```


> pipeline_registry only works in `kedro>=0.17.2`

## Conflict Resolution

_What happens If I register pipelines in both places_

I was not able to find any official documentation on how conflict resolution
worked so I stepped into a project and added to both my `hooks.py` and
`pipeline_registry.py` file.  I noticed that it would pick up pipelines from
both modules, but pipelines from `hooks.py` always take precedence.  The entire
duplicate pipeline will be over written by the one from `hooks.py`.

>  kedro automatically merges pipelines from both hooks.py takes precedence

## Ready to update

In my experience there were no issues upgrading from `0.17.1` to `0.17.2`.  I
would reccomend only having one `register_pipelines` so decide to migrate to
the new `pipeline_registry.py` or keep it in your `hooks.py`, but both is only
going to lead to confusion.
