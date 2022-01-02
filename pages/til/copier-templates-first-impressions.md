---
date: 2022-01-03T12:37:32
templateKey: til
title: First impressions of copier templates
tags:
  - python
  - bash

---

I've been looking for a templating tool for awhile that works well with
single files.  My go to templating tool `cookiecutter` does not work for
single files, it needs to put files into a directory underneath of it.

## adding _envops

I was completely stuck for awhile.  copier was not replacing my template
variables.  I found out that adding all these `_endops` fixed it.

``` yaml
_templates_suffix: .jinja
_envops:
  block_end_string: "%}"
  block_start_string: "{%"
  comment_end_string: "#}"
  comment_start_string: "{#"
  keep_trailing_newline: true
  variable_end_string: "}}"
  variable_start_string: "{{"
```

> Later I read the docs and realized that copier defaults to using `[[`
> and `]]` for its templates unlike other tools like cookiecutter.


## template variables
