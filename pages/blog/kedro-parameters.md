---
templateKey: blog-post
tags: ['kedro', 'python']
title: Setting Parameters in kedro
date: 2021-09-19
published: true

---

Parameters are a place for you to store variables for your pipeline that can be
accessed by any node that needs it, and can be easily changed by changing your
environment.  Parameters are stored in the repository in yaml files.

https://youtu.be/Jj5cQ5bqcjg

[[ what-is-kedro ]]

> 👆 Unsure what kedro is?  Check out this post.

## parameters files

You can have multiple parameters files and choose which ones to load by setting
your environment.  By default kedro will give you a `base` and `local`
parameters file.

* `conf/base/parameters.yml`
* `conf/local/parameters.yml`

## base

The base environment should contain all of the default values you want to run.

``` yaml
# /conf/base/parameters.yml
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

Parameters can be accessed through context or through the catalog.  Generally
when you are working with nodes it will be loaded through the catalog.

Loding with the context.

``` python
context = session.load_context()
context.params
```

Loading with the catalog.

``` python
catalog.load('parameters')
```

Loading a specific key with the catalog.

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

[[ kedro-node ]]

> 👆 Check out this complete guide to creating kedro nodes.

## local

The local parameters by default are in `conf/local/parameters.yml`.  They will
override the base parameters in a shallow fashion.  If a top level key exists
in local, it will override that entire key in your parameters.

``` yaml
# /conf/local/parameters.yml
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
# /conf/new/parameters.yml
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
* [what is kedro](https://waylonwalker.com/what-is-kedro/)
* [comprehensive guide to creating kedro nodes](https://waylonwalker.com/kedro-node/)
* [kedro playlist on YouTube](https://www.youtube.com/watch?v=bw5_FWDVRpU&list=PLTRNG6WIHETCoPt5gAKYSH_HCZvE_r41n)
* [configuration docs](https://kedro.readthedocs.io/en/latest/04_kedro_project_setup/02_configuration.html)
