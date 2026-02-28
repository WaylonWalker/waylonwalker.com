---
title: '💭 johanhaleby/kubetail: Bash script to tail Kubernetes logs from...'
date: 2023-10-31T01:04:16
template: link
link: https://github.com/johanhaleby/kubetail
tags:
  - 
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/johanhaleby/kubetail]]

Kubetail is a pretty sick bash script that allows you to tail logs for multiple pods in one stream.  Very handy when you have more than one replica running.

``` bash
wget https://raw.githubusercontent.com/johanhaleby/kubetail/master/kubetail
chmod u+x ./kubetail
```

Now with kubetail I can tail all the logs for every shot-wayl-one pod in the shot namespace.

``` bash
./kubetail shot-wayl-one -n shot
```

![output from running the kubetail command](https://screenshots.waylonwalker.com/kubetail.png)

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
