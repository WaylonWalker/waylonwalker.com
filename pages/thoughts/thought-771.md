---
title: '💭 csi-driver-smb/deploy/example/smb-provisioner at master · kube...'
date: 2025-08-01T19:50:39
template: link
link: https://github.com/kubernetes-csi/csi-driver-smb/tree/master/deploy/example/smb-provisioner
tags:
  - self-hosted
  - homelab
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/kubernetes-csi/csi-driver-smb/tree/master/deploy/example/smb-provisioner]]

Great guide to setting up a samba server right in kubernetes.  I tried it out after too long of playing with trying to get connected to a samba share on ucore, no idea what was wrong, but this just works, and will live in my homelab no matter what distro I'm on, no playbook required to set it up, just good ol k8s manifest.  TBH I cheated and haven't set up the secrets yet, so its not quite in argocd or in my github repo, but POC is there and it works as advertised without issue.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
