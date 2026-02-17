---
title: '💭 podman requries qemu-system on ubuntu'
date: 2024-06-12T19:29:18
templateKey: link
link: https://askubuntu.com/questions/1490805/how-do-i-install-qemu-on-ubuntu-23-10
tags:
  - linux
  - podman
  - container
published: true

---

> podman requires qemu-system on 


``` bash
❯ podman machine init
Looking up Podman Machine image at quay.io/podman/machine-os:5.1 to create VM
Extracting compressed file: podman-machine-default-amd64.qcow2: done
Error: exec: "qemu-img": executable file not found in $PATH
```

The fix to this for me was to install qemu-system before podman machine init.


``` bash
sudo apt update

sudo apt install qemu-system
```


[Original thought](https://askubuntu.com/questions/1490805/how-do-i-install-qemu-on-ubuntu-23-10)
