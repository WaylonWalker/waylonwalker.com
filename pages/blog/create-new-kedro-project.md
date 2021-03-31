---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Create New Kedro Project
date: 2020-03-02T12:09:00.000+00:00
status: published
description: Getting up and going with a brand new [kedro](https://kedro.readthedocs.io) project
  is super simple, thanks to the help of the `kedro new` command.  The ability to
  add an example pipeline from the start makes it that much easier to get going and
  have a template to follow for your own projects.
cover: "/static/create-new-kedro-project.png"

---
This is a quickstart to getting a new [kedro](https://kedro.readthedocs.io) pipeline up and running.  After this article you should be able to understand how to get started with [kedro](https://kedro.readthedocs.io).  You can learn more about this [Hello World Example](https://kedro.readthedocs.io/en/stable/02_getting_started/04_hello_world.html) in the [docs](https://kedro.readthedocs.io/en/stable/02_getting_started/04_hello_world.html)

🧹 Install [Kedro](https://kedro.readthedocs.io)

🛢 Create the Example Pipeline

💨 Run the example

📉 Show the pipeline visualization

## Create a Virtual Environment

I use conda to control my virtual environments and will create a new environment called `kedro_iris` with the following command.  **note** the latest compatible version of python is 3.7.

**EDIT**: as of kedro 0.16.0 kedro supports up to 3.8

``` bash
conda create -n kedro_iris python=3.8 -y
```

![](https://waylonwalker.com/conda-create-kedro-iris.gif)

Options

## Activate your conda environment

I try to keep my base environment as clean as possible.  I have ran into too many issues installing things in the base environment.  Almost always its some dependency that starts causing issues making it even harder to realize where its coming from as I never even installed it in base.

``` bash
source activate kedro_iris
```

## Install [Kedro](https://kedro.readthedocs.io)

Currently `kedro==0.15.5` is available on pypi and can be pip installed.

**EDIT** kedro is up to [![PyPI version](https://badge.fury.io/py/kedro.svg)](https://pypi.org/project/kedro/)

``` bash
pip install kedro
```

## Make sure you are in the directory that you want your project in

``` bash
cd /mnt/c/temp
```

## Create a new [Kedro](https://kedro.readthedocs.io) project

``` bash
kedro new
cd kedro-iris
git init
kedro install
```

![](https://waylonwalker.com/kedro-new-iris.gif)

## Run the pipeline

This will tell kedro to run your pipeline.  It will look at all of your nodes and determine the correct execution order for you, then run each one of them.  You can do this from a python script, python terminal session, or from the [kedro](https://kedro.readthedocs.io) cli.

> ✨ It will look at all of your nodes and determine the correct execution order for you

Lets run from the cli while in the same directory as kedro-iris

``` bash
kedro run
```

![](https://waylonwalker.com/kedro-new-iris.gif)

## Viz

[kedro-viz](https://github.com/quantumblacklabs/kedro-viz) is a priceless feature of [kedro](https://kedro.readthedocs.io).  It's like x-ray vision into your pipeline.  I can't imagine working without it after having it over the past year.  Unlike traditional documentation [kedro-viz](https://github.com/quantumblacklabs/kedro-viz) cannot lie to you.  It will help guarantee your changes line up properly, plan out adding nodes, and identify dependencies of deprecating nodes.

> Unlike traditional documentation [kedro-viz](https://github.com/quantumblacklabs/kedro-viz) cannot lie to you.

## Install [kedro-viz](https://github.com/quantumblacklabs/kedro-viz)

[kedro-viz](https://github.com/quantumblacklabs/kedro-viz) is also on pypi and can be installed just like any other python package with `pip`.

```bash
pip install kedro-viz
```

## Visualize the pipeline

[kedro-viz](https://github.com/quantumblacklabs/kedro-viz) is ran from the command line in the same directory as your kedro project.  There are ways to store your pipeline data as json, then load them from outside your project, but we will follow the standard practice for now.

``` bash
kedro viz
```

![](https://waylonwalker.com/kedro-viz-iris.gif)

## 🏗 Docker

There is another package that makes creating docker images from kedro projects super simple [kedro-docker](https://github.com/quantumblacklabs/kedro-docker).

If you dont already have docker installed on your machine, feel free to skip this section.

### install [kedro-docker](https://github.com/quantumblacklabs/kedro-docker)

``` bash
pip install kedro-docker
```

### build the image

``` bash
kedro docker build
```

### run the image

``` bash
kedro docker run
```

## Simple Huh

Getting up and going with a brand new [kedro](https://kedro.readthedocs.io) project is super simple, thanks to the help of the `kedro new` command.  The ability to add an example pipeline from the start makes it that much easier to get going and have a template to follow for your own projects.

## Recap

``` bash
conda create -n kedro_iris python=3.7 -y
source activate kedro_iris
pip install kedro
cd /mnt/c/temp
kedro new
# give it a project name Kedro Iris
# accept default package name kedro_iris
# addept default directory name kedro-iris
# yes for an example pipeline
cd kedro-iris
git init
git add .
git commit -m "initialized new kedro project"
kedro install
kedro run
pip install kedro-viz
kedro viz
pip install kedro-docker
kedro docker build
kedro docker run
```

## Other resources

The [kedro docs](https://kedro.readthedocs.io/) have a ton of great resources.  They are searchable, but can be a bit of an overwhelming amount of data.

I keep adding to my [kedro notes](https://waylonwalker.com/notes/kedro/) as I find new and interesting things.

I tweet out most of those snippets as I add them, you can find them all here [#kedrotips](https://twitter.com/search?q=%23kedrotips).

## More to come

I am planning to do more articles like this, you can stay up to date with them by following me on [dev.to](https://dev.to/waylonwalker), subscribing to my [rss feed](https://waylonwalker.com/rss.xml), or subscribe to my [newsletter](https://waylonwalker.com/newsletter)
