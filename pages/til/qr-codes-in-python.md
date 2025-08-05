---
date: 2025-08-05 08:32:12
templateKey: til
title: qr codes in python
published: true
tags:
  - python

---

I have a couple of use cases for simple qr codes in python coming up.  One is
for blog posts, the other is for auth into a new server application logged to a
terminal.  I tried the [`qrcode`](https://pypi.org/project/qrcode/) library
and it does not look as nice to me and I found
[`pyqrcode`](https://pypi.org/project/pyqrcode/) to be quite nice.

``` bash
import pyqrcode
url = pyqrcode.create('https://waylonwalker.com/qr-codes-in-python')
url.svg('qr-codes-in-python.svg', scale=8)
print(url.terminal(quiet_zone=1))
url.svg('qr-codes-in-python.svg', scale=12)
url.svg('qr-codes-in-python.svg', omithw=True) # width is controlled by the container

url.svg('qr-codes-in-python.svg', omithw=True, module_color='#ffd119')
url.svg('qr-codes-in-python.svg', omithw=True, module_color='#ff69b4', background='#2b034c')
```

## result

Here is the final svg result.

<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 45 45" class="pyqrcode"><path fill="#2b034c" d="M0 0h45v45h-45z"/><path stroke="#ff69b4" class="pyqrline" d="M4 4.5h7m2 0h1m1 0h3m3 0h3m5 0h2m3 0h7m-37 1h1m5 0h1m1 0h2m3 0h1m3 0h1m2 0h2m2 0h2m2 0h1m1 0h1m5 0h1m-37 1h1m1 0h3m1 0h1m1 0h1m2 0h2m1 0h2m1 0h1m1 0h1m1 0h1m2 0h2m2 0h1m1 0h1m1 0h3m1 0h1m-37 1h1m1 0h3m1 0h1m1 0h1m1 0h1m2 0h1m1 0h2m1 0h1m3 0h6m2 0h1m1 0h3m1 0h1m-37 1h1m1 0h3m1 0h1m1 0h1m1 0h1m1 0h2m1 0h1m2 0h1m1 0h2m1 0h1m2 0h1m1 0h1m1 0h1m1 0h3m1 0h1m-37 1h1m5 0h1m1 0h5m2 0h1m2 0h1m3 0h1m1 0h1m3 0h1m1 0h1m5 0h1m-37 1h7m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h7m-27 1h2m1 0h1m1 0h1m4 0h3m4 0h2m-27 1h1m2 0h5m2 0h2m1 0h4m1 0h5m3 0h2m1 0h5m-36 1h1m7 0h2m2 0h1m1 0h5m4 0h3m1 0h5m1 0h2m1 0h1m-37 1h2m1 0h1m2 0h6m1 0h7m1 0h1m1 0h2m2 0h4m1 0h1m1 0h1m1 0h1m-37 1h1m1 0h1m2 0h1m1 0h1m2 0h3m1 0h1m2 0h2m1 0h1m1 0h2m2 0h1m1 0h1m2 0h3m1 0h2m-34 1h1m2 0h1m2 0h1m1 0h1m3 0h1m1 0h1m1 0h2m3 0h1m2 0h2m1 0h1m2 0h1m1 0h2m-33 1h1m3 0h2m1 0h2m1 0h4m2 0h3m1 0h1m1 0h6m2 0h1m1 0h1m-37 1h1m1 0h1m1 0h6m1 0h1m1 0h1m1 0h2m1 0h4m3 0h1m1 0h1m2 0h1m2 0h2m1 0h1m-35 1h1m1 0h2m1 0h3m1 0h2m1 0h1m1 0h1m1 0h3m3 0h1m1 0h1m1 0h6m1 0h1m-36 1h1m3 0h1m1 0h1m4 0h2m6 0h1m1 0h2m5 0h1m1 0h1m4 0h1m-36 1h4m3 0h3m2 0h1m1 0h3m3 0h1m1 0h1m1 0h5m1 0h2m1 0h2m1 0h1m-35 1h1m2 0h2m1 0h2m2 0h3m8 0h2m2 0h5m1 0h2m1 0h1m-35 1h4m1 0h1m1 0h1m1 0h1m1 0h1m7 0h2m1 0h1m1 0h1m1 0h2m1 0h3m1 0h2m-37 1h3m1 0h3m1 0h1m1 0h2m3 0h1m1 0h3m2 0h1m1 0h1m3 0h1m1 0h1m2 0h1m1 0h1m-36 1h1m1 0h2m1 0h1m4 0h1m2 0h1m1 0h2m1 0h1m2 0h1m1 0h1m1 0h1m1 0h1m1 0h3m1 0h2m1 0h1m-37 1h1m1 0h1m1 0h1m1 0h1m2 0h2m1 0h4m1 0h3m1 0h3m3 0h6m2 0h2m-35 1h2m1 0h1m1 0h2m1 0h2m3 0h3m4 0h1m3 0h2m3 0h1m1 0h1m1 0h2m-37 1h4m1 0h2m4 0h2m1 0h4m1 0h1m4 0h1m5 0h2m1 0h1m1 0h2m-36 1h3m3 0h5m1 0h1m1 0h1m1 0h1m1 0h2m1 0h1m1 0h1m2 0h4m3 0h1m1 0h1m-37 1h4m1 0h2m1 0h3m1 0h1m3 0h3m2 0h1m2 0h1m2 0h1m1 0h3m2 0h1m1 0h1m-33 1h1m6 0h1m2 0h6m2 0h3m1 0h1m2 0h5m2 0h1m-37 1h5m1 0h6m1 0h1m6 0h1m1 0h1m5 0h6m-26 1h1m1 0h1m1 0h1m1 0h1m2 0h2m2 0h1m1 0h2m3 0h1m3 0h2m1 0h2m-37 1h7m1 0h1m1 0h5m2 0h2m1 0h1m1 0h2m2 0h1m1 0h1m1 0h1m1 0h3m1 0h1m-37 1h1m5 0h1m1 0h2m1 0h1m1 0h1m1 0h2m2 0h2m3 0h1m3 0h1m3 0h2m1 0h1m-36 1h1m1 0h3m1 0h1m3 0h1m2 0h1m2 0h2m1 0h3m1 0h2m1 0h7m2 0h2m-37 1h1m1 0h3m1 0h1m4 0h1m2 0h2m1 0h1m1 0h1m1 0h1m6 0h1m3 0h3m1 0h1m-37 1h1m1 0h3m1 0h1m1 0h1m1 0h1m1 0h4m1 0h1m1 0h7m1 0h2m2 0h2m2 0h2m-37 1h1m5 0h1m3 0h4m1 0h2m2 0h2m1 0h3m3 0h1m2 0h1m1 0h1m-34 1h7m4 0h2m1 0h1m3 0h2m4 0h1m3 0h1m1 0h1m2 0h1m2 0h1"/></svg>

Here is what it looks like in the terminal.

![screenshot-2025-08-05T13-53-17-368Z.png](https://dropper.wayl.one/api/file/c644bd34-b5da-48a3-b6cf-c89efb546114.png)
