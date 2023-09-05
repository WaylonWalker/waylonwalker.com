---
date: 2022-11-11 14:39:23
templateKey: til
title: formatme
published: false
tags:
  - markdown
---

```python
from kedro.pipeline import node

node(
    input="raw",
    output="int",
    func=my_func,
    tags=["one"],
)
```
