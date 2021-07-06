---
templateKey: blog-post
tags: ['kedro', 'python']
title: Incremental Versioned Datasets in Kedro 
date: 2021-07-05T11:12:25
status: draft

---


## setup project

Setup a new project just as normal.  **note** I really like using pipx for
global cli packages.  You can pick a specific version of kedro or opt for the
latest while simply globally installing kedro and running kedro new is purely
dependent on the last time you chose to update kedro.


``` bash
pip install pipx

pipx run kedro new
cd versioned-partitioned-kedro-example
pip install kedro
kedro install
```

> I called my project versioned-partitioned-kedro-example

## update dependencies

I popped open my dependencies, added `kedro[pandas]` and `find-kedro`. As those
are extra packages our example will require.

```
aiohttp
black==21.5b1
find-kedro
flake8>=3.7.9, <4.0
ipython
isort~=5.0
jupyter_client>=5.1, <7.0
jupyterlab~=3.0
jupyter~=1.0
kedro-telemetry~=0.1.0
kedro==0.17.4
kedro[pandas]
nbstripout~=0.4
pytest-cov~=2.5
pytest-mock>=1.7.1, <2.0
pytest~=6.2
requests
wheel>=0.35, <0.37
```

**note** I created `find-kedro` and I really like using it to create my
pipeline object.  Think of how pytest automatically picks up everything named
`test`, `find-kedro` does the same thing for kedro.  It picks up everything
with `node` or `pipeline` in the name and creates pipelines out of it.

## create a node

For this example we need a node in order to do much.  This node is going to
simply pass the `cars.csv` from a url to a `parquet` file.  I am going to use a
lambda to build my identity function inline.

``` python
# pipelines/cars_nodes.py

from kedro.pipeline import node

nodes = []


nodes.append(
        node(
            func=lambda x:x,
            inputs='raw_cars',
            outputs='int_cars',
            name='create_int_cars',
            )
        )
```

> 🗒️ **note**`find-kedro`will automatically pick up these nodes for us after we
> set up our `pipeline_registry.py`.

## implement find-kedro

Next we need to tell kedro where our nodes are.  This is is where `find-kedro`
comes in.  Here we simply point to the directory where our modules of
nodes/pipelines are and it does the rest automatically. 

``` python
# pipeline_registry.py

"""Project pipelines."""
from typing import Dict
from pathlib import Path

from kedro.pipeline import Pipeline

from find_kedro import find_kedro


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    pipeline_dir = Path(__file__).parent / 'pipelines'
    return find_kedro(directory= pipeline_dir)
```

> 🗒️ This is very similar to the default `pipeline_registry`except the last two
> lines.

## create a baseline catalog

Once we have a pipeline setup the kedro cli can automatically fill in missing
catalog entries for us with  `MemoryDataSet`'s for us.  This helps scaffold the
catalog in a consistent way, and ensre we don't end up with a typo in our
dataset name.


``` bash
kedro catalog create --pipeline cars_nodes
```

Kedro will kick out the following catalog file to `base/catalog/cars_nodes.yml`
for us to get started with.

``` yaml
raw_cars:
  type: MemoryDataSet
int_cars:
  type: MemoryDataSet
```

> 🔥 use the kedro cli to automatically fill in any missing datasets from the
> catalog.


## make a versioned dataset

``` yaml
raw_cars:
  type: pandas.CSVDataSet
  filepath: https://waylonwalker.com/cars.csv
int_cars:
  type: pandas.ParquetDataSet
  filepath: data/int_cars.parquet
  versioned: true
```


## run the pipeline

Once we have the nodes and catalog setup, we can run the pipeline a few times
to get some versioned data.  Each time we run it will save a new version inside
of the `int_cars.parquet` directory.

``` bash 
kedro run
```

## inspect the data

listing the files in `data/int_cars.parquet` shows that I now have 5 different
datasets available.  I can load old ones, but by default kedro will load the
latest one.


``` bash
ls data/int_cars.parquet

2021-07-05T15.24.53.164Z
2021-07-05T15.29.56.144Z
2021-07-05T15.30.23.101Z
2021-07-05T15.30.26.555Z
2021-07-05T15.31.12.688Z
```

> 🗒️ kedro sets the version at the timestamp that the session is started.  All
> datasets created within the same run will have the same version.

## stack on a incremental dataset

This is where things get interesting, kedro comes with an incremental dataset
that will load all of the files from a particular directory into a dictionary
wher the keys are the filename that was loaded.  To load up all datasets into
this dictionary all we need to do is add a new catalog entry that is a  `type:
PartitionedDataSet`, with a `path` pointing to the same place as the original,
and a `dataset` type the same as the original.

``` yaml
int_cars_partitioned:
  type: PartitionedDataSet
  dataset: pandas.ParquetDataSet
  path: data/int_cars.parquet

```

