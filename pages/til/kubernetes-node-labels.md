---
date: 2025-05-28 18:49:19
templateKey: til
title: kubernetes node labels
published: true
tags:
  - kubernetes

---

If you need to target a specific k8s node in the cluster, you can use labels.
You want to treat your nodes as much like cattle as you can, but sometimes
budgets get in the way.  You might be like me and just run any free hardware
you can get in your cluster, or you might have some large storage or gpu needs
that you can't afford to put on every node in the cluster.

``` bash
kubectl get nodes --show-labels

# add the bigpool label
kubectl label node k8s-1 bigpool=true
kubectl get nodes --show-labels

# remove the bigpool label
kubectl label node k8s-1 bigpool-
```

To use the label in a pod set `spec.nodeSelector` to the label that you
applied.

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox
spec:
  containers:
  - name: busybox
    image: busybox
  nodeSelector:
    bigpool: "true"
```
