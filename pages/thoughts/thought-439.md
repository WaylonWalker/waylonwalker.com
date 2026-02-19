---
title: '💭 Using OPNsense with Tailscale · Tailscale Docs'
date: 2024-12-03T17:37:52
template: link
link: https://tailscale.com/kb/1097/install-opnsense
tags:
  - opnsense
  - tailscale
  - thoughts
  - thought
  - link
published: true

---

![[https://tailscale.com/kb/1097/install-opnsense]]

On reboot of my opnsense router it did not tailscale up.  I'm not sure if a key expired or what happened.  The fix was to first enable ssh, then ssh in and run tailscale up.

## enable ssh

In opnsense System > Settings > Administration > Secure Shell > Enable Secure Shell

## tailscale up

``` bash
ssh <opnsense ip>
8 # to select shell
tailscale up
```

Follow the link to log in.

## disable ssh

now uncheck secure shell to lock down the opnsense machine.


In opnsense System > Settings > Administration > Secure Shell > Enable Secure Shell


!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
