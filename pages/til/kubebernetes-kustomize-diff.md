---
date: 2024-07-06 09:42:42
templateKey: til
title: k8s kustomize diff
published: true
tags:
  - k8s
  - kubernetes

---

I've started leaning in on kubernetes kustomize to customize my manifests per
deployment per environment.  Today I learned that it comes with a diff command.

``` bash
kubectl diff -k k8s/overlays/local
```

You can enable color diffs by using an external diff provider like colordiff.

``` bash
export KUBECTL_EXTERNAL_DIFF="colordiff -N -u"
```

You might need to install colordiff if you don't already have it.

``` bash
sudo pacman -S colordiff

sudo apt install colordiff
```

Now I can try out kustomize changes and see the change with kustomize diff.
