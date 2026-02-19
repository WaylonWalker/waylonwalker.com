---
title: '💭 Using journalctl - The Ultimate Guide To Logging'
date: 2024-05-02T01:20:51
template: link
link: https://www.loggly.com/ultimate-guide/using-journalctl/
tags:
  - 
  - thoughts
  - thought
  - link
published: true

---

![[https://www.loggly.com/ultimate-guide/using-journalctl/]]



I had a boot issue on my sons fresh ubuntu 24.04 install and journalctl came in clutch.

``` bash
journalctl -p 3 -xb 
```

* -p 3 gives me priority 3
* -x gives me extra catalog information when available
* -b gives me the current boot.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
