---
date: 2024-04-08 16:56:46
templateKey: til
title: scheduling cron jobs in kubernetes
published: true
tags:
  - kubernetes

---

For my reader app I am using cronjobs to schedule my a new build and upload to
cloudflare pages every hour.  In this example I have built a docker image
`docker.io/waylonwalker/reader-waylonwalker-com` and pushed it to dockerhub.
It uses a `CLOUDFLARE_API_TOKEN` secret to access cloudflare, and the
entrypoint itself does the build and upload.

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: reader
  namespace: reader

---
apiVersion: batch/v1
kind: CronJob
metadata:
  name: reader-cronjob
  namespace: reader
spec:
  schedule: "0 * * * *"
  successfulJobsHistoryLimit: 6
  failedJobsHistoryLimit: 6
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: reader-container
              image: docker.io/waylonwalker/reader-waylonwalker-com:latest
              env:
                - name: CLOUDFLARE_API_TOKEN
                  valueFrom:
                    secretKeyRef:
                      name: cloudflare-secret
                      key: cloudflare-secret
          restartPolicy: OnFailure
```
