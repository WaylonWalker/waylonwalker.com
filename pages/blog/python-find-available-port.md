---
date: 2022-01-15 23:47:27.009375
templateKey: til
title: Python Find Available Port
tags:
  - python
  - python
  - python
status: draft

---

``` python
import socket

def find_port(port=8000):
    """Find a port not in ues starting at given port"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if s.connect_ex(("localhost", port)) == 0:
            return find_port(port=port + 1)
        else:
            return port
```
