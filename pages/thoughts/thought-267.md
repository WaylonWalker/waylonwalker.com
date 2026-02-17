---
title: '💭 Using journalctl - The Ultimate Guide To Logging'
date: 2024-05-02T01:20:51
templateKey: link
link: https://www.loggly.com/ultimate-guide/using-journalctl/
tags:
  - 
published: true

---

> 

I had a boot issue on my sons fresh ubuntu 24.04 install and journalctl came in clutch.

``` bash
journalctl -p 3 -xb 
```

* -p 3 gives me priority 3
* -x gives me extra catalog information when available
* -b gives me the current boot.

[Original thought](https://www.loggly.com/ultimate-guide/using-journalctl/)
