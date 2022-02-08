---
date: 2022-02-08 13:54:08.037131
templateKey: til
title: ag silver searcher look ahead and look behind
tags:
  - cli
  - bash
  - linux

---

A super useful tool when doing PR's or checking your own work during a big
refactor is the silver searcher.  Its a super fast command line based searching
tool. You just run `ag "<search term>"` to search for your search term.  This
will list out every line of every file in any directory under your current
working directory that contains a match.

## Ahead/Behind

It's often useful to need some extra context around the change.  I recently
reviewed a bunch of PR's that moved schema from `save_args` to the root of the
dataset in all yaml configs.  To ensure they all made it to the top level
DataSet configuraion, and not underneath save_args.  I can do a search for all
the schemas, and ensure that none of them are under `save_args` anymore.

``` bash
ag "schema: " -A 12 -B 12
```
