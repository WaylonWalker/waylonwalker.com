---
title: '💭 Kubernetes Isn''t for You'
date: 2025-08-02T14:40:42
templateKey: link
link: https://sliplane.io/blog/kubernetes-isnt-for-you
tags:
  - kubernetes
published: true

---

> This post feels like it was written by someone who has never tried kubernetes, someone who reads twitter, listens to t3.gg and thePrimeagen (who cant even container let alone kubernetes).  If you cant run linux, use bash, build your own docker images, run docker comfortably.  If infra is not your thing kubernetes is probably not for you.

> Kubernetes Was Built for Google

Just like how react was built for facebook to solve facebook problems with many teams contributing effectively to the same interactive interfaces.  Turns out that react is actually a pretty good product if you have a highly interactive page, and if this is your bread and butter, you can make overly heavy static sites with too much build very effectively.  It works and runs much of the internet now.

> We are getting serious. We need serious tools.
> Big companies use Kubernetes. We should too.
> It feels more professional. It sounds like we know what we are doing.

If anyone uses these reasons to pitch kubernetes to me they don't belong in a position to make any sort of decision.  The first one could be a heading with maybe something under it.

> But Kubernetes should not be your first infrastructure step. It should be a response to real pain, not an emotional milestone

As with anything, **it depends**!  Keeping with the react example, if you have a team with these skills its a solid choice, maybe its overkill, but you got this skills to start here then go for it.

---

If you have never given something a real shot then don't be writing articles shitting on the tech.  Actually if you do not have a deep expertise in it you probably should not be writing articles shitting on other tech.  If you are the CEO of an alternative, you definitely should not be writing articles shitting on your competition.  [ just build the biggest fucking building in town ](https://garyvaynerchuk.com/build-the-tallest-building-in-town/).

If you are kube curios give kind and kompose a try, you will be surprised at how quickly you can get something up and running in kubernetes.  You might be surprised at how easy it is to remotely manage, add gitops workflows with [argocd](https://argoproj.github.io/cd/).  Give [k9s](https://k9scli.io/) a try and you can see all of your nodes, services, ingress, pvcs, EVERYTHING you have deployed and its status in one easy to use TUI.

I avoided kubernetes for a long time because articles like this told me to and I never gave it a fair try.

Check out [[ just-fucking-use-kubernetes ]] for a satirical opposite take.

[Original thought](https://sliplane.io/blog/kubernetes-isnt-for-you)
