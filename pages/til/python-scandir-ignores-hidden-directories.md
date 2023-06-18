---
date: 2023-06-17 20:19:59
templateKey: til
title: Python scandir ignores hidden directories
status: "published"
tags:
  - python
---

The next version of markata will be around a full second faster at building
it's docs, that's a 30% bump in performance at the current state. This
performance will come when virtual environments are stored in the same
directory as the source code.

!["One lone jedi stands in Glowing chains of interconnected network of technological cubes, in the middle of a futuristic cyberpunk dubai city, in the art style of dan mumford and marc simonetti, atmospheric lighting, intricate, volumetric lighting, beautiful, sharp focus, ultra detailed" -s50 -W800 -H350 -C7.5 -Ak_lms -S1657735302](https://stable-diffusion.waylonwalker.com/000300.1657735302.webp)

## What happened??

I was looking through my profiler for some unexpected performance hits, and
noticed that the `docs` plugin was taking nearly a full second (sometimes
more), just to run glob.

```python
    |  |- 1.068 glob  markata/plugins/docs.py:40
    |  |  |- 0.838 <listcomp>  markata/plugins/docs.py:82
    |  |  |  `- 0.817 PathSpec.match_file  pathspec/pathspec.py:165
    |  |  |        [14 frames hidden]  pathspec, <built-in>, <string>
```

## Python scandir ignores hidden directories

I started looking for different solutions and what I found was that I was
hitting pathspec with way more files than I needed to.

```python
len(list(Path().glob("**/*.py")))
# 6444
len([Path(f) for f in glob.glob("**/*.py", recursive=True)])
# 110
```

After digging into the docs I found that `glob.glob` uses `os.scandir` which
ignores '.' and '..' directories while Path.glob does not.

<https://docs.python.org/3/library/os.html#os.scandir>

## results?

Now glob.py from the docs plugin does not even show up in the profiler.

I opened up ipython and saw the following results. For some reason as I hit
docs.glob it was only hitting 488 ms from ipython, but it was still a massive
improvement over the original.

```python
%timeit docs.glob(m)
# 488 ms ± 3.05 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit docs.glob(m)
# 9.37 ms ± 90.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```
