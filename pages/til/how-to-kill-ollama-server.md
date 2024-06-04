---
date: 2024-04-14 18:31:36
templateKey: til
title: How to kill ollama server
published: true
tags:
  - linux
  - llm

---

I recently updated [ollama](https://ollama.com/), and it now installs a systemd
service that I was not expecting.  Seems like a great option, but I hadn't
expeted this and I was able to kill it previously.  It was using up gpu, and I
do other things on my machine with a gpu.  I tried pkill, kill, and everything,
it was still coming back.

> No matter what it comes back

``` bash
# stop it
systemctl stop ollama.service

# disable it if you want
systemctl disable ollama.service

# confirm its status
systemctl status ollama.service
```

You can confirm this with the following command.

``` bash
# checking running processes
ps aux | grep ollama
pgrep ollama

# checking gpu processes
gpustat --show-cmd --show-pid
```

Next time you want to start you can do it as before with `ollama serve`.
