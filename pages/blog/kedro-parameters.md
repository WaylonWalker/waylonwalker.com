---
templateKey: blog-post
tags: ['kedro', 'python']
title: Setting Parameters in kedro
date: 2021-08-29
status: draft

---

## base

The base environment should contain all of the default values you want to run.

``` yaml
test_size: 0.2
random_state: 3
features:
  - engines
  - passenger_capacity
  - crew
  - d_check_complete
  - moon_clearance_complete
  - iata_approved
  - company_rating
  - review_scores_rating
```

> **NOTE** base will always be loaded first.

## accessing parameters

``` python
context = session.load_context()
context.params
```

``` python
catalog.load('parameters')
```

``` python
catalog.load('params:test_size')
```

## using parameters in nodes

Here is an example from the complete spaceflights demo.  The entire parameters
dict is passed in, then the `features` key is accessed.

``` python
def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters.yml.
    Returns:
        Split data.
    """
    X = data[parameters["features"]]
    y = data["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test
```


## local

The local parameters by default are in `conf/local/parameters.yml`.  They will
override the base parameters in a shallow fashion.  If a top level key exists
in local, it will override that entire key in your parameters.

``` yaml
env: local
features:
  - company_rating
  - review_scores_rating
```

> **NOTE** If you have not explicitly set your environment, local will be the
default environment selected to override base.

## env

You can also have other environments that override the base environment.

``` yaml
env: new
```

> **NOTE** if you use an env local will not be applied

## Activating this environment

Following the [configuration docs](https://kedro.readthedocs.io/en/latest/04_kedro_project_setup/02_configuration.html)
we can activate the environment by setting an environment variable in our shell
or passing in --env to our kedro cli command.

Setting an environment variable.

``` bash
export KEDRO_ENV=test
```

Passing in the env to a kedro cli command.

``` bash
kedro run --env=test
```

Setting the Environment Variable in python.

``` python
import os
os.environ['KEDRO_ENV'] = 'new'
```

## Links

* [all of my kedro articles](https://waylonwalker.com/kedro/)
* [kedro playlist on YouTube](https://www.youtube.com/watch?v=bw5_FWDVRpU&list=PLTRNG6WIHETCoPt5gAKYSH_HCZvE_r41n)
* [configuration docs](https://kedro.readthedocs.io/en/latest/04_kedro_project_setup/02_configuration.html)

