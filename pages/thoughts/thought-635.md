---
title: '💭 Chris Biscardi''s Digital Garden'
date: 2025-05-12T13:05:33
templateKey: link
link: https://www.christopherbiscardi.com/wtf-is-kubernetes
tags:
  - k8s
published: true

---

> Interesting take on kubernetes from a front end perspective.  All valid arguments to me, and really the answer to any do you **need** to any specific implementation of tech is probably no.  We got along just fine before k8s ever existed and you still can, but its really nice in a lot of cases.  If your skills lean toward backend or infrastructure I encourage you to give it a try.  


## k8s _distros_

There are a lot of beginner friendly k8s distros that you can setup with relative ease, kind and k0s are great for single node, If you want multi-node k3s is what I generally use.  If you want a very lightweight OS that you only interact with through an api, and has a very small attack surface talos is an amazing product.

## When else might you want k8s

Internal, on-prem, self hosted.  If you are trying to avoid the cloud for cost, rules, regulations, red tape, kubernetes is a great option to manage your container workflows yourself without needing to have a cloud budget, get approvals and sign offs on running workflows in a public cloud.

[Original thought](https://www.christopherbiscardi.com/wtf-is-kubernetes)
