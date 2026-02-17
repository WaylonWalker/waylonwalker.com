---
title: '💭 valkey-io/valkey: A flexible distributed key-value datastore t...'
date: 2025-02-17T02:27:34
templateKey: link
link: https://github.com/valkey-io/valkey
tags:
  - dev
published: true

---

> valkey appears to be the largest open source fork of redis that was forked just before their transition to the new source available licenses.

One notable thing missing from the readme is how to run with docker, which I saw in the valkey-py docs.

``` bash
docker run -p 6379:6379 -it valkey/valkey:latest
```

You can install the python library with

``` bash
python -m venv .venv
. ./.venv/bin/activate
pip install "valkey[libvalkey]"
```


[Original thought](https://github.com/valkey-io/valkey)
