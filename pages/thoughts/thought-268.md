---
title: '💭 Hatch v1.10.0 - Hatch'
date: 2024-05-02T14:06:57
templateKey: link
link: https://hatch.pypa.io/latest/blog/2024/05/02/hatch-v1100/
tags:
  - python
published: true

---

> Hatch be flyin.

This new release of hatch includes support for the new package installer `uv` which is just mind blowing fast compared to anything else we have in python right now.

``` toml
[tool.hatch.envs.default]
installer = "uv"
```

The other features are cool too, check them out.  I'll probably be using the test runner, but I've been waiting for the uv support since uv launched.

[Original thought](https://hatch.pypa.io/latest/blog/2024/05/02/hatch-v1100/)
