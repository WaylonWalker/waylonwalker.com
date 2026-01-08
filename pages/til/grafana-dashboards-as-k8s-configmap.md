---
date: 2025-05-06 20:24:35
templateKey: til
title: grafana dashboards as k8s configmap
published: true
tags:
  - otel
  - grafana
  - k8s

---

I'm trying to learn proper logs, monitoring, otel, and grafana.  Today I
imported a bunch of pre-made k8s dashboards and made a few of my own for
specific apps, and it made me want to know how I can turn my own custom
dashboards into infrastructure as code.  Turns out grafana makes it pretty easy
to do this, if you have the grafana dashboard sidecar running.  It will pick up
any ConfigMap with the grafana_dashboard label and import it.

Go to Dashboards -> Pick a Dashboard -> Export -> JSON.

![image](https://dropper.waylonwalker.com/api/file/530e8515-a72a-4341-82d7-37f6f985e327.webp)

![image](https://dropper.waylonwalker.com/api/file/d792b2db-2dcf-465f-a400-e84f199ec22d.webp)

![image](https://dropper.waylonwalker.com/api/file/684701cc-efec-4e2b-9630-c8aea7ff5b14.webp)

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-dashboard
  namespace: meta
  labels:
    grafana_dashboard: "1"
data:
  my-dashboard.json: |
    {
      "annotations": {
        "list": [
      ...
      "uid": "fel2uhjhepg5ce",
      "version": 3
    }
```
