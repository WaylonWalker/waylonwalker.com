---
date: 2025-06-03 11:21:11
templateKey: til
title: unset multiple environment variables
published: true
tags:
  - linux
  - bash

---


You can unset multiple environment variables at once. I did not know this was a
thing, its something that ended up happening organically on a call and asking
someone to run `unset`.  They had never done it before and did not know how it
works, but did exactly as I said instead of what I meant.  I like this handy
shortcut doing it in one line rather than each one individually, I will be
using this in the future. You might need this for something like
[[running-aws-cli-commands-with-localstack]].

``` bash
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_DEFAULT_REGION
```
