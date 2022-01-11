---
date: 2022-01-13 00:09:20.553265
templateKey: til
title: Implement --pdb in a python cli
tags:
  - python
  - python
  - python

---

To add a pdb flag `--pdb` to your applications you will need to wrap
your function call in a try/except, and start a post_mortem debugger.
[this stack overflow post](https://stackoverflow.com/questions/242485/starting-python-debugger-automatically-on-error)

``` python
import pdb, traceback, sys


def bombs():
    a = []
    print(a[0])


if __name__ == "__main__":
    if "--pdb" in sys.argv:
        try:
            bombs()
        except:
            extype, value, tb = sys.exc_info()
            traceback.print_exc()
            pdb.post_mortem(tb)
    else:
        bombs()
```
