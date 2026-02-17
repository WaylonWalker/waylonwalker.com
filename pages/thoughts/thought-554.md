---
title: '💭 Developer Productivity, v2 with ThePrimeagen | Preview - YouTube'
date: 2025-02-08T15:29:52
templateKey: link
link: https://www.youtube.com/watch?v=03KsS09YS4E
tags:
  - dev
published: true

---

> Big fan of Primes setup.  I was not far off of his setup before he really came on the scene, but I've picked up a ton of nuggets from him and how he operates.  I took his first developer productivity course on Front End Masters as it came out.  

It is interesting to see him roll back his ansible scripts for bash scripts here.  I converted my setup to ansible after watching his first, but have also since rolled back to bash scripts for quite similar reasons.  Ansible is great for remote tasks that need to be done on a fleet of machines, but like he says here overkill for this purpose and ends up something that you need to read the docs for every change to your dotfiles.

Unlike prime I've really leaned harder on installing everything in a docker image and developing out of a docker image.  I've long built docker images of my dotfiles with the idea that its nice to be able to just use them on other machines, but it rarely happened.  

In the past year I've moved bazzite, an immutable distro.  It comes with podman and distrobox, so I install very little on it, a few flatpaks from the store for brave and signal, but most of what I really use day to day comes from my devtainer.  It's nice that I really have one install target for all of my scripts so they become quite stable.  I don't need to worry about arch vs ubuntu vs fedora, no matter where I am its the same base image.

I've also really started to lean on kubernetes, it is so useful to just be able to start a pod in k8s using the same exact develop setup as I would have locally.  Nothing needs installed, I can just bring my dev setup to the cluster where the network and data I might need to debug is.



[Original thought](https://www.youtube.com/watch?v=03KsS09YS4E)
