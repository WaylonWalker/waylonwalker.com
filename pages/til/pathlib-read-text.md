---
date: 2022-03-20 17:19:00.327485
templateKey: til
title: How I read Files in Python
tags:
  - python

---

When I need to read contents from a plain text file in python I find the
easiest way is to just use `Pathlib`.

``` python
from pathlib import Path

Path('path_to_file').read_text()
```
