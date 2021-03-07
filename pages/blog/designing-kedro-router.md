---
templateKey: blog-post
related_post_label: Check out this related post
tags: ['python']
title: Designing a "Router" for kedro
date: 2020-10-08T05:00:00Z
status: published
description: I released a router-like plugin for kedro back in April 2020.
    This was not the first design, the idea actually came from one of the QB
    folks who taught me kedro nearly a year before.
cover: "/static/designing-kedro-router.png"

---

## nodes_global

I released a router-like plugin for kedro back in April 2020.  This was not the first design, the idea actually came from one of the QB folks who taught me kedro nearly a year before.  We were assembling our pipelines with something called `nodes_global`.  It worked fairly well but did have some issues around being set as a global variable.

_But..._

One thing in particular that it did not lend itself well to was being able to create a packagable pipeline that I could pip install and append into any of my existing pipelines.  Something I am still trying to work out, maybe I don't need this.  I think I have it working for our internal pipelines and it seems like the way to go, but we don't necessarily end up using it.

_Also..._

With this pattern all of the nodes needed to be importable by the module containing nodes_global.  I find that this becomes a big hurdle for new pipelines coming from jupyter to overcome and can be most infuriating when their nodes aren't getting ran after they added them.

<p style='text-align: center' align='center'>
<a href='https://waylonwalker.com/what-is-kedro'>
  <img
    style='width:400px; max-width:80%; margin: auto;'
    src="https://images.waylonwalker.com/what-is-kedro.png"
    alt="What is kedro"
    width='400'
  />
  </a>
</p>

> If you are a bit unsure about what kedro is make sure to check out my [what-is-kedro](https://waylonwalker.com/what-is-kedro) article.


## @node(inputs='a_raw_cars', outputs='b_int_cars')
I set off to design something that was flask-like.  Around November I had something working.  You could simply start creating functions. and decorate these functions with a decorator just like with flask.  I even had it setup to autoname the nodes things like `create_b_int_cars`.

_But...._

This did not lend well to pulling in functions from a library or dynamically creating nodes.  I didn't realize how few nodes I actually make in my pipelines that are a 1:1 relationship between the node and function in real work.  Most examples work this way, but for some reason when I step into a project we end up pulling a lot of functions out of existing libraries, or dynamically creating many datasets from a list of options.

## pytest inspired
_simplicity_

The final design ended up being suggested by a colleague of mine who is not using kedro, but is a  brilliant python dev.  The idea was to walk through the project like pytest does looking for modules and variables with a certain pattern (`node`, or `pipeline`).

I have been using this since April and am loving it. It has have very little change since first release.  When I create a new module, that automatically becomes a new pipeline in my `pipelines` dict and all of the variables with the name node get scrapped up and put into a single pipeline.

_Beginner Friendly_

Just like with pytest.  You just start hacking in modules ending with `_nodes.py` with nodes in them and they just appear in your final pipeline.

## How to use it

The [readme](https://github.com/WaylonWalker/find-kedro) has some great examples.

## Install it

``` python
pip install find-kedro
```

## Enable it

Enable it by changing one line in your run.py

_<small><mark>run.py</mark></small>_

``` python
from kedro.context import KedroContext
from find_kedro import find_kedro

class ProjectContext(KedroContext):
    def _get_pipelines(self) -> Pipeline:
        return find_kedro()
```

Or if your using the new `hooks.py` method.  Again no need to import all of your nodes.

_<small><mark>hooks.py</mark></small>_

``` python
class ProjectHooks:
    @hook_impl
    def register_pipelines(self) -> Dict[str, Pipeline]:
        """Register the project's pipeline.
        Returns:
            A mapping from a pipeline name to a ``Pipeline`` object.
        """

        return find_kedro()
```

## Use it 

Check out the [readme](https://github.com/WaylonWalker/find-kedro) for more examples, but this one is the one that I use and recommend most often.  This method helps keep nodes close to functions that are designed for them.

_<small><mark>my_nodes.py</mark></small>_

``` python
# my-proj/pipelinies/data_engineering/pipeline
from kedro.pipeline import node
from .nodes import split_data

nodes = []

def split_data(df: pd.DataFrame, ratio: float) -> Dict[str, pd.DataFrame]:
   ...

nodes.append(
    node(
        split_data,
        ["example_iris_data", "params:example_test_data_ratio"],
        dict(
            train_x="example_train_x",
            train_y="example_train_y",
            test_x="example_test_x",
            test_y="example_test_y",
        ),
    )
)
```


# Want a simple guide to get started with find kedro


<p style='text-align: center' align='center'>
<a href='https://find.kedro.dev/examples/iris/>
  <img
    style='width:400px; max-width:80%; border-radius: '35px'; margin: auto;'
    width='400'
    src="https://images.waylonwalker.com/find-kedro-examples-iris.png"
    alt="Find Kedro Iris example"
  />
  </a>
</p>

In [this doc](https://find.kedro.dev/examples/iris/) I transform the kedro iris template to find-kedro.

# Ready to start using kedro

If you still have not tried out kedro, it's easier than you think. Check out [create-new-kedro-project](https://waylonwalker.com/create-new-kedro-project) to get a project started in just a few minutes.

<p style='text-align: center' align='center'>
<a href='https://waylonwalker.com/create-new-kedro-project'>
  <img
    style='width:400px; max-width:80%; margin: auto;'
    width='400'
    src="https://images.waylonwalker.com/create-new-kedro-project.png"
    alt="Create New Kedro Project"
  />
  </a>
</p>

