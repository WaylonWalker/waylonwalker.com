---
date: 2025-12-08 20:59:27
templateKey: til
title: check your kubeconfig expire time
published: true
tags:
  - kubenetes

---

Today I learned an important lesson that you should periodically check on your
kubeconfigs expiration date.  It's easy to do.  You can ask for the
client-certificate-data from your kubeconfig, decode it, and use openssl to get
the expiration date.

``` bash
kubectl config view --raw -o jsonpath='{.users[0].user.client-certificate-data}' \
  | base64 -d 2>/dev/null \
  | openssl x509 -noout -dates
```

!!! Note

    This will only work for the first user, if you have more than one user or
    context defined in your kubeconfig you will need to adjust.
