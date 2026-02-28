---
title: '💭 How Fly.io uses Docker (without Docker) - YouTube'
date: 2024-07-27T01:14:21
template: link
link: https://www.youtube.com/watch?v=7iypMRKniPU&t=3s
tags:
  - docker
  - vm
  - thoughts
  - thought
  - link
published: true

---

![[https://www.youtube.com/watch?v=7iypMRKniPU&t=3s]]

Docker no Docker, what!!!


So fly.io uses Dockerfiles to deploy your app, but no docker.  They use containerd to download your docker images into firecracker microvms to run your app.  Firecracker is the same tech that runs aws lambda functions.

Fascinating short post on the beans under the hood at fly.io and how they scale your app globally.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
