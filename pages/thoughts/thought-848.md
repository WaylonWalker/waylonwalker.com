---
title: '💭 python 3.14 highlights! - YouTube'
date: 2025-10-03T01:04:57
template: link
link: https://www.youtube.com/watch?v=-Z-BDux-TRk
tags:
  - python
  - thoughts
  - thought
  - link
published: true

---

![[https://www.youtube.com/watch?v=-Z-BDux-TRk]]

anthony has some of the best python highlight videos each year.  This might be a good sign, but each year there seems to be less and less that I am chomping at the bit to get to.  I thought the remote debugger looked every interesting, his use case for `babi` seemed very interesting.  I wonder what textual would look like built in a 3.14 world, would it still have built its own debugger/console?

``` bash
uv tool run --python=3.14 babi
```

Without a process flag you need sudo permissions to attach a pdb debugger similar to gdb.

``` bash
ps -ef | grep babi
uv tool run --python=3.14 python -m pdb -p8605
```

![screenshot-2025-10-03T01-11-02-918Z.png](https://dropper.wayl.one/api/file/b5e1a34d-c198-440a-ab30-4498bfa6962a.png)


!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
