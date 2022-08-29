---
date: 2022-09-01 13:19:22
templateKey: til
title: Versioning Python Projects with Hatch
status: 'draft'
tags:
  - python

---

## project layout

``` bash
❯ tree .
.
├── pkg
│   ├── __about__.py
│   └── __init__.py
├── pyproject.toml
└── README.md

1 directory, 4 files
```

## pyproject.toml

``` toml
[project]
name = "pkg"
description = "Show how to version packages with hatch"
readme = "README.md"
dynamic = [
 "version",
]

[build-system]
requires = [
 "hatchling>=1.4.1",
]
build-backend = "hatchling.build"

[tool.hatch.version]
path = "pkg/__about__.py"
```

## __about__.py

``` python
__version__ = "0.0.0"
```

## versioning

## Example

![hatch-version-cli](https://screenshots.waylonwalker.com/hatch-version-cli.webp)
