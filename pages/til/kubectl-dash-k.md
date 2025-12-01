---
date: 2024-07-05 20:15:11
templateKey: blog
title: kubectl dash k
published: true
tags:
  - k8s
  - kubernetes

---


Kubernetes ships with a feature called kustomize that allows you to customize
your manifests in a declarative way.  It's a bit like helm, but easier to use.
I found this useful.

## kustomization.yaml

In order to use kustomize you need to have a kustomization.yaml,
kustomization.yml, or Kustomization file in the directory you are applying.

``` bash
kubectl apply -k .
error: unable to find one of 'kustomization.yaml', 'kustomization.yml' or 'Kustomization' in directory '/tank/git/kustomize-playground'
```

The kustomization.yaml file cannot be empty.

``` bash
❯ kubectl apply -k pod
error: kustomization.yaml is empty
```

## lets make an mvp

``` bash
mkdir pod
touch pod/pod.yaml
touch pod/kustomization.yaml
```

``` yaml
# pod.yaml
```

``` yaml
# kustomization.yaml
```

## Overlays

Overlays must point to yaml or a directory with a kustomization.yaml file, and
cannot reside inside the same directory causing a circular reference.

---

## Layout

``` bash
k8s
├── base
│   ├── deployment.yaml
│   └── kustomization.yaml
├── overlays
│   ├── local
│   │   └── kustomization.yaml
│   ├── dev
│   │   └── kustomization.yaml
│   └── prod
│       ├── special-prod.yaml
│       └── kustomization.yaml
```

## base

Place all of the common k8s manifests here in the base directory along with
kustomization.yaml.  You can split them up into separate files or just one
file, I'm keeping it to one for simiplicity.

## base - kustomization.yaml

In the base kustomization.yaml file add all of the manifests that you want to
use as a resource.

``` yaml
resources:
  - deployment.yaml
```

## overlays

Now for each separate environment that you want to have create a directory in
overlays with a kustomization.yaml file, and any special manifests that only
apply to a particular environment.

## overlays - kustomization.yaml

### resoures

``` yaml
resources:
  - ../../base
# any other specific resources, maybe special ones for prod here
  - sealed-dotenv.yaml
```

### images

``` yaml
images:
  - name: my-image
    newName: docker.io/myrepo/myimage
    newTag: 1.0.0
```
