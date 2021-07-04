---
templateKey: blog-post
tags: ['kedro', 'python', 'stream']
title: Kedro Spaceflights - part 1 | Stream replay June 4, 2021
date: 2021-06-04T16:15:04
status: published

---

This was my first time ever streaming on
[twitch.tv/waylonwalker](twitch.tv/waylonwalker).  I am excited to get going.
I have been streaming early in the morning while I am still waking up, so still
a bit groggy as I go.

https://youtu.be/Y07UBr9Ccjs

## Kedro Spaceflights

It all started with
[kedro/issues/606](https://github.com/quantumblacklabs/kedro/issues/606), Yetu
called out for users of kedro to record themselves doing a walk through of
their tutorials.  I wanted to do this, but was really stuck at the fact that
recording or editing somewhat polished vide is quite time consuming for me.

![kedro-issue-606](https://images.waylonwalker.com/kedro-issue-606.png)

## Notes

``` bash
pipx run kedro new
cd project
python -m venv .venv
source .venv/bin/activate
pip install kedro
kedro install
```

