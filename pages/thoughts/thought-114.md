---
title: '💭 How to run pods as systemd services with Podman | Enable Sysadmin'
date: 2023-09-22T01:12:19
template: link
link: https://www.redhat.com/en/blog/podman-run-pods-systemd-services
tags:
  - linux
  - podman
  - container
  - thoughts
  - thought
  - link
published: true

---

![[https://www.redhat.com/en/blog/podman-run-pods-systemd-services]]

podman comes with a nice command for generating systemd service files (units).

``` bash
$ podman pod create --name=my-pod
635bcc5bb5aa0a45af4c2f5a508ebd6a02b93e69324197a06d02a12873b6d1f7

$ podman create --pod=my-pod --name=container-a -t centos top
c04be9c4ac1c93473499571f3c2ad74deb3e0c14f4f00e89c7be3643368daf0e

$ podman create --pod=my-pod --name=container-b -t centos top
b42314b2deff99f5877e76058ac315b97cfb8dc40ed02f9b1b87f21a0cf2fbff

$ cd $HOME/.config/systemd/user

$ podman generate systemd --new --files --name my-pod
/home/vrothberg/.config/systemd/user/pod-my-pod.service
/home/vrothberg/.config/systemd/user/container-container-b.service
/home/vrothberg/.config/systemd/user/container-container-a.service
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
