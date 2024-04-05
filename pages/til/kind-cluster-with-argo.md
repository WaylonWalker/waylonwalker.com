---
date: 2024-04-04 18:42:18
templateKey: til
title: setting up a kind cluster with argo
published: true
tags:
  - python

---

Kind (Kubernetes in Docker) is a tool that makes it easy to create and tear
down local clusters quickly.  I like to use it to test out new workflows.

Argocd is a continuous delivery tool that makes it easy to setup gitops
workflows in kubernetes.

Here is how you can setup a new kind cluster and install argocd into it using
helm, the kubernetes package manager.

``` bash
kind create cluster --name argocd

# your first time through you need to add the argocd repo
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

# install argocd into the cluster
helm install argo argo/argo-cd --namespace argocd --create-namespace

# deploy the app of apps
kubectl apply -f apps/apps.yaml
```
