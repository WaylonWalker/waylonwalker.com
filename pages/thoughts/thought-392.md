---
title: '💭 add init hooks and exported bins · WaylonWalker/devtainer@2e4c6da'
date: 2024-09-28T01:34:08
templateKey: link
link: https://github.com/WaylonWalker/devtainer/commit/2e4c6da537f5672209d1b3922fad754190aef938#diff-38878343c551520f8af2a3986e5f6085b03df197a56a92abc42a44b200f0264aR19
tags:
  - docker
  - podman
  - distrobox
published: true

---

> Today I learned that you can use init_hooks to access host machine commands from inside a distrobox container.  This is super handy for things that you cannot get to from inside the container and need ran outside (docker, podman, flatpak, xdg-open).

``` bash
init_hooks=ln -sf /usr/bin/distrobox-host-exec /usr/local/bin/podman;
```

[Original thought](https://github.com/WaylonWalker/devtainer/commit/2e4c6da537f5672209d1b3922fad754190aef938#diff-38878343c551520f8af2a3986e5f6085b03df197a56a92abc42a44b200f0264aR19)
