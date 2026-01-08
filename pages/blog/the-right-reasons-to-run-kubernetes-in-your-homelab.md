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

## The Right Reasons To Run Kubernetes In Your Homelab

_There are not many_

* You want to learn kubernetes
* You like kubernetes
* You want to **learn** to scale

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

This is probably a stretch reason, maybe not a good one, there are probably
better ways, but here we go.

Don't claim that you **need** scale in your homelab, you don't.  But it sure is
fun to run a cluster of nodes, and load balancing services that run across
them.  Solving these hard problems to scale across machines is hard.  There's
no way around it, there's a lot to think about.  Doing so in a low stakes
environment that you have skin in the game is a great way to learn.

## I run kubernetes in my homelab

I run it and I really like it

> What flavor of autism did you guys get, I got the kind where I run kubernetes in my basement.

Here are some things I really like about it, and Yes I know you can achieve
most of these without kubernetes.

* I don't have to ssh, hardly ever.
* I can see everything I'm running, and its defined in a manifest
* k9s is amazing, and I use it all the time.
  * shell into running pods
  * restart deployments
  * scale deployments
  * trigger cronjobs
  * watch logs
  * I can scale our minecraft server to 0 in seconds if we are in a different season of life
* ArgoCD is amazing
  * I ❤️ gitops
* Ingress just works
* Longhorn 
  * makes snapshots and backups easy
  * makes multi node easy
* zero-downtime deployments
* self healing health checks

I mostly do very simple things, deployments with a container, a volume and
ingress.  Probably things that you could easily run on fly.io.  Theres nothing
really fancy.  I just like how easy this setup works for **me**.

![She's our friend and she's crazy](https://dropper.waylonwalker.com/file/f8e88b6b-a668-4cea-9792-65339860b07f.webp)
