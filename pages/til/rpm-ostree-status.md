---
date: 2026-07-05 17:16:21
templateKey: til
title: rpm ostree status
published: true
tags:
  - linux

---

I've been running fedora coreos on my home servers for awhile.  I really liked
the stability I got from bazzite, and have since enjoyed the stability of
fedora coreos.  Since it's an immutable system I've never quite known if I need
to reboot or not, and was unsure how to check for updates. Today I learned you
can use `rpm-ostree status` to see if your
fedora coreos system is up to date.

``` bash
rpm-ostree status
```

For me it listed security advisories with a count of each severity unknown, low, moderate, and important.
