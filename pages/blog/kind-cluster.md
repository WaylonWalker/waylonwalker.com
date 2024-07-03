---
date: 2024-07-02 08:01:20
templateKey: blog-post
title: kind cluster
tags:
  - k8s
  - kubernetes
published: True

---

[kind](https://kind.sigs.k8s.io/) is a very useful tool to quickly standup and
teardown kubernetes clusters.  I use it to run clusters locally.  Generally
they are short lived clusters for trying, testing, and learning about
kubernetes.

Kind is Kubernetes in Docker, its very fast to get a new cluster up and
running.  Other than checking a box in docker desktop it is the easiest way
currently to get a cluster up and running.  I've used docker desktop for k8s
before I really developed on k8s and it was buggy at the time and sometimes
started and sometimes didn't, when it didnt I had no idea how to fix it.  I'd
suggest kind as the best option to get a cluster up and running locally.

## Not Production

If you are looking for a production ready cluster this is not it.  I really
like [k3s](https://k3s.io/).  At the time that I chose k3s it was the most lightweight option that
easily supported multinode clusters.

## Starting a kind cluster

The first step, and maybe only one that you need is to create a cluster and
give it a name.  This command will edit your $KUBECONFIG file, and set the kind
cluster as your default cluster to interact with.

``` bash
kind create cluster --name <CLUSTER_NAME>
```

## Using [podman](https://podman.io/) as a backend

I use podman as my docker engine, kind works with docker and podman, but docker
by default, in order to switch to podman you need to set an environment
variable.

``` bash
export KIND_EXPERIMENTAL_PROVIDER=podman
```

This will tell kind to use podman as the backend provider instead of docker.

## Loading images

If your images are not publically available from a registry, you can load them
in kind using the `kind load docker-image` command.

``` bash
kind load docker-image $REPOSITORY:$TAG --name <CLUSTER_NAME>
```

!!! Note
    the CLUSTER_NAME is the name that you gave kind when you started the kind cluster.

## Argocd

Argocd is a great way to setup gitops workflows in kubernetes.  compared to
just hand-rolling kubectl apply, argo holds the state and is able to not only
apply new and change, but cleanup removed things.

[[ kind-cluster-with-argo ]]

You can stand up argocd in kind for learning argo or getting a nice visual.
But often when I use kind its overkill.  The cluster is not long lived, I don't
care if things are not cleaned up, and I want to quickly apply changes without
a commit and push to a git repo.
