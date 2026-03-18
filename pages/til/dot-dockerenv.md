---
date: 2026-03-18 10:07:16
templateKey: til
title: dot dockerenv
published: true
tags:
  - containers
  - docker
  - kubernetes

---

Today I learned that docker creates an empty `/.dockerenv` file to indicate that
you are running in a docker container.  Other runtimes like podman commonly use
`/run/.containerenv`.  kubernetes uses neither of these, the most common way to
detect if you are running in kubernetes is to check for the presence of the
`KUBERNETES_SERVICE_HOST` environment variable.  There will also be a directory
at `/var/run/secrets/kubernetes.io/serviceaccount` that contains the service
account credentials if you are running in kubernetes.

