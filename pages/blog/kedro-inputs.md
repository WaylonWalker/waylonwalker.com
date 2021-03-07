---
templateKey: blog-post
related_post_label: Check out this related post
tags: 
  - kedro
  - python
  - data
title: How Kedro handles your inputs
date: 2020-06-19T03:00:00Z
status: published
description: Passing inputs into kedro is a key concept. Understanding how it
    accepts a single catalog key as input is quite trivial that easily makes
    sense, but passing a list or dictionary of catalog entries can be a bit
    confusing.
cover: '/static/kedro-inputs.png'

---

Passing inputs into kedro is a key concept.  Understanding how it accepts a single catalog key as input is quite trivial that easily makes sense, but passing a list or dictionary of catalog entries can be a bit confusing.

## *args/**args review

Check out this post for a review of how `*args` `**kwargs` work in python.

[![python args and kwargs](https://images.waylonwalker.com/python-args-kwargs.png)](https://waylonwalker.com/python-args-kwargs)
> [python args and kwargs](https://waylonwalker.com/python-args-kwargs) article by [@_waylonwalker](https://twitter.com/_WaylonWalker)

## All Kedro inputs are catalog Entries

When kedro runs your pipeline it uses the catalog to imperatively load your data, meaning that you don't tell kedro how to load your data, you tell it where your data is and what type it is.  These catalog entries are like a `key-value` store.  You just need to give the key when setting up a node.

## Single Inputs

These are fairly straightforward to understand.  In the example below when `kedro` runs the pipeline it will load the input from the catalog, then pass that input to the func, then save the returned value to the output catalog entry.

``` python
from kedro.pipeline import node

def create_int_sales(sales):
    "cleans up raw sales data"
    ...
    return cleaned_sales

my_node = node(
    func=create_int_sales,
    inputs='raw_sales',
    output='int_sales',
    )
```

---

## List of inputs

Let's look at an example node that combines more than one dataset. When kedro has sees a list of catalog entries it will load up each catalog entry sequentially then pass them in order to the `create_sales_report` function.

``` python
from kedro.pipeline import node

def create_sales_report(sales, products):
    "adds product metadata to the sales data"
    ...


my_node = node(
    func=create_sales_report,
    inputs=['pri_sales', 'pri_products'],
    output='sales_report',
    )
```

## simulating pipeline run using 2 inputs

Here We can simulate what kedro does during the pipeline run by using `*args`.

``` python
# inputs you gave kedro
inputs=['pri_sales', 'pri_products']
# load data
input_data = [catalog.load(entry) for entry in  inputs]
# run the node
sales_report = create_sales_report(*input_data)
# save the data to the output
catalog.datasets.sales_report.save(sales_report)
```

## More generalizable functions

We can also use `*args` to make our functions a little bit more generalizable. The first that
comes to my mind is a unioner. The second

``` python
def unioner(*dfs: pd.DataFrame): -> pd.DataFrame
    pd.concat(dfs)
```

Now we can pass any number of DataFrames into our kedro node to get unioned together, but
do we really need a function for a one-liner... No we can use an inline function for this case.

``` python
my_node = node(
    func=lambda *dfs: pd.concat(dfs),
    input=['sales_2017', 'sales_2018'],
    output='sales',
)
```

## `*args` scares the crap out of me!

It's great for the `unioner` example where its a collection of similar things where order
does not matter.  But for the `create_sales_report` function.  Those are distinctly different
inputs.  If someone does some refactoring and changes the order in one place or another it's
going to turn into a bad day real fast.

## **kwargs are a bit better

Let's refactor the `create_sales_report` before someone tries to ruin our day.  We can easily
do this by passing a dictionary (keys are the argument name, values are the catalog key)
of arguments to kedro instead of a list.

``` python
from kedro.pipeline import node

def create_sales_report(sales, products):
    "adds product metadata to the sales data"
    ...

my_node = node(
    func=create_sales_report,
    inputs={'sales': 'pri_sales', 'products': 'pri_products'},
    output='sales_report',
    )
```

Now if someone tries to refactor the order of arguments we are safe!

## Simulating the pipeline run with `**kwargs`

Pretty much the same as before, except with `**kwargs` and `dictionaries` keeping us a bit
safer.

``` python
# inputs you gave kedro
inputs={'sales': 'pri_sales', 'products': 'pri_products'},
# load data
input_data = {arg: catalog.load(entry) for arg, entry in inputs.items()}
# run the node
sales_report = create_sales_report(**input_data)
# save the data to the output
catalog.datasets.sales_report.save(sales_report)
```

## Stay Safe

Kedro inputs are quite easy to understand if you already have a grasp of `*args` and `**kwargs`
and if you don't it is still fairly intuitive to pick up.  Stay on the safe side, if your
collection of inputs are clearly different things, use a dictionary for safety.
