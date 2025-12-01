---
date: 2025-04-04 09:57:50
templateKey: blog-post
title: Changing k8s Storage Class - Migration Job
tags:
  - k8s
  - homelab
  - longhorn
published: True

---

I'm setting up longhorn in my homelab, and I ran into an issue where I
initially setup some pvcs under longhorn, and later realized that to get
longhorn to snapshot and backup I needed to hand edit volumes after the fact or
change storage class.  I'm all in on gitops so option 1 was not an option.  So
changing storageclass it is.

Now the issue is that you CANNOT mutate storageclass on a provisioned pvc, it
is an immutable attribute.

## Migration Job

This migration job will create a new pvc with the new storageclass and move the
data from the old pvc to the new pvc.

!!! Note "Existing Pods"
     This migration job will not work if you have a pod using the old pvc.  You
     will need to shutdown the pod and delete it.

``` yaml
# old pvc with longhorn storageclass
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: site-pvc-longhorn
  namespace: waylonwalker-com
spec:
  storageClassName: longhorn-backup
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
# new pvc with longhorn-backup storageclass
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: site-pvc-longhorn-backup
  namespace: waylonwalker-com
spec:
  storageClassName: longhorn-backup
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
---
# migration job to move the data to the new pvc
apiVersion: batch/v1
kind: Job
metadata:
  name: pvc-migration
  namespace: waylonwalker-com
spec:
  template:
    spec:
      containers:
      - name: pvc-migration
        image: ubuntu:22.04
        command: ["/bin/bash", "-c"]
        args:
          - |
            echo "Starting migration..."
            cd /data
            cp -av source/. destination/
            echo "Migration complete!"
        volumeMounts:
        - name: source-vol
          mountPath: /data/source
        - name: dest-vol
          mountPath: /data/destination
      restartPolicy: Never
      volumes:
      - name: source-vol
        persistentVolumeClaim:
          claimName: site-pvc-longhorn
      - name: dest-vol
        persistentVolumeClaim:
          claimName: site-pvc-longhorn-backup
```

Apply the manifests and wait for the job to complete.

``` bash
kubectl apply -f pvc-migration.yaml
```

## Cleanup

I had chatgpt create me a script to help me find what is using the pvc so that
it can be deleted.

``` bash
#!/bin/bash

NAMESPACE="waylonwalker-com"
PVC_NAME="site-pvc-longhorn-new"

echo "⏳ Checking if PVC exists..."
kubectl get pvc "$PVC_NAME" -n "$NAMESPACE" || {
  echo "✅ PVC already deleted."
  exit 0
}

echo "🔍 Describe PVC..."
kubectl describe pvc "$PVC_NAME" -n "$NAMESPACE"

echo -e "\n🔗 Checking if any pod is using this PVC..."
kubectl get pods -n "$NAMESPACE" -o json | jq -r \
  --arg PVC "$PVC_NAME" \
  '.items[] | select(.spec.volumes[].persistentVolumeClaim.claimName == $PVC) | .metadata.name'

echo -e "\n🧹 Checking finalizers..."
kubectl get pvc "$PVC_NAME" -n "$NAMESPACE" -o json | jq '.metadata.finalizers'

echo -e "\n🔎 Checking associated VolumeAttachment..."
PV_NAME=$(kubectl get pvc "$PVC_NAME" -n "$NAMESPACE" -o jsonpath='{.spec.volumeName}')
echo "🔗 PVC is bound to PV: $PV_NAME"

kubectl get volumeattachment -A -o json | jq \
  --arg PV "$PV_NAME" \
  '.items[] | select(.spec.source.persistentVolumeName == $PV) | {name: .metadata.name, node: .spec.nodeName, attached: .status.attached}'

echo -e "\n🚀 Done."
```

I had still had cronjob pods completed, so I had to delete them first.

``` bash
🔗 Checking if any pod is using this PVC...
pvc-migration-ndv92
waylonwalker-com-cronjob-29057840-8s92p
waylonwalker-com-cronjob-29057850-4rvm9
waylonwalker-com-cronjob-29057860-6g89j
```

``` bash
kubectl delete pod pvc-migration-ndv92 -n waylonwalker-com
kubectl delete pod waylonwalker-com-cronjob-29057840-8s92p -n waylonwalker-com
kubectl delete pod waylonwalker-com-cronjob-29057850-4rvm9 -n waylonwalker-com
kubectl delete pod waylonwalker-com-cronjob-29057860-6g89j -n waylonwalker-com
```
