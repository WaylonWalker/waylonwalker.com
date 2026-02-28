---
title: '💭 valkey · PyPI'
date: 2025-02-17T02:22:12
template: link
link: https://pypi.org/project/valkey/
tags:
  - python
  - thoughts
  - thought
  - link
published: true

---

![[https://pypi.org/project/valkey/]]

python bindings for valkey, forked from redis.

one notable difference I see from redis is that you can install with libvalkey to autmatically get faster parsing support.

> For faster performance, install valkey with libvalkey support, this provides a compiled response parser, and for most cases requires zero code changes. By default, if libvalkey >= 2.3.2 is available, valkey-py will attempt to use it for response parsing.

``` bash
pip install "valkey[libvalkey]"
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
