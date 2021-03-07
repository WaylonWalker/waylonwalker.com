---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Kedro Catalog
date: 2020-07-24T05:00:00Z
status: published
description: I am exploring a kedro catalog meta data hook
cover: ''

---
I am exploring a kedro catalog meta data hook, these are some notes about what I am thinking.

## Process

* metadata will be attached to the dataset object under a `.metadata` attribute
* metadata will be updated `after_node_run`
* metadata will be empty until a pipeline is ran with the hook on
* optionally a function to add metadata will be added
* metadata will be stored in a file next to the `filepath`
* meta


## Problems This Hook Should solve

* what datasets have a columns with `sales` in the name
* what datasets were updated after last tuesday
* which pipeline node created this dataset
* how many rows are in this dataset (without reloading all datasets)


## implementation details

* metadata will be attached to each dataset as a dictionary
* list/dict comprehensions can be used to make queries

## Metadata to Capture

try pandas method -> try spark -> try dict/list -> none

* column names
* length
* Null count
* created_by node name


## Database?

Is there an easy way to create a nosql database in memory from a a list of dictionaries?

* [list-dict-DB](https://pypi.org/project/list-dict-DB/)
* [dataset](https://dataset.readthedocs.io/en/latest/)
* [TinyDB](https://tinydb.readthedocs.io/en/latest/)