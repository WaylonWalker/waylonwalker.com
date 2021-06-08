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

## The node function

The node function is the most common and reccomended way to define kedro nodes.
It is a function that constructs and returns `Node` objects for you.

## Creating your first kedro node


``` python
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

#### Using a lambda as a function

``` python
my_first_node = node(
   func=lambda x: x,
   inputs='raw_cars',
   output='int_cars',
   tags=['int',]
   )
```

#### Using a partial function

```
from functools import partial, update_wrapper

def divide(array, by):
    return [i/by for i in array]

half = update_wrapper(partial(divide, by=2), divide)
```

### inputs

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


