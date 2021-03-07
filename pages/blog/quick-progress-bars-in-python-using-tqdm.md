---
templateKey: blog-post
title: Quick Progress Bars in python using TQDM
date: 2019-09-18T05:00:00.000+00:00
status: published
description: Quick Progress Bars in python using TQDM
cover: "/static/photo-1448387473223-5c37445527e7.jpg"
related_post:
# - src/pages/blog/autoreload_ipython.md
tags:
- python
related_post_label: ''

---
tqdm is one of my favorite general purpose utility libraries in python.  It allows me to see progress of multipart processes as they happen.  I really like this for when I am developing something that takes some amount of time and I am unsure of performance.  It allows me to be patient when the process is going well and will finish in sufficient time, and allows me to 💥 kill it and find a way to make it perform better if it will not finish in sufficient time.

![](/tqdm2.gif)

> for more gifs like these follow me on twitter
[@waylonwalker](https://twitter.com/_WaylonWalker)

**Add a simple Progress bar!**
```python
from tqdm import tqdm
from time import sleep

for i in tqdm(range(10)):
	sleep(1)
```

**convenience**

TQDM also has a convenience function called trange that wraps the range function with a tqdm progress bar automatically.

```python
from tqdm import trange
from time import sleep

for i in trange(range(10)):
	sleep(1)
```


**notebook support**

There is also notebook support.  If you are bouncing between ipython and jupyter I recomend importing from the auto module.

```python
from tqdm.auto import tqdm
from time import sleep

for i in tqdm(range(10)):
	sleep(1)
```

https://waylonwalker.com/autoreload-ipython

> If you are using notebooks you should enable ipython autoreload 👆
