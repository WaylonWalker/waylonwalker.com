---
date: 2024-07-02 07:54:01
templateKey: til
title: Install sealed-secreats via manifest
published: true
tags:
  - k8s
  - kubernetes

---

Yesterday I realized that I have overlooked the default installation method of
the sealed secrets controller for [[ kubernetes-kubeseal ]] this whole time an
jumped straight to the helm section.  I spun up a quick [[ kind-cluster ]] and
had it up quickly.  I can't say this is any better or worse than helm as I have
never needed to customize the install.  According to the docs you can customize
it with [[ kustomize ]] or helm.

``` bash
# option if you don't have a cluster try with kind

kind create cluster

curl -L https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.27.0/controller.yaml > controller.yaml

kubectl apply -f controller.yaml
```
