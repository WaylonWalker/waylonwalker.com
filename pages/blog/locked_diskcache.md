---
templateKey: blog-post
tags: ['python']
title: Python Diskcahe is locked
date: 2021-05-14T18:38:45
published: true

---

<script>
change_speed = (speed) => [...document.querySelectorAll('video')].map(v => v.playbackRate=v.playbackRate+speed)
</script>
<style>
</style>

Running multiple processes using the same diskcache object can cause issues
with locks.  As I was trying to setup a rich Live display for markata I ran
into issues where each part could not nun simultaneusly.  As I had followed the
instructions from discache it was not directly aparant to me, so I had to make
a simple example to experiment and play with at a small scale.

## Minimum reproducible error

Minimum reporducible error is one of my superpowers in development.  I do this
very often to sus out what is really happening.  My day to day work is
processing data with python, I keep a number of very small data sets handy to
break and fix.  This helps separate complexities of the project and the problem.

## Let's break it

Markata has a lot going on.  It's a plugins all the way down static site
generator built in python.  Trying to find the root cause through the layers of
plugin and cli modules can be a pain, but in this case building a very simple
minimum reporducible error was much easier.

```python
from pathlib import Path
from diskcache import FanoutCache
import time

CACHE_DIR = Path(".") / ".markata.cache"

if __name__ == "__main__":

    cahe = FanoutCache(CACHE_DIR, statistics=True)
    item = cache.get("me")
    print(item)
    time.sleep(20)
```

> 📝 `time.sleep(20)` is here to simulate doing some other work, while the cache
> object is still open.

## Running locked_diskcache.py

Here I have my editor showing the file on the top split and have ran it in the
two lower splits.  Notice that the first (left split) immediately prints out
the result, while the second one (right split) does not print out the result
until the first is completely finished.

![locked diskcache](https://dropper.waylonwalker.com/file/98930c40-24c4-4b5c-9258-edfc1ddcfa6b.mp4)

## Using a context manager

This time lets put the cache in a context manager so that it automatically
closes after it gets the item.

``` python
from pathlib import Path
from diskcache import FanoutCache
import time

CACHE_DIR = Path(".") / ".markata.cache"

if __name__ == "__main__":

    with FanoutCache(CACHE_DIR, statistics=True) as cache:
        item = cache.get("me")
    print(item)
    time.sleep(20)
```

## Running unlocked_diskcahce.py

Notice when we run this time when I run both splits, they are able to
immediatly print out their result and get to work on that sleep statement.
This time the right right split only takes ~20s rather than ~40s since it no
longer needs to wait for the left one to unlock the cache.

![unlocked diskcache](https://dropper.waylonwalker.com/file/ee4e94aa-779d-49bc-b96c-4f5eb98b29c6.mp4)

## I've learned

Keep your diskcache open for as little as needed, especially if you plan to
have it open on multiple processes.  Hopefully this problem solving session
helps someone else with their discache problems or find a better way to problem
solve with minimum viable errors.

## Useful Links

* [diskcache-pypi](https://pypi.org/project/diskcache/)
* [diskcache-tutorial](https://www.grantjenks.com/docs/diskcache/tutorial.html)
* [diskcache-github](https://github.com/grantjenks/python-diskcache) 👈 Give it a star
