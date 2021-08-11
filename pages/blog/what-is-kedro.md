---
templateKey: blog-post
tags: ['kedro', 'python']
title: What is Kedro
date: 2020-02-24T12:48:00Z
status: published

---

Kedro is an unopinionated Data Engineering framework that comes with a somewhat
opinionated template. It gives the user a way to build pipelines that
automatically take care of io through the use of abstract `DataSets` that the
user specifies through `Catalog` entries.  These `Catalog` entries are loaded,
ran through a function, and saved by `Nodes`.  The order that these `Nodes` are
executed are determined by the `Pipeline`, which is a  **DAG**.  It's the
`runner`'s job to manage the execution of the `Nodes`.

---

https://waylonwalker.com/what-is-kedro-1/

> This is an updated version of my original what-is-kedro article

---

## Orchestrators

Like I said, `kedro` is unopinionated it does determine where or how your data
should be ran.  The kedro team does support the following **Orchestrators**
with very little add on to the base template.

* [Argo Workflows](https://kedro.readthedocs.io/en/stable/10_deployment/04_argo.html)
* [Prefect](https://kedro.readthedocs.io/en/stable/10_deployment/05_prefect.html)
* [Kubeflow Workflows](https://kedro.readthedocs.io/en/stable/10_deployment/06_kubeflow.html)
* [AWS Batch](https://kedro.readthedocs.io/en/stable/10_deployment/07_aws_batch.html)
* [Databricks](https://kedro.readthedocs.io/en/stable/10_deployment/08_databricks.html)

## DataSets

Did I say kedro is unopionated?  Datasets are what allow kedro too be so
flexible accross a number of different python objects.  Any python object can
be made into a kedro dataset.  Kedro comes out of the box with **many** purpose built
`DataSets` like storing pandas DataFrames to parquet, csv, or a sql table.  If
kedro does not come with support for the type of python objects you work with
don't worry, you can for the closest option they support and build your own.
Or if you do not want to builf your own, you can use a `PickleDataSet` for
anything.


## Catalog

You will not often be creating your own datasets, most of what you need whould
already be taken care of by the kedro framework.  What you will need to do is
to use the existing `DataSets` to build your data catalog.

Kedro takes care of all fo the file io for you, you simply need to use the
catalog to tell kedro what type of DataSet to use and any extra information
that `DataSet` needs.  Much of the time this is simply a filepath.

Typically the catalog is specified in yaml format.  If you are not familiar
with yaml, I suggest
[learnxinyminutes.com/docs/yaml/](https://learnxinyminutes.com/docs/yaml/) as a
resource of examples.

``` yaml
test:
  type: pandas.CSVDataSet
  filepath: s3://your_bucket/test.csv #
```

> Here is the most basic yaml catalog entry taken from the kedro
> [docs](https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html?highlight=catalog)

``` yaml
cars:
  type: pandas.CSVDataSet
  filepath: data/01_raw/company/cars.csv
  load_args:
    sep: ','
  save_args:
    index: False
    date_format: '%Y-%m-%d %H:%M'
    decimal: .
```

> Here is a bit more complex example that takes in `load_args` and `save_args`
> [docs](https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html?highlight=catalog)


## Nodes

Nodes are a very core part of kedro to build the **DAG**.  These nodes are what
provides the definition of what catalog entries, get passed into which
function, and output to another catalog entry.  

``` python
import pandas as pd
import numpy as np

def clean_data(cars: pd.DataFrame,
               boats: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    return dict(cars_df=cars.dropna(), boats_df=boats.dropna())

def halve_dataframe(data: pd.DataFrame) -> List[pd.DataFrame]:
    return np.array_split(data, 2)

nodes = [
    node(clean_data,
         inputs=['cars2017', 'boats2017'],
         outputs=dict(cars_df='clean_cars2017',
                      boats_df='clean_boats2017')),
    node(halve_dataframe,
         'clean_cars2017',
         ['train_cars2017', 'test_cars2017']),
    node(halve_dataframe,
         dict(data='clean_boats2017'),
         ['train_boats2017', 'test_boats2017'])
]
```

> Here is an example of three nodes taken from their
> [docs](https://kedro.readthedocs.io/en/stable/kedro.pipeline.node.html?highlight=node)

## Pipeline

todo

## Runner

The runner is the bridge between kedro and the orchestrators.  The kedro team
provides some basic runners for running pipelines locally, built right into the
framework, but adding on new runners for different orchestrators is done
through the use of adding in a new runner to your project.

## Hooks

todo


## Links
* [kedro deployment](https://kedro.readthedocs.io/en/stable/10_deployment/01_deployment_guide.html)
