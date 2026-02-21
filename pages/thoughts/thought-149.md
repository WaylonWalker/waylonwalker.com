---
title: '💭 How to kill process based on the port number in Linux - Linux ...'
date: 2023-10-23T15:15:02
template: link
link: https://linuxconfig.org/how-to-kill-process-based-on-the-port-number-in-linux
tags:
  - arch
  - thoughts
  - thought
  - link
published: true

---

![[https://linuxconfig.org/how-to-kill-process-based-on-the-port-number-in-linux]]

I've often struggled to find and kill a process using a certain port on archlinux.  Mainly becuase most guides use netstat rather than `ss`.


Here is how I just killed the process using port 5000 using `fuser`.

``` bash
sudo fuser -k 5000/tcp
```

You can also get information about the process by running `lsof`


``` bash
❯ lsof -i :5000
COMMAND      PID   USER   FD   TYPE    DEVICE SIZE/OFF NODE NAME
thoughts 1058292 waylon   11u  IPv4 119622828      0t0  TCP *:commplex-main (LISTEN)
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