## catalog list

Listing the catalog entries confirms that we have successfully added our new `PartitionedDataSet`.


``` python
In [17]: context.catalog.list()
Out[17]:
['raw_cars',
 'int_cars',
 'int_cars_partitioned',
 'parameters']
```


## loading an incremental dataset

Now we can easily load the datasets from every run we just did into a single
dictionary, simply by running `context.catalog.load('int_cars_incremental')`

``` python
In [19]: context.catalog.load('int_cars_incremental')
2021-07-05 11:32:40,534 - kedro.io.data_catalog - INFO - Loading data from `int_cars_incremental` (IncrementalDataSet)...
Out[19]:
{'2021-07-05T15.29.56.144Z/int_cars.parquet':              Unnamed: 0   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
 0             Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
 1         Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
 2            Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
 3        Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
 4     Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2
 5               Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0     3     1
 6            Duster 360  14.3    8  360.0  245  3.21  3.570  15.84   0   0     3     4
 7             Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0     4     2
 8              Merc 230  22.8    4  140.8   95  3.92  3.150  22.90   1   0     4     2
 9              Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0     4     4
 10            Merc 280C  17.8    6  167.6  123  3.92  3.440  18.90   1   0     4     4
 11           Merc 450SE  16.4    8  275.8  180  3.07  4.070  17.40   0   0     3     3
 12           Merc 450SL  17.3    8  275.8  180  3.07  3.730  17.60   0   0     3     3
 13          Merc 450SLC  15.2    8  275.8  180  3.07  3.780  18.00   0   0     3     3
 14   Cadillac Fleetwood  10.4    8  472.0  205  2.93  5.250  17.98   0   0     3     4
 15  Lincoln Continental  10.4    8  460.0  215  3.00  5.424  17.82   0   0     3     4
 16    Chrysler Imperial  14.7    8  440.0  230  3.23  5.345  17.42   0   0     3     4
 17             Fiat 128  32.4    4   78.7   66  4.08  2.200  19.47   1   1     4     1
 18          Honda Civic  30.4    4   75.7   52  4.93  1.615  18.52   1   1     4     2
 19       Toyota Corolla  33.9    4   71.1   65  4.22  1.835  19.90   1   1     4     1
 20        Toyota Corona  21.5    4  120.1   97  3.70  2.465  20.01   1   0     3     1
 21     Dodge Challenger  15.5    8  318.0  150  2.76  3.520  16.87   0   0     3     2
 22          AMC Javelin  15.2    8  304.0  150  3.15  3.435  17.30   0   0     3     2
 23           Camaro Z28  13.3    8  350.0  245  3.73  3.840  15.41   0   0     3     4
 24     Pontiac Firebird  19.2    8  400.0  175  3.08  3.845  17.05   0   0     3     2
 25            Fiat X1-9  27.3    4   79.0   66  4.08  1.935  18.90   1   1     4     1
 26        Porsche 914-2  26.0    4  120.3   91  4.43  2.140  16.70   0   1     5     2
 27         Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.90   1   1     5     2
 28       Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.50   0   1     5     4
 29         Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.50   0   1     5     6
 30        Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.60   0   1     5     8
 31           Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.60   1   1     4     2,
 '2021-07-05T15.30.23.101Z/int_cars.parquet':              Unnamed: 0   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
 0             Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
 1         Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
 2            Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
 3        Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
 4     Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2
 5               Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0     3     1
 6            Duster 360  14.3    8  360.0  245  3.21  3.570  15.84   0   0     3     4
 7             Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0     4     2
 8              Merc 230  22.8    4  140.8   95  3.92  3.150  22.90   1   0     4     2
 9              Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0     4     4
 10            Merc 280C  17.8    6  167.6  123  3.92  3.440  18.90   1   0     4     4
 11           Merc 450SE  16.4    8  275.8  180  3.07  4.070  17.40   0   0     3     3
 12           Merc 450SL  17.3    8  275.8  180  3.07  3.730  17.60   0   0     3     3
 13          Merc 450SLC  15.2    8  275.8  180  3.07  3.780  18.00   0   0     3     3
 14   Cadillac Fleetwood  10.4    8  472.0  205  2.93  5.250  17.98   0   0     3     4
 15  Lincoln Continental  10.4    8  460.0  215  3.00  5.424  17.82   0   0     3     4
 16    Chrysler Imperial  14.7    8  440.0  230  3.23  5.345  17.42   0   0     3     4
 17             Fiat 128  32.4    4   78.7   66  4.08  2.200  19.47   1   1     4     1
 18          Honda Civic  30.4    4   75.7   52  4.93  1.615  18.52   1   1     4     2
 19       Toyota Corolla  33.9    4   71.1   65  4.22  1.835  19.90   1   1     4     1
 20        Toyota Corona  21.5    4  120.1   97  3.70  2.465  20.01   1   0     3     1
 21     Dodge Challenger  15.5    8  318.0  150  2.76  3.520  16.87   0   0     3     2
 22          AMC Javelin  15.2    8  304.0  150  3.15  3.435  17.30   0   0     3     2
 23           Camaro Z28  13.3    8  350.0  245  3.73  3.840  15.41   0   0     3     4
 24     Pontiac Firebird  19.2    8  400.0  175  3.08  3.845  17.05   0   0     3     2
 25            Fiat X1-9  27.3    4   79.0   66  4.08  1.935  18.90   1   1     4     1
 26        Porsche 914-2  26.0    4  120.3   91  4.43  2.140  16.70   0   1     5     2
 27         Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.90   1   1     5     2
 28       Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.50   0   1     5     4
 29         Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.50   0   1     5     6
 30        Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.60   0   1     5     8
 31           Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.60   1   1     4     2,
 '2021-07-05T15.30.26.555Z/int_cars.parquet':              Unnamed: 0   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
 0             Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
 1         Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
 2            Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
 3        Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
 4     Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2
 5               Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0     3     1
 6            Duster 360  14.3    8  360.0  245  3.21  3.570  15.84   0   0     3     4
 7             Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0     4     2
 8              Merc 230  22.8    4  140.8   95  3.92  3.150  22.90   1   0     4     2
 9              Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0     4     4
 10            Merc 280C  17.8    6  167.6  123  3.92  3.440  18.90   1   0     4     4
 11           Merc 450SE  16.4    8  275.8  180  3.07  4.070  17.40   0   0     3     3
 12           Merc 450SL  17.3    8  275.8  180  3.07  3.730  17.60   0   0     3     3
 13          Merc 450SLC  15.2    8  275.8  180  3.07  3.780  18.00   0   0     3     3
 14   Cadillac Fleetwood  10.4    8  472.0  205  2.93  5.250  17.98   0   0     3     4
 15  Lincoln Continental  10.4    8  460.0  215  3.00  5.424  17.82   0   0     3     4
 16    Chrysler Imperial  14.7    8  440.0  230  3.23  5.345  17.42   0   0     3     4
 17             Fiat 128  32.4    4   78.7   66  4.08  2.200  19.47   1   1     4     1
 18          Honda Civic  30.4    4   75.7   52  4.93  1.615  18.52   1   1     4     2
 19       Toyota Corolla  33.9    4   71.1   65  4.22  1.835  19.90   1   1     4     1
 20        Toyota Corona  21.5    4  120.1   97  3.70  2.465  20.01   1   0     3     1
 21     Dodge Challenger  15.5    8  318.0  150  2.76  3.520  16.87   0   0     3     2
 22          AMC Javelin  15.2    8  304.0  150  3.15  3.435  17.30   0   0     3     2
 23           Camaro Z28  13.3    8  350.0  245  3.73  3.840  15.41   0   0     3     4
 24     Pontiac Firebird  19.2    8  400.0  175  3.08  3.845  17.05   0   0     3     2
 25            Fiat X1-9  27.3    4   79.0   66  4.08  1.935  18.90   1   1     4     1
 26        Porsche 914-2  26.0    4  120.3   91  4.43  2.140  16.70   0   1     5     2
 27         Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.90   1   1     5     2
 28       Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.50   0   1     5     4
 29         Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.50   0   1     5     6
 30        Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.60   0   1     5     8
 31           Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.60   1   1     4     2,
 '2021-07-05T15.31.12.688Z/int_cars.parquet':              Unnamed: 0   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
 0             Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
 1         Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
 2            Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
 3        Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
 4     Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2
 5               Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0     3     1
 6            Duster 360  14.3    8  360.0  245  3.21  3.570  15.84   0   0     3     4
 7             Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0     4     2
 8              Merc 230  22.8    4  140.8   95  3.92  3.150  22.90   1   0     4     2
 9              Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0     4     4
 10            Merc 280C  17.8    6  167.6  123  3.92  3.440  18.90   1   0     4     4
 11           Merc 450SE  16.4    8  275.8  180  3.07  4.070  17.40   0   0     3     3
 12           Merc 450SL  17.3    8  275.8  180  3.07  3.730  17.60   0   0     3     3
 13          Merc 450SLC  15.2    8  275.8  180  3.07  3.780  18.00   0   0     3     3
 14   Cadillac Fleetwood  10.4    8  472.0  205  2.93  5.250  17.98   0   0     3     4
 15  Lincoln Continental  10.4    8  460.0  215  3.00  5.424  17.82   0   0     3     4
 16    Chrysler Imperial  14.7    8  440.0  230  3.23  5.345  17.42   0   0     3     4
 17             Fiat 128  32.4    4   78.7   66  4.08  2.200  19.47   1   1     4     1
 18          Honda Civic  30.4    4   75.7   52  4.93  1.615  18.52   1   1     4     2
 19       Toyota Corolla  33.9    4   71.1   65  4.22  1.835  19.90   1   1     4     1
 20        Toyota Corona  21.5    4  120.1   97  3.70  2.465  20.01   1   0     3     1
 21     Dodge Challenger  15.5    8  318.0  150  2.76  3.520  16.87   0   0     3     2
 22          AMC Javelin  15.2    8  304.0  150  3.15  3.435  17.30   0   0     3     2
 23           Camaro Z28  13.3    8  350.0  245  3.73  3.840  15.41   0   0     3     4
 24     Pontiac Firebird  19.2    8  400.0  175  3.08  3.845  17.05   0   0     3     2
 25            Fiat X1-9  27.3    4   79.0   66  4.08  1.935  18.90   1   1     4     1
 26        Porsche 914-2  26.0    4  120.3   91  4.43  2.140  16.70   0   1     5     2
 27         Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.90   1   1     5     2
 28       Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.50   0   1     5     4
 29         Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.50   0   1     5     6
 30        Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.60   0   1     5     8
 31           Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.60   1   1     4     2}
```

