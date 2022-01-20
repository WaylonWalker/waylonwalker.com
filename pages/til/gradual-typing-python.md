---
date: 2022-01-22 14:27:32.053092
templateKey: til
title: Gradual Typing in Python
tags:
  - python
  - python
  - python

---

# Step 1

Run Mypy as is.

``` bash
pip install mypy
mypy .
# or your specific project to avoid .venvs
mypy src
# or a single file
mypy my-script.py
```

## Step 2

add `check-untyped-defs`, this will start checking inside functions
that are not typed.

``` toml
[mypy]
check_untyped_defs = True
```

## Step 3

add `disallow_untyped_defs`

``` toml
[mypy]
check_untyped_defs = True
```

## Anthony's video

https://www.youtube.com/watch?v=Rk-Y71P_9KE
