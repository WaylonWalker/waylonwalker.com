---
date: 2022-01-14 23:43:42.001865
templateKey: til
title: python functools total ordering
tags:
  - python
published: true

---

functools.total_ordering makes adding all of six of the rich comparison
operators to your custom classes much easier, and more likely that you
remember all of them.

> From the Docs: The class must define one of \_\_lt\_\_(), \_\_le\_\_(),
> \_\_gt\_\_(), or \_\_ge\_\_ In addition, the class should supply an
> \_\_eq\_\_() method.

one of these

* __lt__()
* __le__()
* __gt__()
* __ge__()

and required to have this one

* __eq__()

[Total Ordering Docs](https://docs.python.org/3/library/functools.html#functools.total_ordering)

Here is an example using the Enum I was working on the other day.

``` python
from enum import Enum, auto
from functools import total_ordering


@total_ordering
class LifeCycle(Enum):

    configure = auto()
    glob = auto()
    load = auto()
    pre_render = auto()
    render = auto()
    post_render = auto()
    save = auto()

    def __lt__(self, other):
        try:
            return self.value < other.value
        except AttributeError:
            return self.value < other

    def __eq__(self, other):
        try:
            return self.value == other.value
        except AttributeError:
            return self.value == other

```
