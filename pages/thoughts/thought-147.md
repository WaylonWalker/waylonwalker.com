---
title: '💭 casey/just: 🤖 Just a command runner'
date: 2023-10-22T02:09:57
template: link
link: https://github.com/casey/just
tags:
  - cli
  - dev
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/casey/just]]

I think just, might just be the thing I have been looking for.  I've been looking for some ci/cd that I can host myself, but everything looks pretty big, so for now I am going to use just as my task runner.


I installed with installer.

``` bash
curl https://i.wayl.one/casey/just | bash
```

I set up my devtainer builds with just.  Here is my `justfile`, yes you just need the cli and a file named `justfile`.

``` yaml
default: base alpine slim
base: build deploy
alpine: build-alpine deploy-alpine
slim: build-slim deploy-slim

build:
    podman build -t registry.wayl.one/devtainer:latest .
deploy:
    podman push registry.wayl.one/devtainer

build-alpine:
    podman build -f docker/Dockerfile.alpine -t registry.wayl.one/devtainer:alpine .
deploy-alpine:
    podman push registry.wayl.one/devtainer:alpine

build-slim:
    podman build -f docker/Dockerfile.slim -t registry.wayl.one/devtainer:slim .
deploy-slim:
    podman push registry.wayl.one/devtainer:slim
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
