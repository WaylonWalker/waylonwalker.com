---
date: 2022-02-10 03:57:32.041457
templateKey: til
title: Read stderr from python subprocess.Popen
tags:
  - python

---

I often run shell commands from python with Popen, but not often enough
do I set up error handline for these subprocesses.  It's not too hard,
but it can be a bit awkward if you don't do it enough.

## Using Popen


``` python
import subprocess
from subprocess import Popen

proc = Popen(["cat", "me"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

```

## reading from stderr
``` python
```
