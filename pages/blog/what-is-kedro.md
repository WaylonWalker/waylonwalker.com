---
templateKey: blog-post
related_post_label: Check out this related post
tags: ['kedro']
title: What is Kedro
date: 2020-02-24T12:48:00Z
status: published
description: Kedro is an open source data pipeline framework.  It provides
  guardrails to set your project up right from the start without needing to
  know deeply how to setup your own python library for data pipelining.  It
  includes really great ways to manipulate `catalogs` and `pipelines`.  This
  article will cover the 10K view of kedro, future articles will dive deper
  into each one.
cover: "/static/what-is-kedro.png"

---

[kedro](https://kedro.readthedocs.io) is an open-source data pipeline framework.  It provides guardrails to set your project up right from the start without needing to know deeply how to set up your own python library for data pipelining.  It includes great ways to manipulate `catalogs` and `pipelines`.  This article will cover the 10K view of [kedro](https://kedro.readthedocs.io), future articles will dive deeper into each one.

<!-- {% slideshare DAZrqvJmuUUfFF %} -->


## Libraries

Currently, [kedro](https://kedro.readthedocs.io) is broken down into 3 different libraries.

💎 [kedro](https://kedro.readthedocs.io)

📉 [kedro-viz](https://github.com/quantumblacklabs/kedro-viz)

🏗 [kedro-docker](https://github.com/quantumblacklabs/kedro-docker)

## [kedro](https://kedro.readthedocs.io)

![kedro logo](https://images.waylonwalker.com/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f7175616e74756d626c61636b6c6162732f6b6564726f2f6d61737465722f696d672f6b6564726f5f62616e6e65722e6a7067.jpg)


[kedro](https://kedro.readthedocs.io) is the core of the ecosystem.  It provides the docs, getting started, `kedro new` templates, and the core library including the catalog and pipeline.

### Catalog

![catalogs](https://dev-to-uploads.s3.amazonaws.com/i/trzfj86dbq0ronis26x1.jpg)

Inside this core library is a data catalog object.  This allows you to specify attributes about your data, then load and save it without ever writing a single line of read/write code, which can become very cumbersome.  Older versions would load this into the io variable, currently it loads into the catalog.  The power of the catalog is that it allows you to read and write data by just referencing its name.  Typically this is done inside of a YAML file, but can be done in python.

Here is an example of a CSV dataset stored locally

``` yaml
# Example 1: Loads a local csv file
bikes:
  type: CSVLocalDataSet
  filepath: "data/01_raw/bikes.csv"
```

This dataset can be loaded by name

``` python
catalog.load('bikes')
```

Though it's not typical practice it is possible to save data to a catalog entry ad-hoc.  Typically the pipeline is used to run functions and save data for you.

``` python
import pandas as pd
bikes_df = pd.DataFrame({...<bikes_data>...})
catalog.datasets.bikes.save(bikes_df)
```

### Pipeline

![building pipelines](https://images.waylonwalker.com/roman-pentin-T5QT2bmiD4E-unsplash.jpg)

The pipeline object is the brains of [kedro](https://kedro.readthedocs.io).  When working with [kedro](https://kedro.readthedocs.io) you simply define functions that take in data as arguments, manipulate it, and return a new dataset.  The pipeline will decide what order to execute these functions ini based on their dependencies.  It will then work with the catalog to load the data from the catalog pass it to your function, the save the returned data in the catalog.

Here is an example pipeline from the docs.

``` python
import pandas as pd
import numpy as np
from kedro.pipeline import Pipeline
from kedro.pipeline import node

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

pipeline = Pipeline(nodes)
```

## [kedro-viz](https://github.com/quantumblacklabs/kedro-viz)

[kedro-viz](https://github.com/quantumblacklabs/kedro-viz) is a priceless component to the [kedro](https://kedro.readthedocs.io) ecosystem.  It gives you x-ray vision into your project.  You can see exactly how data flows through your pipeline.  Since it is fully automated it is always up to date and never lies to you.  [kedro-viz](https://github.com/quantumblacklabs/kedro-viz) is an integral part of my daily debugging and refactoring toolbelt.

Starting the viz from the command line is super easy

``` bash
cd my-kedro-project
kedro viz
```

![](https://images.waylonwalker.com/pipeline_visualisation.png)

## [kedro-docker](https://github.com/quantumblacklabs/kedro-docker)

[kedro-docker](https://github.com/quantumblacklabs/kedro-docker) is a simple way to set up your project for production.  It provides a few simple cli commands

``` bash
cd my-kedro-project
kedro docker build
kedro docker run
```

## Other resources

The [kedro docs](https://kedro.readthedocs.io/) have a ton of great resources.  They are searchable, but can be a bit of an overwhelming amount of data.

I keep adding to my [kedro notes](https://waylonwalker.com/notes/kedro/) as I find new and interesting things.

I tweet out most of those snippets as I add them, you can find them all here [#kedrotips](https://twitter.com/search?q=%23kedrotips).

## More to come

I am planning to do more articles like this, you can stay up to date with them by following me on [dev.to](https://dev.to/waylonwalker), subscribing to my [rss feed](https://waylonwalker.com/rss.xml), or subscribe to my [newsletter](https://waylonwalker.com/newsletter)
