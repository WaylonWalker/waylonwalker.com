---
title: '💭 Manual Upgrades | K3s'
date: 2024-04-19T12:51:03
templateKey: link
link: https://docs.k3s.io/upgrades/manual
tags:
  - k8s
  - kubernetes
  - k3s
published: true

---

> You can give k3s an install channel to install `stable`,  `latest`, or specific versions like `1.26`.  This is handy to make sure that you install the same version on all of your workers.

``` bash
curl -sfL https://get.k3s.io | INSTALL_K3S_CHANNEL=latest <EXISTING_K3S_ENV> sh -s - <EXISTING_K3S_ARGS>
```

[Original thought](https://docs.k3s.io/upgrades/manual)
