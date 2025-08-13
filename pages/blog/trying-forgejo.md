---
date: 2025-08-12 11:57:42
templateKey: blog-post
title: trying forgejo
tags:
  - self-hosted
  - homelab
published: True

---

WIP

``` yaml
networks:
  forgejo:
    external: false
services:
  server:
    image: codeberg.org/forgejo/forgejo:11
    container_name: forgejo
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: always
    networks:
      - forgejo
    volumes:
      - ./forgejo:/data
    ports:
      - '3000:3000'
      - '2222:22'
  docker-in-docker:
    image: docker:dind
    container_name: docker_dind
    privileged: true
    command: ["dockerd", "-H", "tcp://0.0.0.0:2375", "--tls=false"]
    restart: unless-stopped
    networks: [forgejo]
  runner:
    image: data.forgejo.org/forgejo/runner:4.0.0
    container_name: forgejo-runner
    user: "1001:1001"
    depends_on:
      - docker-in-docker
    environment:
      DOCKER_HOST: tcp://docker-in-docker:2375
    volumes:
      - ./runner-data:/data:Z,U # will hold .runner + cache
    command: /bin/sh -c "while :; do sleep 1; done"
    restart: unless-stopped
    networks: [forgejo]
```
