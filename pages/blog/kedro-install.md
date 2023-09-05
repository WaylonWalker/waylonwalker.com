---
templateKey: blog-post
tags: ['kedro', 'python']
title: Kedro Install
date: 2021-08-21T20:40:45
published: true

---

Kedro comes with an `install` command to install and manage all of your
projects dependencies.

https://youtu.be/IWimEs-hHQg

## cd into your project directory and activate env

You must start by having your kedro project either cloned down
from an existing project or created from kedro new.  Then
activate your environment.

https://waylonwalker.com/kedro-new/

> this post covers kedro new

https://waylonwalker.com/kedro-environment/

> This post covers creating your virtual environment for kedro

## install kedro

Make sure you have kedro installed in your current
environment, if you dont already have it.

``` bash
pip install kedro==0.17.4
```

## pip-tools

Kedro uses the `pip-tools` package under the hood to pin
dependencies in a very robust way to ensure that the project
will continue to work on everyone's machine day, including
production, day in and day out.  No matter what happens to the
dependencies you have installed.

### pip-compile

The command that kedro uses from `pip-tools` is `pip-compile`.  It will look at
what you have in a `requirements.in` file, compile the dependencies down to
exact versions, and create a requirements.txt that is fully pinned down, and
updatable by re-running `pip-compile`.

## requirements.in

If kedro does not see a `requirements.in` file it will automatically move your
`requirements.txt` to `requirements.in` and run `pip-compile`.

``` bash
No requirements.in found. Copying contents from requirements.txt...
```


## kedro install

Lets go ahead and run kedro install on one of the projects we already create
and environment for in a previous post, `kedro-conda`.

``` bash
kedro install
```

The first time you run this on a new repo it is likely that you will run into
this warning about creating a new `requirements.in` file.

``` bash
No requirements.in found. Copying contents from requirements.txt...
```

## kedro install flags

Kedro does let you avoid pip-compile all together, by using the
`--no-build-reqs` flag.

``` bash
kedro install --no-build-reqs
```

It also lets you upgrade all of your dependencies with build-reqs.  I would
reccomend doing this on its own branch, and own pull request.  If you are
working on a team you want everyone to be on the same page when it comes to
dependencies.  If you are not, you surely do not want something to break with a
new set of dependencies without a way of rolling back.

``` bash
kedro install --build-reqs
```
