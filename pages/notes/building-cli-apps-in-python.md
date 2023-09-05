---
templateKey: blog-post
tags: ["python"]
title: Building Cli apps in Python
date: 2019-11-11T06:00:00.000+00:00
published: true
description: learning about building cli apps in python
---

## Packages

## [Click](https://click.palletsprojects.com/en/7.x/ "Click")

### Inputs

Click primarily takes two forms of inputs Options and arguments. I think of options as keyword argument and arguments as regular positional arguments.

#### Option

- typically aliased with a shorthand ('-v', '--verbose')

---

\*\*From the [Docs](https://click.palletsprojects.com/en/7.x/options/)

To get the Python argument name, the chosen name is converted to lower case, up to two dashes are removed as the prefix, and other dashes are converted to underscores.

```python
@click.command()
@click.option('-s', '--string-to-echo')
def echo(string_to_echo):
    click.echo(string_to_echo)
```

```python
@click.command()
@click.option('-s', '--string-to-echo', 'string')
def echo(string):
    click.echo(string)
```

---

#### Argument

- positional
- required
- no help text supplied by click

## [Yaspin](https://pypi.org/project/yaspin/ "Yaspin")

![Yaspin Gif](https://images.waylonwalker.com/yaspin-demo.gif)

## [Click Help Colors](https://github.com/click-contrib/click-help-colors)

## ![Click Help Colors Example](https://raw.githubusercontent.com/r-m-n/click-help-colors/master/examples/1.png)

## [Colorama](https://github.com/tartley/colorama "colorama")

[Colorama Example](https://github.com/tartley/colorama/raw/master/screenshots/ubuntu-demo.png)

### [Click DidYouMean](https://github.com/click-contrib/click-didyoumean)
