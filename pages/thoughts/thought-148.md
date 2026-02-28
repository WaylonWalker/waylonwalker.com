---
title: '💭 mkimuram/k8sviz: Generate Kubernetes architecture diagrams fro...'
date: 2023-10-22T21:07:26
template: link
link: https://github.com/mkimuram/k8sviz
tags:
  - homelab
  - k8s
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/mkimuram/k8sviz]]

This is a sick kubernetes architecture diagran generation tool.

Here is an example

![an example output from k8sviz](https://raw.githubusercontent.com/mkimuram/k8sviz/master/examples/wordpress/default.png)


## installation

``` bash
$ curl -LO https://raw.githubusercontent.com/mkimuram/k8sviz/master/k8sviz.sh
$ chmod u+x k8sviz.sh
```
### Usage

``` bash
./k8sviz.sh --kubeconfig ~/.config/kube/falcon-k3s.yaml -t png -o k8sviz.png
```


!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
