---
title: 'uv cache prune'
date: 2025-07-09T19:41:13
template: link
link: https://simonwillison.net/2025/Jul/8/uv-cache-prune/#atom-everything
tags:
  - uv
  - python
  - thought
published: true

---

![[https://simonwillison.net/2025/Jul/8/uv-cache-prune/#atom-everything]]

Good point to check on your uv cache if you are running low on disk space.  I checked mine today, and it wasn't too bad so I left it alone.

``` bash
du -sh `uv cache dir`
```
