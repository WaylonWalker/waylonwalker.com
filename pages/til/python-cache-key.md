---
date: 2022-03-30 16:11:09.318689
templateKey: til
title: How I make cache-keys from python objects
tags:
  - python


---

I

```python
def make_hash(self, *keys: str) -> str:
    str_keys = [str(key) for key in keys]
    return hashlib.md5("".join(str_keys).encode("utf-8")).hexdigest()
```
