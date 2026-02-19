---
title: '💭 Can I access k3s using just kubectl (no sudo and no k3s comman...'
date: 2023-10-20T22:52:00
template: link
link: https://www.reddit.com/r/kubernetes/comments/cojjf5/can_i_access_k3s_using_just_kubectl_no_sudo_and/
tags:
  - homelab
  - k3s
  - thoughts
  - thought
  - link
published: true

---

![[https://www.reddit.com/r/kubernetes/comments/cojjf5/can_i_access_k3s_using_just_kubectl_no_sudo_and/]]

Right after installing k3s you are going to need to use `sudo` to use any `kubectl` command.  The reason for this is that the default config is owned by root.  To get around this you will need to make your own config and set the `KUBECONFIG` environment variable

To do this I used `sudo` one last time to copy the `k3s.yaml` file into my own directory and take ownership of it.

``` bash
sudo cp /etc/rancher/k3s/k3s.yaml /home/waylon/.config/kube

sudo chown -R waylon:waylon ~/.config/kube

export KUBECONFIG=~/.config/kube/k3s.yaml
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
