---
title: '💭 Can''t create Secret in Kubernetes: illegal base64 data at inpu...'
date: 2023-10-21T00:49:39
template: link
link: https://stackoverflow.com/questions/53394973/cant-create-secret-in-kubernetes-illegal-base64-data-at-input
tags:
  - homelab
  - k3s
  - thoughts
  - thought
  - link
published: true

---

![[https://stackoverflow.com/questions/53394973/cant-create-secret-in-kubernetes-illegal-base64-data-at-input]]

In order to use k8s secrets manifest you first need to encode the data values.

``` bash
echo -n 'mega_secret_key' | openssl base64
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
