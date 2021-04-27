---
templateKey: blog-post
tags: ['docker', 'linux']
title: 📝 Docker Deep Dive - Notes
date: 2021-04-23T09:41:29
status: draft

---

https://www.hanselminutes.com/784/doing-open-source-with-brian-douglas

## Play With Docker

A handy way to try weird things in docker is using
[play-with-docker](play-with-docker.com).  You get a four hour session for
free, after four hours everything will be deleted, but you can start a new
session.

### Installing Docker on Linux

Installing on Ubuntu.

``` bash
wget -qO- https://get.docker.com/ | sh
```

### Running Docker commands without sudo

In order to run docker commands without using sudo you need to add docker to
your group.


``` bash
sudo usermod -aG docker ubuntu
```

## Architecture and Theory


**Container** - Isolated area of an OS with resource usage limits applied.

Namespaces and Control Groups are hard, which is why containers were unusable
by mortals before docker.



## Namespaces
_Isolation_

Each container looks and feels like a regular OS. It has its own eth0, users,
kernel.  These are completely isolated from every other container running on
the system.

Namespaces are analogous to what Hypervisors do on hardware.

* Process ID (pid)
* Network (net)
* Filesystem/mount (mnt)
* Inter-proc comms (ipc)
* UTS (uts)
* User (usr)

##  Control Groups
_Resource usage limits_






