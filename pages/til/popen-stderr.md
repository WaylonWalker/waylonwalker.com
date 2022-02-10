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

# this will run the shell command `cat me` and capture stdout and stderr
proc = Popen(["cat", "me"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# this will wait for the process to finish.
proc.wait()
```

## reading from stderr

To get the stderr we must get it from the proc, read it, and decode the
bystring.  Note that we can only get the stderr object once, so if you want to
do more than just read it you will need to store a copy of it.

``` python
proc.stderr.read().decode()
```

## Better Exception

Now that we can read the `stderr` we can make better error tracking for the
user so they can see what to do to resolve the issue rather than blindly
failing.

``` python
err_message = proc.stderr.read().decode()
if proc.returncode != 0:
    # the process was not successful

    if "No such file" in err_message:
        raise FileNotFoundError('No such file "me"')
```
