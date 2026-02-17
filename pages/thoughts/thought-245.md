---
title: '💭 inline-snapshot'
date: 2024-04-17T18:37:15
templateKey: link
link: https://15r10nk.github.io/inline-snapshot/
tags:
  - python
  - testing
published: true

---

> This is a cool snapshot testing tool that automatically creates, and updates test values for you.

Starting with some test code.

``` python
from inline_snapshot import snapshot


def something():
    return 1548 * 18489


def test_something():
    assert something() == snapshot()
```

now if I run `pytest` my tests will fail because my assert will fail, but if I run `pytest --inline-snapshot=create` it will fill out my snapshot values and the file will then look like this.

``` python
from inline_snapshot import snapshot


def something():
    return 1548 * 18489


def test_something():
    assert something() == snapshot(28620972)
```

[Original thought](https://15r10nk.github.io/inline-snapshot/)
