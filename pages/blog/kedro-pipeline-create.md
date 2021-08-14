---
templateKey: blog-post
tags: ['kedro', 'python']
title: Kedro Pipeline Create
date: 2021-08-22T22:40:45
status: draft

---

Kedro pipeline create is a command that makes creating new
pipelines much easier.  There is much less boilerplate that
you need to write yourself.

## creating a new pipeline

The kedro cli comes with the following command to scaffold out
new pipelines.  Note that it will not add it to your
`pipeline_registry`, to be covered later, you will need to add
it yourself.

``` bash
kedro pipeline create example
```

## results

The directory structure that it creates looks like this.

``` bash
tree src/kedro_conda/pipelines
src/kedro_conda/pipelines
├── __init__.py
└── example
    ├── __init__.py
    ├── nodes.py
    ├── pipeline.py
    └── README.md
```

