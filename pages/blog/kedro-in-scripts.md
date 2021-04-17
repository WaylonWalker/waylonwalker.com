---
templateKey: blog-post
tags: []
title: Using Kedro In Scripts
date: 2021-04-17T00:00:00
status: draft
description: ''

---

With the latest releases of kedro `0.17.x` it is now possible to run kedro
pipelines from within scripts.  While I would not start a project with this
technique it will be a good tool to keep in my back pocket when I want to
sprinkle in a bit of kedro goodness in existing projects.

## No More Rabbit Hole of Errors

I've tried to do this in kedro `0.16.x` and it turned into a rabbit hole of
errors.  First kedro needed a `conf` directory, if you tried to fake one in it
would then ask for logging setup.  These errors just kept coming to the point
it wasnt worth doing and I might as well use a proper template for real
projects and stick to simple function calls for things that are not a kedro
project.

## Kedro in a script

``` python 
from kedro.pipeline import Pipeline, node
from kedro.io import DataCatalog
from kedro.runner.sequential_runner import SequentialRunner

# additional datasets you want to use
from kedro.extras.datasets.pandas.csv_dataset import CSVDataSet
from kedro.extras.datasets.pandas.parquet_dataset import ParquetDataSet

runner = SequentialRunner()
pipeline = Pipeline(
    [
        node(lambda: range(100), None, "range"),
        node(lambda x: [i ** 2 for i in x], "range", "range**2"),
        node(lambda x: [i for i in x if i > 5000], "range**2", "range>5k"),
        node(lambda x: x[:5], "range>5k", "range>5k-head"),
        node(lambda x: sum(x) / len(x), "range>5k", "range>5k-mean"),
    ]
)
catalog = DataCatalog()

runner.run(pipeline, catalog)

```

