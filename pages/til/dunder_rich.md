---
date: 2021-12-23T19:34:18
templateKey: til
title: fugitive verbose commit
tags:
  - python
  - rich

---

Adding a `__render__` method that returns a rich renderable to any python class
makes it display this output if printed with rich.  This also includes being
nested inside of a rich Layout.

``` python
import rich
from rich.panel import Panel


class ShowMe:
    def __rich__(self):
        return Panel("hello", border_style="gold1")


if __name__ == "__main__":
    rich.print(ShowMe())
```
