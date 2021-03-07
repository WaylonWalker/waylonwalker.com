---
templateKey: blog-post
related_post_label: Check out this related post
tags: 
  - kedro
  - python
  - data
title: Gracefully adopt kedro, the catalog
date: 2020-06-29T03:00:00Z
status: published
description:
cover: '/static/graceful-kedro-catalog.png'

---


## Why use kedro catalog?

While using the catalog alone will not reap all of the benefits of the framework, it does get you and your project ready for the full framework eventually.  For me the full benefit of the catalog comes when you combine it with the pipeline and dont even touch read/write steps at all.

Taking a step into kedro by adopting the catalog first will give you a way to organize all of your data loads in one place, and stop manually writing read/write code, which can be different for each data and storage type. You just don't need to think about it.

---

* iperitive loading style
* organizes your data
* all file locations can be quickly identified
* can be dropped into kedro later

---

> "can be dropped into kedro later"
> Let's talk a bit more about that

## 2 Ways to Gracefully adopt the catalog
_How do I get started with the kedro catalog_

* add with the code api
* load from yaml (**recommended**)


## 1. Adding to the catalog with the code api
_how to use the kedro catalog code api_

It is possible to keep everything inside of one single file if you want by utilizing the code api, which defines the kedro catalog inside of your script with python.  I personally like this method as it is a bit more scriptable to create many layers of datasets with a for loop.  It can still be carried right into a kedro project, but is not the normal way that other kedro users will be used to seeing.  I'll leave it up to you which technique to use.


``` python
from kedro.io import DataCatalog
from kedro.extras.datasets.pandas import CSVDataSet

io = DataCatalog(
    {
        "bikes": CSVDataSet(filepath="../data/01_raw/bikes.csv"),
    }
)

```
> taken right from the kedro [docs](https://kedro.readthedocs.io/en/stable/04_user_guide/04_data_catalog.html)

👆 This can be done inside of a single Jupyter cell, and pulled out later.



## 2. Creating a catalog config file

**recommended**

This reccommended method it great since it will simply drop right in to a full kedro project if you were ever ready to adopt the framework as a whole.  The downside to gracefully adopting the framework is that you need to have a bit of an understanding of the internals to do it.  When using the framework as a whole it seemlessly takes care of everything for you.

``` yaml
# conf/base/catalog.yml
# Example 1: Loads / saves a CSV file from / to a local file system

bikes:
  type: pandas.CSVDataSet
  filepath: data/01_raw/bikes.csv
```


``` python
from kedro.config import ConfigLoader
from kedro.io import DataCatalog

conf_loader = ConfLoader(['conf/base'])
conf_catalog = conf_loader.get('catalog*', 'catalog/**')
catalog = DataCatalog.from_config(conf_catalog)
```

> You can even do this 👆 from a Jupyter notebook

If you do happen to be in a module deeper into an existing library I tend to leverage the use of the `__file__` magic.  `__file__` is a string containing the location of the current file.  You can initiate a `Path` object from this and roll up the necessary number of directories with the `parents` attribute then into the `conf/base` directory.  I find this more **more robust** as it does not depend on your current working directory.

``` python
from pathlib import Path
conf_loader = ConfLoader([Path(__file__).parents[1] / 'conf/base'])
conf_catalog = conf_loader.get("catalog*", "catalog/**")
new_catalog = DataCatalog.from_config(conf_catalog)
```

> I find leveraging the `__file__` magic a bit more robust when possible as it does not depend on your current working directory.

## Adhoc adding to an existing kedro catalog

Let's say that you are already using a kedro project, but you are wanting to develop new features entirely in the context of a notebook.  You can easily create a catalog as shown above.  Since the kedro catalog variable is typically `catalog`, we will call it `new_catalog` and add it to the existing `catalog` below.  If you are not quite sure what that `**catalog` syntax is doing check out my article on `**kwargs`.

``` python
catalog.add_feed_dict(new_catalog.datasets.__dict__)
```

[![python args and kwargs](https://images.waylonwalker.com/python-args-kwargs.png)](https://waylonwalker.com/python-args-kwargs)
> [python args and kwargs](https://waylonwalker.com/python-args-kwargs) article by [@_waylonwalker](https://twitter.com/_WaylonWalker)

The framework makes appending

``` python
catalog = DataCatalog({**catalog.datasets.__dict__, **new_catalog.datasets.__dict__})
``



## One word of caution


If you have any hooks running `after_catalog_created`, they will not be run on the appended catalog entries.
