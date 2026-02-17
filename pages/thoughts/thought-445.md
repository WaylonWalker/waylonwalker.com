---
title: '💭 casey/just: 🤖 Just a command runner'
date: 2024-12-14T17:04:06
templateKey: link
link: https://github.com/casey/just?tab=readme-ov-file#constants
tags:
  - bash
  - linux
  - just
published: true

---

> new versions of just now come with color variables already set.

``` bash
[group('manage')]
version:
    #!/usr/bin/env bash
    version=$(cat version)
    echo current version {{BOLD}}{{GREEN}}$version{{NORMAL}}
```

[Original thought](https://github.com/casey/just?tab=readme-ov-file#constants)
