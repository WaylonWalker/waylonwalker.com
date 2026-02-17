---
title: '💭 Performance Difference between RWX and RWO volumes · longhorn/...'
date: 2025-08-15T19:13:56
templateKey: link
link: https://github.com/longhorn/longhorn/discussions/6964
tags:
  - kubernets
  - longhorn
published: true

---

> Interesting longhorn storage performance test, author does highlight right away that this is a simulation and not a REAL test.  I did not fully understand the storage semantics before reading through this.

* **RWO** -  Always presents a filesystem `ext4` or `xfs`
* **RWX**/**ROX** - Always presents a network share `nfs` to the pod.

This is an important distinction for applications that use sqlite or a tool on top of sqlite such as diskcache.  With sqlite it is not recomended to run over nfs due to missing required file locking mechanisms.  

Longhorn storage still provides a lot of benefits to these applications as the storage is automatically replicated, if the node that your application is running on goes offline a new pod will start on an existing node.  If you have planned downtime, you can cordon and drain a node.  Since the data is available in another location you will be able to start a new pod on anther node.  barring your PodDisruptionBudget settings, taints, and affinity, this may happen automatically.

[Original thought](https://github.com/longhorn/longhorn/discussions/6964)
