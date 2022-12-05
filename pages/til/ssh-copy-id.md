---
date: 2022-12-04 20:10:05
templateKey: til
title: ssh copy id
status: 'published'
tags:
  - linux

---

I recently setup some vm's on my main machine and got sick of signing in with
passwords.

``` bash
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub virt
```
