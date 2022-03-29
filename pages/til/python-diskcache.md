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

There are a couple of different types of cache, `Cache`, `FanoutCache`,
and `DjangoCache`, you can read more about those in the
[docs](https://grantjenks.com/docs/diskcache)

```python
from diskcache import Cache
cache = FanoutCache('.mycache', statistics=True)
```



## Adding to the cache

Adding to the cache only needs a key and value.

``` python
cache.add('me', 'waylonwalker' )
```

## Set the expire time

Optionally you can set the seconds before it expires.  The cache invalidation
tools like this is what really makes diskcache shine over using raw sqlite or
any sort of static file.

``` python
cache.add('me', 'waylonwalker', expire=60)
```

## tagging

Diskcache supports tagging entries added to the cache.

``` python
# add an item to the cache with a tag
cache.add('me', 'waylonwalker', expire=60, tag='people')
```

This seems to let you do a few new things like getting items from the cache by
both key and tag, or evict all tags from the cache.

``` python
# evict all items tagged as 'people' from the cache
cache.evict(tag='people')
```

## Reading from the cache

You can read from the cache by using the `.get` method and giving it the key
you want to retrieve.

```python
who = cache.get('me')
# who == 'waylonwalker'
```

## Cache Misses

Cache misses will return a `None` just like any dictionary `.get` miss.

```
missed = cache.get('missing')
# missed == None
```

## ⭐

Give Grant some love and give
[grantjenks/python-diskcache](https://github.com/grantjenks/python-diskcache) a
⭐.
