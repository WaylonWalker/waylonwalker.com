---
title: '💭 Uptime Kuma'
date: 2023-11-11T02:46:12
templateKey: link
link: https://uptime.kuma.pet/
tags:
  - homelab
  - k3s
  - containers
published: true

---

> Uptime kuma is a fantastic self hosted monitoring tool.  One docker run command and you are up and running.  Once you are in you have full control over checking status of urls, frequency, allowed timeouts, and a HUGE list of notification providers


``` bash
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1
```


I deployed it in my homelab today.

[![screenshot of https://twitter.com/_WaylonWalker/status/1723077941649707468](https://shots.wayl.one/shot/?url=https://twitter.com/_WaylonWalker/status/1723077941649707468&height=800&width=450&scaled_width=450&scaled_height=800&selectors=)](https://twitter.com/_WaylonWalker/status/1723077941649707468)


[Original thought](https://uptime.kuma.pet/)
