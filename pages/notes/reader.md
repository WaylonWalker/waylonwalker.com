---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Reader
date: 2020-07-12T05:00:00.000+00:00
status: published
description: Notes about my reader idea
cover: ""

---

# Inputs

The input will be a yaml file containing a list of `Items` you want to stay up to date with.  Inside each item will be a url, and weight.


``` yaml
email:
    max-entries: 10
    recipients:
      - waylon@waylonwalker.com
markdown:
    max-entries: 100
    output:
        - README.md
json:
    max-entries: 1000
    output:
        - feeds/feed.json
rss:
    max-entries: 1000
    output:
        - feeds/feed.xml
html:
    max-entries: 100
    output:
        index.html

items:
    Waylon Walker:
    weight: 5
    url: https://waylonwalker.com/rss.xml
    @_WaylonWalker:
    weight: 3
    twitter: https://twitter.com/_waylonwalker
    DEV Waylon Walker:
    weight: 8
    url: https://dev.to/waylonwalker
    Stack Overflow Kedro:
    weight: 5
    url: https://stackoverflow.com/questions/tagged/kedro
    Kedro GitHub:
    weight: 4
    url: https://github.com/quantumblacklabs/kedro
    Kedro Pypi
        weight: 10
        url: https://pypi.org/project/kedro/
```


# Types

* rss feed (primary source)
* youtube feed
* Stack Overflow tags
* GitHub repo activity
* pypi release
* dev.to post
* Twitter Search # user will need an api key

# Methodology

Each url will be pulled in and parsed into a standard data scructure.  Some items may yield special feaures, a schemaless/nosql datastructure may be best.  Pipeline will decide to how to weight posts based on users weight, recent position on feed, .

```
a_raw (raw plain text / json items) -> b_int (cleaned items) -> c_pri (single feed of items) -> d_fea (weighted feed of items) -> e_out (requested output formats)
```

## output

Pipeline outputs will be email, json, markdown, xml, html.  Each will be able to be configured by the config file (max-entries, output location).


## Running

Users will be able to create their own reader.  Here is a list of possiblilites.  Users will not have the pipeline inside their repo. It will pull the pipeline from a package repo, pypi, dockerhub, GitHub.

* fork a template repo (might be cumbersome to update)
* use a GitHub action from the Marketplace (easier to update)
* GH actions will run the pipeline on a schedule
