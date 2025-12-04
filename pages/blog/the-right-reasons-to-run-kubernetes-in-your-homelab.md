---
date: 2025-12-10 09:48:14
templateKey: blog-post
title: The Right Reasons To Run Kubernetes In Your Homelab
tags:
  - kubernetes
  - self-hosted
  - homelab
published: True

---

Running kubernetes in your homelab is a fantastic way to learn, explore, express
yourself, and run services that you use.

* You want to learn kubernetes
* You like kubernetes
* You want to learn to scale

There are also [[ the-wrong-reasons-to-run-kubernetes-in-your-homelab ]]

## You want to learn kubernetes

Homelabbing is a such a great way to learn new skills, deploy real apps that
you use.  Create new custom apps for your specific use cases that no one else
has.  You should absolutely run kubernetes in your homelab if you want to learn it.

I would recommend to start locally, pull up kind, minikube, or k3d and start
from your local machine before putting it on a server.

When you decide you are ready for a server, you probably don't need any crazy
hardware.  You can probably run on some old retired Dell Optiplex or an old
desktop someone is throwing out as it no longer runs windows.

## You like kubernetes

Hell Yeah Brother, 100% no better reason to run kubernetes at home than because
you enjoy it.  I'm with you.  There's nothing quite like having git ops kick in
and deploy new services, updates, watching deployments rollover with zero
downtime.  Watching your cluster heal itself when a node goes down.  Never
ssh-ing in to do deployments.  Still owning your entire hardware.

## You want to learn to scale

Don't claim that you **need** scale in your homelab, you don't.  But it sure is
fun to run a cluster of nodes, and load balancing services that run across
them.  Solving these hard problems to scale across machines is hard.  There's
no way around it, there's a lot to think about.  Doing so in a low stakes
environment that you have skin in the game is a great way to learn.

