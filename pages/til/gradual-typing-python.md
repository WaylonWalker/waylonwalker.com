---
date: 2022-01-21 14:27:32.053092
templateKey: til
title: Gradual Typing in Python
tags:
  - python

---

I've referenced a video from Anthony Sotile in passing conversation several
times.  Walking through his gradual typing process has really helped me
understand typing better, and has helped me make some projects better over time
rather than getting slammed with typing errors.

https://youtu.be/Rk-Y71P_9KE

# Step 1

Run Mypy as is, don't get fancy yet.  This will not reach into any functions
unless they are alreay explicitly typed.  It will not enforce you to type them
either.

``` bash
pip install mypy
mypy .
# or your specific project to avoid .venvs
mypy src
# or a single file
mypy my-script.py
```

## Step 2

Next we will add `check-untyped-defs`, this will start checking inside
functions that are not typed.

``` toml
[mypy]
check_untyped_defs = True
```

## Step 3

The final stage to this series is to add `disallow_untyped_defs`.  This will
start requiring all of your functions to be type hinted.  This one is probably
the toughest, because as you type functions mypy can uncover more issues for
you to fix.  Often times the list of errors grows before it shrinks.

``` toml
[mypy]
check_untyped_defs = True
```

## Anthony's video

https://www.youtube.com/watch?v=Rk-Y71P_9KE
