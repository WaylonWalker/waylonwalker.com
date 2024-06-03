---
date: 2022-01-13 00:09:20.553265
templateKey: til
title: Implement --pdb in a python cli
tags:
  - python

---

Adding a `--pdb` flag to your applications can make them much easier for
those using it to debug your application, especially if your applicatoin
is a cli application where the user has much fewer options to start this
for themselves.  To add a pdb flag `--pdb` to your applications you will
need to wrap your function call in a try/except, and start a post_mortem
debugger. I give credit to
[this stack overflow post](https://stackoverflow.com/questions/242485/starting-python-debugger-automatically-on-error)
for helping me figure this out.

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

## Using --pdb

``` python
python yourfile.py --pdb
```

![running this example with and without --pdb flag](https://images.waylonwalker.com/using-pdb-flag-from-cli.png)
