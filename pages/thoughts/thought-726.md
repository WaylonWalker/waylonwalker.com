---
title: '💭 { TechDufus } | Building a Talos Kubernetes Homelab with Terra...'
date: 2025-07-02T01:45:11
templateKey: link
link: https://techdufus.com/tech/2025/06/30/building-a-talos-kubernetes-homelab-on-proxmox-with-terraform.html
tags:
  - 
published: true

---

> I've ran my homelab on k3s for a year and a half now, and have had talos fomo the whole time.  I'm not sure if this article helps or hurts.  Helps to see that techdufus struggled and wished he went k3s first, but theres so much good to it that I want it.

## Prometheus and Grafana for monitoring (because you can’t manage what you can’t see)

I'm getting there, ok, I have some of it figured out but not firing on all cylinders like I want.

## CloudNativePG

> for PostgreSQL (way better than managing databases manually)

Amen to this, cnpg is kick ass and has me tempted to drop sqlite for my production database default.  I mostly make small shit on the side that is never going to blow up.  sqlite is really good, but the automation that comes along with cnpg to just run it on all nodes and backups once you establish the pattern with the first one is sick.

## 🤣🤣🤣 actually read the docs 🤣🤣🤣

![image](https://dropper.wayl.one/api/file/9c41132e-7808-49af-9aaa-68a5e5870a4b.webp)

## Is This Overkill for a Homelab?

>Absolutely. Could do most of this with k3s or Docker Compose. But where’s the fun in that?

Speaking my language here!  Again I'm well past the 1 year mark of running k3s and i've had no regrets.  Kubernetes is about establishing and replicating patterns, its a dream to deploy to.  It gets so much hate for being obtuse, hard to use, yaml intense.  You get full control of ever damn thing you need through configuration, and if you keep it simple you can deploy some sick shit out of it without needing to go hard on the yaml, again, think really hard about it a few times, and replicate.


[Original thought](https://techdufus.com/tech/2025/06/30/building-a-talos-kubernetes-homelab-on-proxmox-with-terraform.html)
