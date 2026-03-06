---
title: '💭 Quick-Start Guide | K3s'
date: 2023-10-20T21:32:03
template: link
link: https://docs.k3s.io/quick-start
tags:
  - homelab
  - k3s
  - thoughts
  - thought
  - link
published: true

---

![[https://docs.k3s.io/quick-start]]

I recently spun up k3s in my homelab.  I'm trying to offload some work off of my free tier fly.io app in order to keep it free tier without crashing.


``` bash
# install and start k3s
curl -sfL https://get.k3s.io | sh -
# check to see if your nodes are started
sudo kubectl get nodes
```

My main hiccup so far was the machine I am running on runs zfs on root, and it would not start the master node.  Rather than figuring out how to make zfs play nice I just pointed k3s to a drive that is not zfs.

``` bash
# manuallly
sudo k3s server -d /mnt/vault/.rancher/k3s
# without editing systemd service
sudo ln -s /mnt/vault/.rancher/k3s /var/lib/rancher/k3s
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
