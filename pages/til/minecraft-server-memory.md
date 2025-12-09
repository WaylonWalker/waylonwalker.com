---
date: 2025-12-10 08:46:36
templateKey: til
title: minecraft server memory
published: true
tags:
  - kubernetes
  - compose
  - docker
  - homelab
  - minecraft

---

I learned to today that setting `MEMORY` on your minecraft server causes the
JVM to egregiously allocate all of that memory.  Not setting it causes slow
downs and potential crashes, but setting `INIT_MEMORY` and `MAX_MEMORY` gives
us the best of both worlds.  It is allowed to use more, but does not gobble it
all up on startup.

In this economy we need to save all the memory we can!

Here is a non-working snippet for a minecraft server deployment in kubernetes.

``` yaml
      containers:
        - name: dungeon
          image: itzg/minecraft-server
          env:
            - name: EULA
              value: "true"
            - name: INIT_MEMORY
              value: "512M"
            - name: MAX_MEMORY
              value: "3G"
```

and in docker compose

``` yaml
  dungeon:
    image: itzg/minecraft-server
    environment:
      EULA: "true"
      INIT_MEMORY: "512M"
      MAX_MEMORY: "3G"
```
