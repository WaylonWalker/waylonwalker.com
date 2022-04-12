---
date: 2022-04-10 14:21:54.240315
templateKey: til
title: Python sys.excepthook
tags:
  - python

---

Sometimes you just want python to do something else when you hit an exception,
maybe that's fire a text, slack message, email, or system notification like I
wanted.

I am working on a quick and dirty python script designed to take screenshots
and land them on my website in a single hotkey.  With it being designed to run
with a hotkey, if it were to error I would not see it.

I could have gone down a logging route, but honestly this is meant to be quick,
dirty, and work on my system for me.  I just want to get it in my system
notification.

## sys.excepthook

Python exposes sys.excepthook for just this case.  Here is what I ended up
doing to fire a system notification as well as printing the message.  Yaya a
log would be mroe appropriate, but this is designed to just get done quick and
do the job I want it to do.

```python
def notify_exception(type, value, tb):
    traceback_details = "\n".join(traceback.extract_tb(tb).format())

    msg = f"caller: {' '.join(sys.argv)}\n{type}: {value}\n{traceback_details}"
    print(msg)
    Popen(
        f'notify-send "screenshot.py hit an exception" "{msg}" -a screenshot.py',
        shell=True,
    )


sys.excepthook = notify_exception
0 / 0
```
