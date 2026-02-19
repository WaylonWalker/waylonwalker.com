---
title: '💭 casey/just: 🤖 Just a command runner'
date: 2024-12-14T17:04:06
template: link
link: https://github.com/casey/just?tab=readme-ov-file#constants
tags:
  - bash
  - linux
  - just
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/casey/just?tab=readme-ov-file#constants]]

new versions of just now come with color variables already set.

``` bash
[group('manage')]
version:
    #!/usr/bin/env bash
    version=$(cat version)
    echo current version {{BOLD}}{{GREEN}}$version{{NORMAL}}
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
