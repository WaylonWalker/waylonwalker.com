---
title: '💭 Pin versions of dependencies · Issue #2200 · Kozea/WeasyPrint'
date: 2024-10-11T13:36:19
templateKey: link
link: https://github.com/Kozea/WeasyPrint/issues/2200
tags:
  - python
published: true

---

> weazyprint was throwing me some errors, turns out that it's currently not compatible with the latest pydyf package.

my error

``` python
TypeError: __init__() takes 1 positional argument but 3 were give
```

I fixed it by locking in pydyf at 0.8.0

``` txt
pydyf==0.8.0
```


[Original thought](https://github.com/Kozea/WeasyPrint/issues/2200)
