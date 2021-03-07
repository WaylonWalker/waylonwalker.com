---
templateKey: blog-post
related_post_label: Check out this related post
tags: ['kedro', 'python', 'data']
title: How to find things in your kedro catalog
date: 2020-06-22T03:00:00Z
status: published
description: kedro 0.16.2 just dropped last week with a long-awaited feature...
    catalog search!  I went as far as monkey patching this into each of my
    projects.  I work jump between a few really big projects that have tons of
    datasets.  Being able to quickly search for what I need is so useful.
cover: '/static/kedro-catalog-search.png'

---

kedro 0.16.2 just dropped last week with a long-awaited feature... **catalog search**!  I went as far as monkey patching this into each of my projects.  I work jump between a few really big projects that have tons of datasets.  Being able to quickly search for what I need is so useful.

## The Catalog

The kedro data catalog is a key component to the kedro framework.  It handles all data loading and saving for you.  It is configurable and hackable.  Having all your data connections listed in one place make it so easy to pick your project up and move it to a completely new environment.  That sweet imperative loading style saves so much read/write overhead.  I can load all my data with a single command whether it's in amazon s3, google cloud platform, or a local file.

## Kick start a toy project

Just like with most of these articles, I am going to create a conda environment so that I don't break any existing projects and scaffold up a toy project to learn from.

``` bash
conda create -n kedro0162 python=3.8 -y
activate kedro0162
pip install kedro
kedro new # call it Kedro 0162 and click-through
cd kedro-0162
kedro install
```

Expect this set of commands to take a few minutes depending on your system, connection speed, and amount of packages already in your local cache.

## Create some catalog

Now the power of the catalog search really starts to shine when your projects grow legs.  You have groups of many datasets containing patterns of data including `layer`, or `source` among other things.

``` bash
vim conf/base/catalog.yml
```

In the catalog, you will see a few lines of instructions followed by

``` yml
example_iris_data:
  type: pandas.CSVDataSet
  filepath: data/01_raw/iris.csv
```

This gives us one stored catalog entry called `example_iris_data`, it is a CSV file stored in `data/01_raw/iris.csv`.


Let's make up a transportation company that is siloed into three different divisions and it is our job to bring their sales and product metadata into a single report.  This company makes `lifted-trucks`, `primium-scoots`, and `luxy-yahts`.  and we know that we will want `raw`, `int`, `pri` and `modin` layers to start our project so let's scaffold up that catalog real quick.

``` yml
# ――――――――― lifted-truck ―――――――――

raw_lifted_truck_sales:
  type: pandas.CSVDataSet
  filepath: data/01_raw/sales/lifted-truck.csv

int_lifted_truck_sales:
  type: pandas.CSVDataSet
  filepath: data/01_int/sales/lifted-truck.csv

pri_lifted_truck_sales:
  type: pandas.CSVDataSet
  filepath: data/01_pri/sales/lifted-truck.csv

raw_lifted_truck_info:
  type: pandas.CSVDataSet
  filepath: data/01_raw/info/lifted-truck.csv

int_lifted_truck_info:
  type: pandas.CSVDataSet
  filepath: data/01_int/info/lifted-truck.csv

pri_lifted_truck_info:
  type: pandas.CSVDataSet
  filepath: data/01_pri/info/lifted-truck.csv

# ――――――――― primium-scoot ―――――――――

raw_primium_scoot_sales:
  type: pandas.CSVDataSet
  filepath: data/01_raw/sales/primium-scoot.csv

int_primium_scoot_sales:
  type: pandas.CSVDataSet
  filepath: data/01_int/sales/primium-scoot.csv

pri_primium_scoot_sales:
  type: pandas.CSVDataSet
  filepath: data/01_pri/sales/primium-scoot.csv

raw_primium_scoot_info:
  type: pandas.CSVDataSet
  filepath: data/01_raw/info/primium-scoot.csv

int_primium_scoot_info:
  type: pandas.CSVDataSet
  filepath: data/01_int/info/primium-scoot.csv

pri_primium_scoot_info:
  type: pandas.CSVDataSet
  filepath: data/01_pri/info/primium-scoot.csv

# ――――――――― luxy-yaht ―――――――――

raw_luxy_yaht_sales:
  type: pandas.CSVDataSet
  filepath: data/01_raw/sales/luxy-yaht.csv

int_luxy_yaht_sales:
  type: pandas.CSVDataSet
  filepath: data/01_int/sales/luxy-yaht.csv

pri_luxy_yaht_sales:
  type: pandas.CSVDataSet
  filepath: data/01_pri/sales/luxy-yaht.csv

raw_luxy_yaht_info:
  type: pandas.CSVDataSet
  filepath: data/01_raw/info/luxy-yaht.csv

int_luxy_yaht_info:
  type: pandas.CSVDataSet
  filepath: data/01_int/info/luxy-yaht.csv

pri_luxy_yaht_info:
  type: pandas.CSVDataSet
  filepath: data/01_pri/info/luxy-yaht.csv


# ――――――――― combined ―――――――――
pri_combined_sales:
  type: pandas.CSVDataSet
  filepath: data/01_pri/sales/combined.csv

pri_combined_info:
  type: pandas.CSVDataSet
  filepath: data/01_pri/info/combined.csv

# ――――――――― modin ―――――――――

modin_main:
  type: pandas.CSVDataSet
  filepath: data/01_pri/info/combined.csv

```

## Some examples of common regex uses

