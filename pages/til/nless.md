---
date: 2026-05-06 20:45:01
templateKey: til
title: nless
published: true
tags:
  - python

---

nless is a seriously sick tui for exploring streaming data.  It makes it
seriously simple to pivot (U), drill in (Enter), sort (s).  It leave
breadcrumbs as you go and you can press q to back out.

Play with your kubernetes events.  Ya, my homelab is far from perfect, dont judge.

``` bash
kubectl get events -A -w | uvx --from nothing-less nless
```

![ceda8873-cb08-4436-a3ac-b5bf4a0b2379.mp4](http://dropper.wayl.one/file/ceda8873-cb08-4436-a3ac-b5bf4a0b2379.mp4)
