---
date: 2022-04-01 01:21:30.473713
templateKey: til
title: Don't inherit from python BaseException, Here's why.
tags:
  - python

---

## You cannot Keybard interrupt

```python
from time import sleep

while True:
    try:
        sleep(30)
    except BaseException:
        pass
```


```python
from time import sleep

while True:
    try:
        sleep(30)
    except BaseException:
        pass
```
