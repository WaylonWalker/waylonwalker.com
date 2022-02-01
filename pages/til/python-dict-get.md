---
date: 2022-02-03 03:00:36.433916
templateKey: til
title: python dict get
tags:
  - python

---

For an embarassingly long time, til today, I have been wrapping my dict
gets with key errors in python.  I'm sure I've read it in code a bunch
of times, but just brushed over why you would use get.  That is until I
read a bunch of PR's from my buddy Nic and notice that he never gets
things with brackets and always with `.get`.  This turns out so much
cleaner to create a default case than try except.


## Example

Lets consider this example for prices of supplies.

```
prices = {'pen': 1.2, 'pencil', 0.3, 'eraser', 2.3}
```

```
try:
    paper_price = prices['paper']
except KeyError:
    paper_price = None
```

```
paper_price = prices.get('paper', None)
```

```
paper_sales = sales.get('paper', 0)
```
