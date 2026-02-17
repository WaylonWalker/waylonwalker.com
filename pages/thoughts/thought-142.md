---
title: '💭 Can''t create Secret in Kubernetes: illegal base64 data at inpu...'
date: 2023-10-21T00:49:39
templateKey: link
link: https://stackoverflow.com/questions/53394973/cant-create-secret-in-kubernetes-illegal-base64-data-at-input
tags:
  - homelab
  - k3s
published: true

---

> In order to use k8s secrets manifest you first need to encode the data values.

``` bash
echo -n 'mega_secret_key' | openssl base64
```

[Original thought](https://stackoverflow.com/questions/53394973/cant-create-secret-in-kubernetes-illegal-base64-data-at-input)
