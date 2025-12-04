---
date: 2022-09-22 14:43:06
templateKey: til
title: Python direct dependencies in pyproject.toml
status: 'draft'
tags:
  - python

---

Hatch allows you to specify direct references for dependencies in your
`pyproject.toml` file. This is useful when you want to depend on a package that
is not available on PyPI or when you want to use a specific version from a Git
repository.  Often used for unreleased packages, or unreleased versions of
packages.

[docs](https://hatch.pypa.io/dev/config/dependency/#direct-references)

``` toml
[project]
dependencies = ['markata', 'markata-todoui@git+https://github.com/waylonwalker/markata-todoui']

[tool.hatch.metadata]
allow-direct-references=true
```
