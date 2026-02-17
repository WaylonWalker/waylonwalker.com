---
title: '💭 Kubernetes Secrets in 5 Minutes! - YouTube'
date: 2023-10-30T16:47:19
templateKey: link
link: https://www.youtube.com/watch?v=cQAEK9PBY8U&t=186
tags:
  - infra
  - k8s
published: true

---

> I am converting my docker compose env secrets over to k8s secrets.  This guide was clear and to the point how I can replicate this exact workflow.

First set the secret, the easiest way is to use kubectl wtih --from-literal because it automatically base64 encodes for you.

``` bash
kubectl create secret generic minio-access-key --from-literal=ACCESS_KEY=7FkTV**** -n shot
```

If you don't use the `--from-literal` you will have to base64 encode it.

``` bash
echo "7FkTV****" | openssl base64
```

Once you have your secret deployed, you have to update the container spec in your deployment manifest to get the valueFrom secretKeyRef.

``` yaml
    spec:
      containers:
        - env:
            - name: ACCESS_KEY
              valueFrom:
                secretKeyRef:
                  key: ACCESS_KEY
                  name: minio-access-key
            - name: SECRET_KEY
              valueFrom:
                secretKeyRef:
                  key: SECRET_KEY
                  name: minio-secret-key
          image: registry.wayl.one/shot-scraper-api
          name: shot-wayl-one
          ports:
            - containerPort: 5000
              protocol: TCP
          resources: {}
      restartPolicy: Always
```

[Original thought](https://www.youtube.com/watch?v=cQAEK9PBY8U&t=186)
