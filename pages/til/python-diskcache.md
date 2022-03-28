---
date: 2022-03-30 16:47:36.688035
templateKey: til
title: How I setup a sqlite cache in python
tags:
  - python

---

When I need to cache some data between runs or share a cache accross multiple
processes my go to library in python is `diskcache`.  It's built on sqlite with
just enough cacheing niceties that make it very worth it.

## install diskcache

Install diskcache into your virtual environement of choice using pip from your command line.

```bash
python -m pip install diskcache
```

## setup the cache

```python
from diskcache import Cache
cache = FanoutCache('.mycache', statistics=True)
```

## Adding to the cache

``` python
cache.add('me',  )
```

## Reading from the cache

https://github.com/grantjenks/python-diskcache
https://grantjenks.com/docs/diskcache/
