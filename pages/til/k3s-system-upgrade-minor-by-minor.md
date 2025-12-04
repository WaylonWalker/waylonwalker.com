---
date: 2025-12-05 09:25:39
templateKey: til
title: k3s system-upgrade minor by minor
published: true
tags:
  - k8s
  - k3s
  - kubernetes

---

The k3s system-upgrade controller is a fantastic tool for upgrading k3s
automatically.  It has done a fantastic job for me every time I've used it.
Today I ran it on a cluster that needed to upgrade several minors and I
learned that the controller does not pick up on changes to the channel url if
you change from minor to minor.  

The solution I came up with was to name the plan with the version it supports.
Then on each patch upgrade, change both the plan name and the channel.  I use
gitops with argocd, it automcatically cleaned up old plans, created new plans,
and the system-upgrade-controller picked up the plan and started applying
immediately.


``` yaml
# Server plan
apiVersion: upgrade.cattle.io/v1
kind: Plan
metadata:
  name: server-plan-v1.33 # <- This is important if you want to change the channel name
  namespace: system-upgrade
spec:
  concurrency: 1
  cordon: true
  nodeSelector:
    matchExpressions:
    - key: node-role.kubernetes.io/control-plane
      operator: In
      values:
      - "true"
  serviceAccountName: system-upgrade
  upgrade:
    image: rancher/k3s-upgrade
  channel: https://update.k3s.io/v1-release/channels/v1.33
---
# Agent plan
apiVersion: upgrade.cattle.io/v1
kind: Plan
metadata:
  name: agent-plan-v1.33 # <- This is important if you want to change the channel name
  namespace: system-upgrade
spec:
  concurrency: 1
  cordon: true
  nodeSelector:
    matchExpressions:
    - key: node-role.kubernetes.io/control-plane
      operator: DoesNotExist
  prepare:
    args:
    - prepare
    - server-plan
    image: rancher/k3s-upgrade
  serviceAccountName: system-upgrade
  upgrade:
    image: rancher/k3s-upgrade
  channel: https://update.k3s.io/v1-release/channels/v1.33
```
