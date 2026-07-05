---
date: 2026-07-05 17:16:21
templateKey: til
title: rpm ostree status
published: true
tags:
  - linux

---

today I learned you can use `rpm-ostree status` to see if your fedora coreos system is up to date.

``` bash
rpm-ostree status
```

For me it listed security advisories with a count of each severity unknown, low, moderate, and important.
