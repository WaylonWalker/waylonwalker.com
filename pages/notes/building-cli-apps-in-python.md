---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Building Cli apps in Python
date: 2019-11-11T06:00:00.000+00:00
status: published
description: learning about building cli apps in python
cover: "/static/jp-valery-6W9G5G2WXGY-unsplash.jpg"

---
## Packages

## [Click](https://click.palletsprojects.com/en/7.x/ "Click")

### Inputs

Click primarily takes two forms of inputs Options and arguments.  I think of options as keyword argument and arguments as regular positional arguments.

#### Option

* typically aliased with a shorthand ('-v', '--verbose')

---

**From the [Docs](https://click.palletsprojects.com/en/7.x/options/)

To get the Python argument name, the chosen name is converted to lower case, up to two dashes are removed as the prefix, and other dashes are converted to underscores.

``` python
@click.command()
@click.option('-s', '--string-to-echo')
def echo(string_to_echo):
    click.echo(string_to_echo)
```

``` python
@click.command()
@click.option('-s', '--string-to-echo', 'string')
def echo(string):
    click.echo(string)
```

---

#### Argument

* positional
* required
* no help text supplied by click

## [Yaspin](https://pypi.org/project/yaspin/ "Yaspin")

![Yaspin Gif](https://warehouse-camo.cmh1.psfhosted.org/1bf73e6062750b03a63648f4cab5147b82e4be97/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f706176646d79742f79617370696e2f6d61737465722f676966732f64656d6f2e676966)

## [Click Help Colors](https://github.com/click-contrib/click-help-colors)

## ![Click Help Colors Example](https://raw.githubusercontent.com/r-m-n/click-help-colors/master/examples/1.png)

## [Colorama](https://github.com/tartley/colorama "colorama")

[Colorama Example](https://github.com/tartley/colorama/raw/master/screenshots/ubuntu-demo.png)

### [Click DidYouMean](https://github.com/click-contrib/click-didyoumean)