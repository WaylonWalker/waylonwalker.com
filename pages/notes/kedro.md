---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Kedro
date: 2019-11-02T05:00:00.000+00:00
status: published
description: My Notes about using kedro
cover: "/static/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f7175616e74756d626c61636b6c6162732f6b6564726f2f6d61737465722f696d672f6b6564726f5f62616e6e65722e6a7067.jpg"

---
## [#kedrotips](https://twitter.com/search?q=%23kedrotips&f=live)

I am tweeting out most of these snippets as I add them, you can find them all here [#kedrotips](https://twitter.com/search?q=%23kedrotips).

## 🗣 Heads up

Below are some quick snippets/notes for when using kedro to build data pipelines. So far I am just compiling snippets. Eventually I will create several posts on kedro. These are mostly things that I use In my everyday with kedro. Some are a bit more essoteric. Some are helpful when writing production code, some are useful more usefule for exploration.

## 📚 Catalog

![catalogs](https://images.waylonwalker.com/jesse-orrico-h6xNSDlgciU-unsplash.jpg)
_Photo by jesse orrico on Unsplash_

### CSVLocalDataSet

**python**

``` python
import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/quantumblacklabs/kedro/d3218bd89ce8d1148b1f79dfe589065f47037be6/kedro/template/%7B%7B%20cookiecutter.repo_name%20%7D%7D/data/01_raw/iris.csv')

data_set = CSVLocalDataSet(filepath="test.csv",
                                 load_args=None,
                                 save_args={"index": False})

iris_data_set.save(iris)
reloaded_iris = iris_data_set.load()
```

**yaml**

``` yaml
test_data:
   type: CSVLocalDataset
   filepath: test.csv
   load_args: None
   save_args:
      index: False
```

## CSVHTTPDataSet

``` python
cities = CSVHTTPDataSet(
    fileurl="https://raw.githubusercontent.com/quantumblacklabs/kedro/d3218bd89ce8d1148b1f79dfe589065f47037be6/kedro/template/%7B%7B%20cookiecutter.repo_name%20%7D%7D/data/01_raw/iris.csv",
    auth=None,
    load_args=None)

iris = iris_data_set.load()
```

``` yaml
cities:
   type: CSVHTTPDataSet
    fileurl: https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv
    auth: None
    load_args: None
```

## HDFLocalDataSet

``` python
import pandas as pd
from kedro.io import HDFLocalDataSet

iris = pd.read_csv('https://raw.githubusercontent.com/quantumblacklabs/kedro/d3218bd89ce8d1148b1f79dfe589065f47037be6/kedro/template/%7B%7B%20cookiecutter.repo_name%20%7D%7D/data/01_raw/iris.csv')
iris_data_set = HDFLocalDataSet(filepath="iris.hdf",
                           key="test_hdf_key",
                           load_args=None,
                           save_args=None)

iris_data_set.save(iris)
reloaded_iris = iris_data_set.load()
```

``` yaml
cars:
   type: HDFLocalDataSet
   filepath: test.hdf
   key: test_hdf_key
```

## HDFS3LocalDataSet

``` python
import pandas as pd
from kedro.io import HDFS3DataSet

iris = pd.read_csv('https://raw.githubusercontent.com/quantumblacklabs/kedro/d3218bd89ce8d1148b1f79dfe589065f47037be6/kedro/template/%7B%7B%20cookiecutter.repo_name%20%7D%7D/data/01_raw/iris.csv')
iris_data_set = HDFS3DataSet(filepath="iris.hdf",
                        bucket_name="bucket-us-west-1",
                        key="test_hdf_key",
                        load_args=None,
                        save_args=None)

iris_data_set.save(iris)
reloaded_iris = iris_data_set.load()
```

``` yaml
cars:
   type: HDFS3DataSet
   filepath: cars.hdf
   bucket_name: bucket-us-west-1
   key: test_hdf_key
```

## JSONLocalDataSet

``` python
import pandas as pd
from kedro.io import JSONLocalDataSet

iris = pd.read_csv('https://raw.githubusercontent.com/quantumblacklabs/kedro/d3218bd89ce8d1148b1f79dfe589065f47037be6/kedro/template/%7B%7B%20cookiecutter.repo_name%20%7D%7D/data/01_raw/iris.csv')
cars = JSONLocalDataSet(filepath="iris.json",
                        load_args=None,
                        save_args=None)

iris_data_set.save(iris)
reloaded_iris = iris_data_set.load()
```

``` yaml
cars:
   type: JSONLocalDataSet
   filepath: iris.json
```

## ParquetLocalDataSet

``` python
import pandas as pd
from kedro.io import ParquetLocalDataSet

iris = pd.read_csv('https://raw.githubusercontent.com/quantumblacklabs/kedro/d3218bd89ce8d1148b1f79dfe589065f47037be6/kedro/template/%7B%7B%20cookiecutter.repo_name%20%7D%7D/data/01_raw/iris.csv')

iris_data_set = ParquetLocalDataSet('iris',
                           engine='auto',
                           load_args=None,
                           save_args=None,
                           version=None)

iris_data_set.save(iris)
reloaded_iris = iris_data_set.load()
```

``` yaml
cars:
   type: JSONLocalDataSet
   filepath: cars
```

PickleS3DataSet

SQLTableDataSet

SQLQueryDataSet

TextLocalDataSet

ExcelLocalDataSet

## ⏳ Loading Data

![loading data](https://images.waylonwalker.com/battlecreek-coffee-roasters-eg6OUchGCsw-unsplash.jpg)
_Photo by Battlecreek Coffee Roasters on Unsplash_

### Simple Loading

``` python
df = catalog.load('cars')
```

### list all datasets

``` python
catalog.list()
```

### Saving Data

``` python
catalog.save('cars', cars)
```

### 🔍 Finding data

**simple keyword search**

``` python
query = 'raw'
[data for data in catalog.list() if query in data]
```

_see on_ [_#kedrotips_](https://twitter.com/_WaylonWalker/status/1197130980659732480?s=20)

**multi keyword serch**

``` python
query = 'raw sales'
data_sets = catalog.list()
for word in query.split():
	data_sets = [
       data
       for data in data_sets
       if query in data
       ]
```

_see on_ [_#kedrotips_](https://twitter.com/_WaylonWalker/status/1197528461587419139?s=20)

**🐒 monkey patch it**

``` python
def query(*search_terms):
     data_sets = catalog.list()
     for search in search_terms:
         data_sets = [
         data
         for data in data_sets
         if search in data
         ]
     return data_sets

catalog.query = query
```

_see on [#kedrotips](https://twitter.com/_WaylonWalker/status/1197855759507300352?s=20)

### 🤙 YOLO

_You Only Load Once_

**simple**

``` python
data = [catalog.load(d)
        for d in
        catalog.query('c_pri', 'cars')
        ]
```

**more refined**

``` python
data = {
   d: catalog.load(d)
   for d in catalog.query('c_pri', 'cars')
   }
```

**🍷 refined like a fine wine**

``` python
from types import SimpleNamespace
data = SimpleNamespace**{
   d: catalog.load(d)
   for d in catalog.query('c_pri', 'cars')
   })
```

**🧀 Make it a function**
_getting funcy_

``` python
from types import SimpleNamespace

def yolo(*search_terms):
   """you only load once
   using query method from previous tip"""
   data = SimpleNamespace(**{
       d: catalog.load(d)
   for d in catalog.query(*search_terms)
    })
    return data

all_pri = yolo('c_pri')
```

**🐒 monkey patch it**

``` python
from functools import partial

catalog.yolo = yolo
catalog.yolo.__doc__ = "you only load once"

all_pri = catalog.yolo('c_pri')
```


### adding catalogs together

``` python
from kedro.io import DataCatalog
DataCatalog({**cat1.__dict__['_data_sets'], **cat2.__dict__['_data_sets']})
```
## 🛢 Building pipelines

![building pipelines](https://images.waylonwalker.com/roman-pentin-T5QT2bmiD4E-unsplash.jpg)
_Photo by roman pentin on Unsplash_

### 📍 Creating Nodes

``` python
from kedro.pipeline import node
node = node(lambda x: x.dropna(), inputs='raw_cars', outputs='int_cars')
```

``` python
from kedro.pipeline import node

def drop_columns(df, *columns):
   for column in columns:
      df = df.drop(columns=column)
   return df

node = node(
   lambda x: drop_columns(x, 'vs', 'am', 'gear', 'carb'),
   inputs='int_cars',
   outputs='pri_cars'
   )
```

### 🛢 Creating a pipeline

### Don't be so verbose

Create similar nodes dynamically

``` python
def halve_dataframe(data: pd.DataFrame) -> List[pd.DataFrame]:
   """ splits a dataframe in half """
    return np.array_split(data, 2)

nodes = []
datasets = [
   'cars', 'trucks', 'boats', 'motorcycles', 'planes',
   'ships', 'busses', 'trains', 'subways'
   ]

# creates a pipeline node for every dataset in the datasets list
for dataset in datasets
   nodes.append(
       node(halve_dataframe,
            'e_modin_{dataset}',
            ['train_{dataset}', 'test_{dataset}']),
   )
```

## 🏃‍♂️ Running Pipelines

![running pipelines](https://images.waylonwalker.com/rodion-kutsaev-xNdPWGJ6UCQ-unsplash.jpg)
_Photo by Rodion Kutsaev on Unsplash_

**🔖 filter by tags**

``` python
nodes = pipeline.only_nodes_with_tags('cars')
```

_see on_ [_#kedrotips_](https://twitter.com/_WaylonWalker/status/1195319044808888321?s=20)

**filter by node**

``` python
nodes = pipeline.only_nodes('b_int_cars')
```

_see on [#kedrotips](https://twitter.com/_WaylonWalker/status/1196406204479737856?s=20)

**filter nodes like**

``` python
query_string = 'cars'
nodes = [
   node.name
   for node in pipeline.nodes
   if query_string in node.name
   ]
pipeline.only_nodes(*nodes)
```

_see on_ [_#kedrotips_](https://twitter.com/_WaylonWalker/status/1196813895228428288?s=20)

**only nodes with tags** _or_

``` python
nodes = pipeline.only_nodes_with_tags('cars', 'trains')
```

**only nodes with tags** _and_

``` python
raw_nodes = pipeline.only_nodes_with_tags('raw')
car_nodes = pipeline.only_nodes_with_tags('cars')
raw_car_nodes = raw_nodes & car_nodes
```

``` python
raw_nodes = (
   pipeline
   .only_nodes_with_tags('raw')
   .only_nodes_with_tags('cars')
   )
```

**add pipelines**

``` python
car_nodes = pipeline.only_nodes_with_tags('cars')
train_nodes = pipeline.only_nodes_with_tags('trains')
transportation_nodes = car_nodes + train_nodes
```

**ensure nodes are attached**

``` python
cars_attached = len(
   pipeline
   .only_nodes_with_tags('cars')
   .grouped_nodes
   ) == 1
```

### 🎂 Pipeline Decorators

[example - log_time](https://kedro.readthedocs.io/en/latest/_modules/kedro/pipeline/decorators.html#log_time)

``` python
from kedro.pipeline.decorators import log_time, mem_profile
pipeline.decorate(log_running_time)
```

## Pipeline IO

`pipleine.all_inputs()` and `pipeline.all_outputs()` return sets of pipeline inputs and outputs and you can do set operations on them.  This is particularly useful to find the upper and lower edges of your pipeline or subset of pipeline.  The pipeline object here is any `kedro` pipeline including a filtered subset.

### Find all raw data

``` python
pipeline.all_inputs() - pipeline.all_outputs()
```

### Find all final data

``` python
pipeline.all_outputs() - pipeline.all_inputs()
```

### Find all nodes that do not raw

This one is probably one that is pushing the limits of what I would do in a list comprehension that I use in prod or even put into a text editor, but I commonly use ipython for my adhoc work and keeping it all in one line is very handy.  Complex list comprehensions kinda start becoming like regex in a way that they are really easy to write and really hard to read.  I don't think this one quite hits that point but its getting close.

I find this one super useful to help me either move data beween environments, or avoid unnecessary database calls.

``` python
raw_inputs = pipeline.all_inputs() - pipeline.all_outputs()
raw_nodes = [node for node in pipeline.nodes if [i for i in raw_inputs if i in set(node.inputs)] != []]
```
