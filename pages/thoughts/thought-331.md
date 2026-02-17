---
title: '💭 DiskCache API Reference — DiskCache 5.6.1 documentation'
date: 2024-07-03T13:35:12
templateKey: link
link: https://grantjenks.com/docs/diskcache/api.html#diskcache.Cache.peekitem
tags:
  - python
published: true

---

> diskcache has a peekitem method that allows you to lookup the expire_time of a cached item without changing it.  I recently used this to implement debounce for fastapi background tasks with multiple workers running.  since all the workers I care about are on the same machine, but running in different processes diskcache was a great option.  All workers have access to the same disk, but not the same variables in memory.

[Original thought](https://grantjenks.com/docs/diskcache/api.html#diskcache.Cache.peekitem)
