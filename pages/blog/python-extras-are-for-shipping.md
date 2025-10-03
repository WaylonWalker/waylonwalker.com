---
date: 2025-10-02 20:18:23
templateKey: blog
title: python extras are for shipping
published: true
tags:
  - python

---

Python has two ways of adding optional dependencies to your projects
pyproject.toml file `dependency-groups` and `optional-dependencies`.

## dependency-groups
_for development_

Dependency grooups are used when working on the project, they do not ship with
the project, users cannot select to install them with the project.  These are
for things like running tests, linting, or docs.  You might want to run these
in ci, or keep your dev machines tight.  For the most part you can probably
keep these in `dev`.  Depending on your team, fluency, and tolerance for slower
installs extra packages.  Adding too many tight groups might make it hard for
the team to remember all the groups and which one to use and end up with them
using `--all-groups` anyways.

## optional-dependencies
_for users_

Optional dependencies are for shipping.  These are for your users, not your
development team.  This is used for dependencies that are clearly not needed
for all or main use cases.  It is annoying to use projects that you need to add
optionals to just to use at all so use them a bit sparingly.

## example fastapi

[fastapi](https://github.com/fastapi/fastapi/blob/master/pyproject.toml)
provides a very simple example. `fastapi` itself provides almost everything you
need with optional-dependencies for `standard`,
`standard-no-fastapi-cloud-cli`, and `all`.  These primarily add support for
uvicorn websockets and multipart forms.

## example pandas

[Pandas](https://github.com/pandas-dev/pandas/blob/main/pyproject.toml) is a
very good example here.  As a data processing library there are a lot of
different sources for data that you might want to use, but you probably won't
need most of them, and often don't need them to [[ just ]] get a `DataFrame`
going.  They offer a long list of optional dependencies such as `pyarrow`,
`aws`, `gcp`, `postgresql` and many more.

## example kedro-datasets

Very similar to pandas `kedro-datasets` uses a similar pattern to pandas but at
a higher level.  A dataset is an abstraction of a datasource that get defined
in the catalog, and primarily provide the framework with `load` and `save`
methods for datasets. There are many optionals for data providers like pandas,
but also many for each dataframe abstraction like `pandas`, `polars`, `dask`,
`databricks`.

[kedro-datasets](https://github.com/kedro-org/kedro-plugins/blob/main/kedro-datasets/pyproject.toml)

## let's build a package

Let's make a package called `learn-uv` that implements these dependency features.

``` bash
mkdir /tmp/learn-uv
cd /tmp/learn-uv
uv init --package
uv add httpx
# add development dependencies
uv add --dev pytest
uv add --group dev ipython
# add documentation dependencies to the docs group
uv add --group docs markata

# add optional dependencies
# these are dependencies that a user could install
# python -m pip install 'learn-uv[data-science]'
uv add --optional data-science pandas

# add extra dependencies
# this adds the jupyter extra from rich
# similar to `python -m pip install 'learn-uv[jupyter]'`
uv add --extra jupyter rich
```

This will result in the following pyproject.toml.

``` pyproject.toml
[project]
name = "learn-uv"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Waylon S. Walker", email = "hello@waylonwalker.com" }
]
requires-python = ">=3.13"
dependencies = [
    # uv add httpx
    "httpx>=0.28.1",
    # uv add --extra jupyter rich
    "rich[jupyter]>=14.1.0",
]

[project.scripts]
learn-uv = "learn_uv:main"

[project.optional-dependencies]
data-science = [
    # uv add --optional data-science pandas
    "pandas>=2.3.3",
]

[build-system]
requires = ["uv_build>=0.8.22,<0.9.0"]
build-backend = "uv_build"

[dependency-groups]
dev = [
    # uv add --group dev ipython
    "ipython>=9.6.0",
    # uv add --dev pytest
    "pytest>=8.4.2",
]
docs = [
    # uv add --group docs markata
    "markata>=0.9.1",
]
```

## Using the project

Let's start off with one common point of confusion.  `uv tool run` or its alias
`uvx` does not install any dependencies or anything from the project.

``` bash
uv tool run ipython
```
* ✅ ipython
* ❌ learn_uv
* ❌ httpx
* ❌ pytest
* ❌ markata
* ❌ pandas
* ❌ rich
* ❌ ipywidgets (from rich[jupyter])

Using `uv run` is project aware, installs the dependencies from the
pyproject.toml.

``` bash
uv run ipython
```

* ✅ ipython
* ✅ learn_uv
* ✅ httpx
* ✅ pytest
* ❌ markata
* ❌ pandas
* ✅ rich
* ✅ ipywidgets (from rich[jupyter])

``` bash
uv run --group docs markata
```

* ✅ ipython
* ✅ learn_uv
* ✅ httpx
* ✅ pytest
* ✅ markata
* ❌ pandas
* ✅ rich
* ✅ ipywidgets (from rich[jupyter])


Installing the optional dependency extra `data-science` gives me `pandas` in
this project.

``` bash
uv run --extra data-science ipython
```
* ✅ ipython
* ✅ learn_uv
* ✅ httpx
* ✅ pytest
* ✅ markata
* ✅ pandas
* ✅ rich
* ✅ ipywidgets (from rich[jupyter])

## everything

There are many combinations of include/exclude that you can use, check `uv run
--help` to see all of the options.  Here is the nuclear option to include
everything.

``` bash
uv run --all-groups --all-extras ipython
```

## Potential `uv` bug

At the time of writing once a dependency group is used it persists in the
virtual environment for the rest of the project.

``` bash
❯ uv --version
uv 0.8.22 (ade2bdbd2 2025-09-23)
```

``` bash
# install docs group
uv sync --group docs
# docs dependencies are available
uv run markata
# sync resets the environment
uv sync
# docs dependencies are not available
uv run markata
error: Failed to spawn: `markata`
  Caused by: Permission denied (os error 13)
```
