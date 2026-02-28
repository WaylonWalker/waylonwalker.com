---
title: '💭 k8s-monitoring-helm/charts/k8s-monitoring/docs/examples/privat...'
date: 2025-05-23T19:58:59
template: link
link: https://github.com/grafana/k8s-monitoring-helm/blob/main/charts/k8s-monitoring/docs/examples/private-image-registries/globally/values.yaml#L29
tags:
  - k8s
  - kubernetes
  - helm
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/grafana/k8s-monitoring-helm/blob/main/charts/k8s-monitoring/docs/examples/private-image-registries/globally/values.yaml#L29]]

k8s-monitoring requires setting imageregistry and pullsecrets twice

``` yaml
global:
  image:
    registry: my.registry.com
    pullSecrets:
      - name: my-registry-creds
  imageRegistry: my.registry.com
  imagePullSecrets:
    - name: my-registry-creds
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
