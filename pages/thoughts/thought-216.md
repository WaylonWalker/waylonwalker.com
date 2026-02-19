---
title: '💭 Configure Liveness, Readiness and Startup Probes | Kubernetes'
date: 2024-03-15T14:38:02
template: link
link: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
tags:
  - k8s
  - kubernetes
  - thoughts
  - thought
  - link
published: true

---

![[https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/]]

What is the difference between health, liveness, readiness, and startup?  This article does a great job at a full writeup description of how it works in kubernetes, here is my TLDR.



* health 200 OK - I'm still responding to requests
* health ERR - something happened and I cant respond to requests

* liveness 200 OK - I'm ready for more work
* liveness ERR - I'm still responding to requests, and i'm already working send requests to another pod, or scale up


## Z-pages

These probes are commonly deployed at `/healthz` and `/livez` endpoints.

Why the z?

z is a convention that comes from google for meta endpoints to reduce conflict with actual endpoints, and can be deployed to any application.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
