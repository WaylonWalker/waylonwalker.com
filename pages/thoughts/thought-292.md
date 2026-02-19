---
title: '💭 xxhash · PyPI'
date: 2024-06-03T13:34:05
template: link
link: https://pypi.org/project/xxhash/
tags:
  - python
  - thoughts
  - thought
  - link
published: true

---

![[https://pypi.org/project/xxhash/]]

I hit an issue with markata where even though a bunch of articles were cached, the site build was still slow because I was hitting hashlib.sha256 so hard for cache keys.  I was shocked when this popped up in my profiler as a significant portion of the time spent.  I swapped out for xxhash and that issue completely went away.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