`regex` gets really complicated fast, but these basic examples are very common use cases and will get you a long way without being very complicated.

* `term` - all catalog entries that include `term` in the catalog entry
* `^term` - all catalog entries that include `term` at the **beginning** of the catalog entry
* `term$` - all catalog entries that include `term` at the **end** of the catalog entry
* `term1.*term2` - include anything in between `term1` and `term2`.
* `term1|term2` - all catalog entries that include `term1` or `term2`


## Let's Search this thing

kedro has long included the `catalog.list()` feature that returns a list of all datasets.  Now the `list` command takes in a `regex_search` keyword argument.  By default, it is empty and returns the entire catalog.


``` bash
kedro ipython
```

## list out all of the luxy-yahts

``` python
>>> catalog.list('luxy_yaht`)
['raw_luxy_yaht_sales',
 'int_luxy_yaht_sales',
 'pri_luxy_yaht_sales',
 'raw_luxy_yaht_info',
 'int_luxy_yaht_info',
 'pri_luxy_yaht_info']
 ```

## List out data by layer

Easy just search for the layer name.

### raw

``` python
>>> catalog.list('raw')
['raw_lifted_truck_sales',
 'raw_lifted_truck_info',
 'raw_primium_scoot_sales',
 'raw_primium_scoot_info',
 'raw_luxy_yaht_sales',
 'raw_luxy_yaht_info']
```

### pri

``` python
 >>> catalog.list('pri')
['pri_lifted_truck_sales',
 'pri_lifted_truck_info',
 'raw_primium_scoot_sales',
 'int_primium_scoot_sales',
 'pri_primium_scoot_sales',
 'raw_primium_scoot_info',
 'int_primium_scoot_info',
 'pri_primium_scoot_info',
 'pri_luxy_yaht_sales',
 'pri_luxy_yaht_info',
 'pri_combined_sales',
 'pri_combined_info']
```

😲 We just included every `primium-scoot` dataset!

Here we just encountered our first need for `regex`.  I'll be the first to admit that I am really bad at regex, it's incredibly confusing, becomes read-only with much complexity, but is super powerful and used in a lot of places.


## `^term`
_beginning of catalog entry_

The `^` regex operator searches for catalog entries that include the search term at the very beginning.

``` python
 >>> catalog.list('^pri')
['pri_lifted_truck_sales',
 'pri_lifted_truck_info',
 'pri_primium_scoot_sales',
 'pri_primium_scoot_info',
 'pri_luxy_yaht_sales',
 'pri_luxy_yaht_info',
 'pri_combined_sales',
 'pri_combined_info']
```

## `term$`
_end of catalog entry_

The `$` operator is the opposite of the `^` operator.  It means give me all that matches that occur at the end of the catalog entry.

``` python
>>> catalog.list('info$')
['raw_lifted_truck_info',
 'int_lifted_truck_info',
 'pri_lifted_truck_info',
 'raw_primium_scoot_info',
 'int_primium_scoot_info',
 'pri_primium_scoot_info',
 'raw_luxy_yaht_info',
 'int_luxy_yaht_info',
 'pri_luxy_yaht_info',
 'pri_combined_info']

```


## `term1.*term2`

The `.*` operator in regex means give me all the datasets that include the two terms no matter what is between them.  There is also a `.?` to only allow one character between them.  More often than not I really just want the two patterns to exist in the dataset entry.

``` python
>>> catalog.list('raw.*info$')
['raw_lifted_truck_info',
 'raw_primium_scoot_info',
  'raw_luxy_yaht_info']
```

## Some real things that we can do with search

Let's look at a few examples beyond the obvious of just searching for the dataset that we want to load.

## Check Raw Data

While migrating pipelines between environments it's important to know if your raw datasets are available.  I will argue that you should also consider looking at `pipeline.inputs` as it cannot lie and gives you a true reading of the pipeline inputs.  But another easy check might be to check all the datasets that the Data Engineers have labeled raw.

``` python
>>> {dataset: catalog.exists(dataset) for dataset in catalog.list('^raw')}
{'raw_lifted_truck_sales': False,
 'raw_lifted_truck_info': False,
 'raw_primium_scoot_sales': False,
 'raw_primium_scoot_info': False,
 'raw_luxy_yaht_sales': False,
 'raw_luxy_yaht_info': False}
```

Since we just created a dummy catalog the data does not exist in this example.

## Create a new catalog

Let's say that we have someone on the team who is from the land division of our company and they want a simplified catalog readily available that does not include any marine data.

To do this we will need to reach a bit into the kedro internals for the `DataCatalog` class and utilize a new regex operator `|`.


``` python
>>> from kedro.io import DataCatalog
>>> land_catalog = DataCatalog(
    {
        dataset: getattr(catalog.datasets, dataset)
        for dataset in catalog.list('truck|scoot')
        }
    )
>>> land_catalog.list()
['raw_lifted_truck_sales',
 'int_lifted_truck_sales',
 'pri_lifted_truck_sales',
 'raw_lifted_truck_info',
 'int_lifted_truck_info',
 'pri_lifted_truck_info',
 'raw_primium_scoot_sales',
 'int_primium_scoot_sales',
 'pri_primium_scoot_sales',
 'raw_primium_scoot_info',
 'int_primium_scoot_info',
 'pri_primium_scoot_info']
```

## regex recap

* `^term` - beginning
* `term$` - end
* `term1.*term2` - anything in between
* `term1|term2` - or
