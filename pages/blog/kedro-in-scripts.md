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
_as of 0.17.2_

I've tried to do this in kedro `0.16.x` and it turned into a rabbit hole of
errors.  First kedro needed a `conf` directory, if you tried to fake one in it
would then ask for logging setup.  These errors just kept coming to the point
it wasnt worth doing and I might as well use a proper template for real
projects and stick to simple function calls for things that are not a kedro
project.

## Kedro in a script

In order to get kedro running you are going to need a pipeline, catalog, and
runner at a minimum.  For those who have used kedro before the pipeline will
look very similar to what you are familiar with, but the catalog will not be
loaded from yaml and you will need to bring your own runner.

``` python 
from kedro.pipeline import Pipeline, node
from kedro.io import DataCatalog
from kedro.runner.sequential_runner import SequentialRunner


# additional datasets you want to use
from kedro.extras.datasets.pandas.csv_dataset import CSVDataSet
from kedro.extras.datasets.pandas.parquet_dataset import ParquetDataSet

# the seqential runner is the simplest, it runs one node at a time.
runner = SequentialRunner()

# this is a super simple example pipeline
pipeline = Pipeline(
    [
        node(lambda: range(100), None, "range"),
        node(lambda x: [i ** 2 for i in x], "range", "range**2"),
        node(lambda x: [i for i in x if i > 5000], "range**2", "range>5k"),
        node(lambda x: x[:5], "range>5k", "range>5k-head"),
        node(lambda x: sum(x) / len(x), "range>5k", "range>5k-mean"),
    ]
)

# to get up and running you can use an empty catalog
catalog = DataCatalog()

runner.run(pipeline, catalog)
```

> Above is the minimal setup to get a kedro pipeline running

## more practically

More often your kedro pipelines are going to use a real function rather than a
lambda, and pandas dataframes.


``` python
def clean_columns(df: pd.DataFrame):
    df.columns = [col.lower().strip() for col in df.columns]

pipeline = Pipeline(
    [
        node(clean_columns, "raw_data", "clean_columns", name="create_clean_columns"),
    ]
)

catalog = DataCatalog(
    {
        "raw_data": ParquetDataSet(filepath=f"data/raw_data.parquet")
        "clean_columns": ParquetDataSet(filepath=f"data/clean_columns.parquet")
    }
)
```


> One single node pipeline to get you started

## Semi-automatic catalog

For some reason when I tried to use the DataCatalogWithDefault it did not pick
up my datasets right.  I suspect this has something to do with not setting up a
proper session, so this is what I did in a pinch to get that catalog goodness
for my DataFrames without setting up each one manually.


``` python
catalog = DataCatalog(
    {
        name: ParquetDataSet(filepath=f"data/{name}.parquet")
        for name in pipeline.all_outputs()
    }
)
```

> for use with pandas

For the example above that does not use DataFrames I would pickle all of my
outputs to enable re-loading them later.

``` python
catalog = DataCatalog(
    {
        name: PickleDataSet(filepath=f"data/{name}.pkl")
        for name in pipeline.all_outputs()
    }
)
```


> for use with non-pandas datasets

## Logging

Once you explicitly add datasets kedro will start logging when its
loading, running, or saving each node.  This will start to look a
bit more familiar to anyone who has used kedro before.

``` python
ww3 ↪main ©kedro-in-scripts v3.8.8 ipython
❯ runner.run(pipeline, catalog)
2021-04-18 09:30:58,099 - kedro.pipeline.node - INFO - Running node: <lambda>(None) -> [range]
2021-04-18 09:30:58,100 - kedro.io.data_catalog - INFO - Saving data to `range` (PickleDataSet)...
2021-04-18 09:30:58,104 - kedro.runner.sequential_runner - INFO - Completed 1 out of 5 tasks
2021-04-18 09:30:58,105 - kedro.io.data_catalog - INFO - Loading data from `range` (PickleDataSet)...
2021-04-18 09:30:58,105 - kedro.pipeline.node - INFO - Running node: <lambda>([range]) -> [range**2]
2021-04-18 09:30:58,105 - kedro.io.data_catalog - INFO - Saving data to `range**2` (PickleDataSet)...
2021-04-18 09:30:58,111 - kedro.runner.sequential_runner - INFO - Completed 2 out of 5 tasks
2021-04-18 09:30:58,111 - kedro.io.data_catalog - INFO - Loading data from `range**2` (PickleDataSet)...
2021-04-18 09:30:58,112 - kedro.pipeline.node - INFO - Running node: <lambda>([range**2]) -> [range>5k]
2021-04-18 09:30:58,112 - kedro.io.data_catalog - INFO - Saving data to `range>5k` (PickleDataSet)...
2021-04-18 09:30:58,115 - kedro.runner.sequential_runner - INFO - Completed 3 out of 5 tasks
2021-04-18 09:30:58,115 - kedro.io.data_catalog - INFO - Loading data from `range>5k` (PickleDataSet)...
2021-04-18 09:30:58,115 - kedro.pipeline.node - INFO - Running node: <lambda>([range>5k]) -> [range>5k-mean]
2021-04-18 09:30:58,115 - kedro.io.data_catalog - INFO - Saving data to `range>5k-mean` (PickleDataSet)...
2021-04-18 09:30:58,118 - kedro.runner.sequential_runner - INFO - Completed 4 out of 5 tasks
2021-04-18 09:30:58,119 - kedro.io.data_catalog - INFO - Loading data from `range>5k` (PickleDataSet)...
2021-04-18 09:30:58,119 - kedro.pipeline.node - INFO - Running node: <lambda>([range>5k]) -> [range>5k-head]
2021-04-18 09:30:58,119 - kedro.io.data_catalog - INFO - Saving data to `range>5k-head` (PickleDataSet)...
2021-04-18 09:30:58,122 - kedro.runner.sequential_runner - INFO - Completed 5 out of 5 tasks
2021-04-18 09:30:58,122 - kedro.runner.sequential_runner - INFO - Pipeline execution completed successfully.
```

## Kedro Viz

I was not able to easily get kedro viz up and running for my use case.  If you
really wanted to you could start modifying their format_pipelines_data function
in
[server.py](https://github.com/quantumblacklabs/kedro-viz/blob/main/package/kedro_viz/server.py).
Or you could render a new template, and put your pipeline there for viz
purposes.

> It's possible, but might as well stick to the template

## cli

For something that I would be using this on I am probably not going to put much
effort into the cli as its not likely something that we are going to have a
team of developers interacting with contstantly.  I would just put together the
minimum necessary to run my application how I need.


``` python
if __name__ == "__main__":
    import sys

    if '--skip-raw' in sys.argv:
        runner.run(pipeline.from_inputs('range**2'), catalog)
    else:
        runner.run(pipeline, catalog)

```

## It's a bit Rough

While I might use this in production somewhere, its going to be inside of some
other not kedro application. I will still be using something quite similar to
their template for my pipleining projects.  It misses out on some really good
things that brings me to kedro like hooks, plugins, credentials, catalog,
logging config, cli, and viz.