## stack on a partitioned dataset

``` yaml
int_cars_incremental:
  type: IncrementalDataSet
  dataset: pandas.ParquetDataSet
  path: data/int_cars.parquet
```

## loading an partitioned dataset

``` python
In [18]: context.catalog.load('int_cars_partitioned')
2021-07-05 11:31:11,253 - kedro.io.data_catalog - INFO - Loading data from `int_cars_partitioned` (PartitionedDataSet)...
Out[18]:
{'2021-07-05T15.29.56.144Z/int_cars.parquet': <bound method AbstractVersionedDataSet.load of <kedro.extras.datasets.pandas.parquet_dataset.ParquetDataSet object at 0x7f4bb1570820>>,
 '2021-07-05T15.30.23.101Z/int_cars.parquet': <bound method AbstractVersionedDataSet.load of <kedro.extras.datasets.pandas.parquet_dataset.ParquetDataSet object at 0x7f4bb1570850>>,
 '2021-07-05T15.30.26.555Z/int_cars.parquet': <bound method AbstractVersionedDataSet.load of <kedro.extras.datasets.pandas.parquet_dataset.ParquetDataSet object at 0x7f4bb1570910>>,
 '2021-07-05T15.31.12.688Z/int_cars.parquet': <bound method AbstractVersionedDataSet.load of <kedro.extras.datasets.pandas.parquet_dataset.ParquetDataSet object at 0x7f4bb15709a0>>}
```

