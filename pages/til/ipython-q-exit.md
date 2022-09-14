---
date: 2022-06-13 10:10:34
templateKey: til
title: IPython q to exit
status: published
tags:
  - python

---

So many terminal applications bind `q` to exit, even the python debugger, its
muscle memory for me.  But to exit ipython I have to type out `exit<ENTER>`.
This is fine, but since q is muscle memory for me I get this error a few times
per day.

```
╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
│ <ipython-input-1-2b66fd261ee5>:1 in <module>                                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
NameError: name 'q' is not defined
```

After digging way too deep into how IPython implements its `ExitAutoCall` I
realized there was a very simple solution here.  `IPython` automatically
imports all the scripts you put in your profile directory, all I needed was to
create `~/.ipython/profile_default/startup/q.py` with the following.

```
q = exit
```

It was that simple.  This is not a game changer by any means, but I will now
see one less error in my workflow.  I just press `q<Enter>` and I am out,
without error.
