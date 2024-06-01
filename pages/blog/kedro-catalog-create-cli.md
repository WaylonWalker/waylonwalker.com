---
templateKey: blog-post
tags: ['kedro', 'python']
title: kedro catalog create
date: 2021-11-15T07:18:55
published: true

---

I use `kedro catalog create` to boost my productivity by automatically
generating yaml catalog entries for me.  It will create new yaml files for each
pipeline, fill in missiing catalog entries, and respect already existing
catalog entries.  It will reformat the file, and sort it based on catalog key.

<https://youtu.be/_22ELT4kja4>

<!-- syntax highlighting broken after underscore from the link __ -->

[[ what-is-kedro ]]

> 👆 Unsure what kedro is?  Check out this post.

## Running Kedro Catalog Create

The command to ensure there are catalog entries for every dataset in the passed
in pipeline.

``` bash
kedro catalog create --pipeline history_nodes
```

* Create's new yaml file, if needed
* Fills in new dataset entries with the default dataset
* Keeps existing datasets untouched
* it will reformat your yaml file a bit
  * default sorting will be applied
  * empty newlines will be removed

## CONF_ROOT

Kedro will respect your `CONF_ROOT` settings when it creates a new catalog
file, or looks for existing catalog files.  You can change the location of your
configuration files by editing your `CONF_ROOT` variable in your projects.

`settings.py`.

``` python
# settings.py
# default settings
CONF_ROOT = "conf"

# I like to package my configuration
CONF_ROOT = str(Path(__file__).parent / "conf")
```

> I prefer to keep my configuration packaged inside of my project.  This is
> partly due to how my team operates and deploys pipelines.

## File Location

The `kedro catalog create` command will look for a `yaml` file based on the
name of the pipeline (`CONF_ROOT/catalog/<pipeline-name>.yml`).  If it does not
find one it will create one and make entries for each dataset in the pipeline.
It will not look in all of your existing catalog files for entries, only the
one in the exact file for your pipeline.  If you are going to use this command
its important that you follow this pattern or copy what it generates into your
own catalog file of choice.

> ⚠️ It will not look in all of your existing catalog files for entries, only the
one in the exact file for your pipeline.

## MemoryDataSet's

When you run `kedro catalog create` you get `MemoryDataSet`, that's it.  As of
`0.17.4` its hard coded into the library and not configurable.

``` yaml
range12:
  type: MemoryDataSet
```

## Your free to use what you want though

Let's switch this dataset over to a `pandas.CSVDataSet` so that the file gets
stored and we can pick up  and read the file without re-running the whole
pipeline.

``` yaml
range12:
  type: pandas.CSVDataSet
  filepath: data/range12.csv
```

## Continue adding nodes

As we work we will keep adding nodes to our kedro pipeline, in this case we
added another node that created a dataset called `range13`.

``` bash
kedro catalog create --pipeline history_nodes
```

After telling kedro to create new catalog entries for us we will see that it
left our `range12` entry alone and created `range13` for us.

``` yaml
range12:
  type: pandas.CSVDataSet
  filepath: data/range12.csv
range13:
  type: MemoryDataSet
```

## Formatting is not worthwhile

If we decide this is too cramped for us we could add some space between
datasets.  The next time we run `kedro catalog create` empty lines will be
removed.

``` yaml
range12:
  type: pandas.CSVDataSet

range13:
  type: MemoryDataSet
```

## Continuing to work

If we coninue adding new nodes, and tell kedro to create catalog entries again,
all of our effort given to formatting will be lost.  I wouldn't worry about it
unless you have an autoformatter that you can run on your yaml files.  The
productivity gains in an semi-automated catalog are worth it.

``` yaml
range12:
  type: pandas.CSVDataSet
  filepath: data/range12.csv
range121:
  type: MemoryDataSet
range13:
  type: MemoryDataSet
```

## Sorting Order

Notice the sorting order in the last entry, `range121` comes before `range13`.
This is all based on how pythons `yaml.safe_dump` works, kedro has set the
`default_flow_style` to `False`.  You can see where they write your file in the
source code currently
[here](https://github.com/quantumblacklabs/kedro/blob/master/kedro/framework/cli/catalog.py#L202)
