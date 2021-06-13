---
templateKey: blog-post
tags: ['kedro', 'python']
title: Comprehensive guide to creating kedro nodes
date: 2021-06-03T21:30:35
status: draft

---

The Kedro node is an essential part of the pipeline.  It defines what catalog
entries get passed in, what function gets ran, and the catalog entry to save
the results under.

https://waylonwalker.com/what-is-kedro/

> 👆 Unsure what kedro is?  Check out this post.

## The node function

The node function is the most common and reccomended way to define kedro nodes.
It is a function that constructs and returns `Node` objects for you.

## Creating your first kedro node


``` python
from kedro.pipeline import node

def identity(df):
    "a function that returns itself"
    return df

my_first_node = node(
   func=identity,
   inputs='raw_cars',
   output='int_cars',
   tags=['int',]
   )
```

### function

The `func` passed into node can be any callable that accepts the inputs yout
have specified, and returns the correct output that you specify as your output.

* any callable
* a function you write
* a function from a library
* class constructor
* lambda function
* partial function
* literally any callable

https://waylonwalker.com/kedro-inputs/

> For more information on how kedro passes inputs into your functions check out
> this post


``` python
import pandas as pd
from kedro.pipeline import node

range_node = node(lambda: range(100), None, "range", name="range"),
dataframe_node = node(pd.DataFrame, "range", "df"),
```
#### Using a lambda as a function

``` python
from kedro.pipeline import node

my_first_node = node(
   func=lambda x: x,
   inputs='raw_cars',
   output='int_cars',
   tags=['int',]
   )
```

#### Using a partial function

```
from kedro.pipeline import node
from functools import partial, update_wrapper

def divide(array, by):
    return [i/by for i in array]

halfer = update_wrapper(partial(divide, by=2), divide)

my_halfer_node = node(
   func=halfer,
   inputs='raw_cars',
   output='int_cars',
   tags=['int',]
   )
```

To further show the point that any callable can be out node's `func`.

``` python
from kedro.pipeline import node
import pandas as pd
from functools import partial, update_wrapper

MyDataFrame = update_wrapper(partial(pd.DataFrame, columns=["mycol"]), pd.DataFrame)

range_node = node(lambda: range(100), None, "range", name="range"),
dataframe_node = node(MyDataFrame, "range", "df"),
```
### inputs

kedro inputs can be `None`, a catalog entry, or a dict mapping the functions
keyword arguments to catalog entries.  Catalog entries are always represented
as a string matching the key of the catalog entry you want to load.

#### None

Sometimes you may want to have a node without any inputs.  This node may be
used to generate some data from scratch, or fetch some data that does not have
an existing DataSet type setup.  DataSets are easy to setup, simply fork one of
kedros built in ones and use it, but for one or two nodes the setup may not be
worth it.

``` python
from kedro.pipeline import node

random_100_node = node(
   func=lambda: random.sample(range(0, 100), 100),
   inputs=None,
   output='random_100',
   name='create_random_100',
   )
```

#### str

This is by far the most common input that you will use.  This will simply tell
kedro what dataset to load behind the scenes and passin to the function that
you provide.

``` python
from kedro.pipeline import node

random_100_node = node(
   func=lambda random_100: [x**2 for x in random_100],
   inputs='random_100',
   output='random_squared',
   name='create_random_squared',
   )
```

> Note, I am using a lot of lambdas here for simplicity as each function so far
> is a simple one-liner.  These could also be a regular function if you are
> uncomfortable with lambdas.

#### list

``` python
from kedro.pipeline import node

random_100_node = node(
   func=lambda random_100, random_squared: list(zip(random_100, random_squared)
   inputs=['random_100', 'random_squared'],
   output='random_join',
   name='create_random_join',
   )
```


#### dict

kedro will unpack dictionaries into your function if you pass in a dictionary.
In code review I start suggesting converting from a list to dict at 3 and
require it above 5.  It gets way too hard to refactor and move things while
keeping track of the order of really long sets of inputs.  Passing them in by
name, as a dictionary, makes it such that order no longer matters.

``` python
from kedro.pipeline import node

random_100_node = node(
   func=lambda x, y: list(zip(x, y)),
   inputs={'x': 'random_100', 'y':'random_squared'},
   output='random_join',
   name='create_random_join',
   )
```

> Switch from list to dict inputs between 3 and five inputs to improve
> readability and prevent ordering mistakes.


### outputs

### tags

### name

## Execution order

## Running specific nodes

### by name

### by tag

### to_inputs

### to_outputs

### from_inputs

### from outputs


