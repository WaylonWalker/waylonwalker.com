---
date: 2025-12-06 09:46:47
templateKey: blog-post
title: The Wrong Reasons To Run Kubernetes In Your Homelab
tags:
  - kubernetes
  - self-hosted
  - homelab
published: True

---

Running kubernetes in your homelab is complex, time consuming, there are almost
no docs to help you (homelab focused docs for things you want to install), and
nothing is copy paste.  You have to make everything happen yourself.

## The Wrong Reasons To Run Kubernetes In Your Homelab

* I run compose and think kubernetes is the next logical step
* Techno Tim runs it
* I heard it's what cool kids do
* Kubernetes BTW
* Talos Linux looks cool
* I found a cool helm chart on GitHub
* I need scale

There are also [[ the-right-reasons-to-run-kubernetes-in-your-homelab ]].

## I run compose and think kubernetes is the next logical step

No it's not.  It's much different than running docker, compose, swarm.  It's
meant for scale, it's complex, it's made for enterprise, not your local
development or your homelab.  It can do these things, it can do them quite
well, but it's not the target audience.

## Techno Tim runs it

_I heard it's what cool kids do_

You need to rethink who the cool kids are, touch some grass.  Tim also does it
for his job, he likes it, he knows it, he wants to lean on it and learn more.

## Kubernetes BTW

Kubernetes does not make you look cool, it makes you look like you are trying
to over optimize and over engineer your life.  It's not worth it, in fact
nothing in life is worth worrying about what everyone else thinks of you.

## Talos Linux looks cool

Talos is an S tier OS wherever you deploy it.  It is a secure, minimal,
kubernetes first OS.  They also have some really great people working there
putting Talos in some really cool places like
[backpack](https://justingarrison.com/blog/petaflop-cluster/) or [Apple Power
Mac](https://justingarrison.com/cubernetes/)

## I found a cool helm chart on GitHub

No you didn't.  Everything in homelab is compose first.  A few things have a
k8s option, but almost nothing is k8s first.

## I need scale

No.  You're homelab does not need scale.  If you think it does, you have some
real shit hardware, some bad optimizations, or somehow you have a startup you
need to launch cause you got more users than most.