## incremental vs. partitioned

* incremental loads the data
* partitioned give a load function

## creating nodes with partitioned datasets

```python
def timeseries_partitioned(cars: Dict):
    return {k:len(car()) for k, car in cars.items()}

nodes.append(
        node(
            func=timeseries_partitioned,
            inputs='int_cars_partitioned',
            outputs='int_cars_timeseries_partitioned',
            name='create_int_cars_timeseries_partitioned',
            )
        )
```

## creating nodes with incremental datasets

```python
def timeseries_incremental(cars: Dict):
    return {k:len(car) for k, car in cars.items()}

nodes.append(
        node(
            func=timeseries_incremental,
            inputs='int_cars_incremental',
            outputs='int_cars_timeseries_incremental',
            name='create_int_cars_timeseries_incremental',
            )
        )
```



## Loading the new datasets

``` python
In [32]: context.catalog.load('int_cars_timeseries_incremental')
2021-07-05 12:00:55,014 - kedro.io.data_catalog - INFO - Loading data from `int_cars_timeseries_incremental` (PickleDataSet)...
Out[32]:
{'2021-07-05T15.29.56.144Z/int_cars.parquet': 32,
 '2021-07-05T15.30.23.101Z/int_cars.parquet': 32,
 '2021-07-05T15.30.26.555Z/int_cars.parquet': 32,
 '2021-07-05T15.31.12.688Z/int_cars.parquet': 32,
 '2021-07-05T16.43.43.088Z/int_cars.parquet': 32}

In [33]: context.catalog.load('int_cars_timeseries_partitioned')
2021-07-05 12:01:03,223 - kedro.io.data_catalog - INFO - Loading data from `int_cars_timeseries_partitioned` (PickleDataSet)...
Out[33]:
{'2021-07-05T15.29.56.144Z/int_cars.parquet': 32,
 '2021-07-05T15.30.23.101Z/int_cars.parquet': 32,
 '2021-07-05T15.30.26.555Z/int_cars.parquet': 32,
 '2021-07-05T15.31.12.688Z/int_cars.parquet': 32,
 '2021-07-05T16.43.43.088Z/int_cars.parquet': 32,
 '2021-07-05T16.50.46.686Z/int_cars.parquet': 32}

```


