---
title: '💭 Inspect a Kubernetes PersistentVolumeClaim | Frank Sauerburger'
date: 2023-10-21T01:34:08
templateKey: link
link: https://frank.sauerburger.io/2021/12/01/inspect-k8s-pvc.html
tags:
  - homelab
  - k3s
published: true

---

> I was curious to see what was going on inside of my minio object storage. Great technique here by Frank to create an inspector pod, then you can do as you wish with the data.

I created the manifest as `pvc-inspector.yml`

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: pvc-inspector
spec:
  containers:
  - image: busybox
    name: pvc-inspector
    command: ["tail"]
    args: ["-f", "/dev/null"]
    volumeMounts:
    - mountPath: /pvc
      name: pvc-mount
  volumes:
  - name: pvc-mount
    persistentVolumeClaim:
      claimName: pvc-name
```

Then used it like this.

``` bash
# create pvc-inspector pod
kubectl apply -f pvc-inspector.yml
# exec into inspector
kubectl exec -it pvc-inspector -- sh
# explore data
ls /pvc
# cleanup
kubectl delete -f pvc-inspector.yml
```

[Original thought](https://frank.sauerburger.io/2021/12/01/inspect-k8s-pvc.html)
