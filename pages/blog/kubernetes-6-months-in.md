---
date: 2024-03-26 13:20:24
templateKey: blog-post
title: kubernetes 6 months in
tags:
  - kubernetes
published: True

---

 I stumbled into kubernetes December 2023 when I was looking for a better way
 to self host applications.  I was looking for something that didn't require
 logging into a server and building and deploying like a cave man.  I wanted a
 smoother experience than docker compose was giving me.

[https://waylonwalker.com/looking-for-a-heroku-replacement/](https://waylonwalker.com/looking-for-a-heroku-replacement/){.hoverlink}

This post turned into a list of tools that I have adopted into my k8s workflow,
and plan to keep. enjoy.

## Kompose

<a href='https://kompose.io' >
<img
    src='https://shots.wayl.one/shot/?url=https://kompose.io/&height=450&width=800&scaled_width=800&scaled_height=450&selectors='
    alt='screenshot of https://kompose.io/'
    height='450'
    width='800'
/>
</a>

Kompose is a great tool for gettting going and converting your docker-compose
to kubernetes manifests or helm templates.  It was a great tool for me to get
started with, but I was afraid that it was hindering me learning more and just
blindly using its output so I have tried to use it less and less.  I'm now not
solely leaning on it, but using it to get out quick POCs with low friction.

Kompose really helped me go 0 to 60 and get right into kubernetes with my
existing docker compose files and very little change.  I found it a great way
to get my feet wet and learn.

## Argocd

[https://argoproj.github.io/cd](https://argoproj.github.io/cd){.hoverlink}

<a href='https://argoproj.github.io/cd/' >
<img
    src='https://shots.wayl.one/shot/?url=https://argoproj.github.io/cd/&height=450&width=800&scaled_width=800&scaled_height=450&selectors='
    alt='screenshot of https://argoproj.github.io/cd/'
    height='450'
    width='800'
/>
</a>

Argocd is the first tool I am going to reach for in any kubernetes deployment
that I work on.  The number one reason is that it keeps track of all of
everything internally, and if you remove something it cleans it up.  Very
quickly if you are not diligent you will end up with stuff laying around not
sure if you need it, or where it came from.

For instance if I create a new deployment and don't include the namespace, If I
just change the yaml with the new namespace without taking it down first, that
original one will be left behind and I will be stuck manually cleaning it up.

## Argo Rollouts

[https://argoproj.github.io/rollouts](https://argoproj.github.io/rollouts){.hoverlink}

<a href='https://argoproj.github.io/rollouts/' >
<img
    src='https://shots.wayl.one/shot/?url=https://argoproj.github.io/rollouts/&height=450&width=800&scaled_width=800&scaled_height=450&selectors='
    alt='screenshot of https://argoproj.github.io/rollouts/'
    height='450'
    width='800'
/>
</a>

I'm looking into rollouts, and have played with it, but argocd really does most
of what I need with low friction.  I thought I needed rollouts to prevent
downtime, but argo tends to do a good job of cutting over to a new pod only
after its up and ready.  This solves most of my problems, and I can pretty
quickly roll back with low friction.  If I needed to manage a high availabilty
application Id look closer.

## KubeSeal

[https://sealed-secrets.netlify.app/](https://sealed-secrets.netlify.app/){.hoverlink}

<a href='https://sealed-secrets.netlify.app/' >
<img
    src='https://shots.wayl.one/shot/?url=https://sealed-secrets.netlify.app/&height=450&width=800&scaled_width=800&scaled_height=450&selectors='
    alt='screenshot of https://sealed-secrets.netlify.app/'
    height='450'
    width='800'
/>
</a>

KubeSeal is a fantastic low friction pair to argocd.  The biggest benefit to
kubeseal is that you can safely commit secrets straight to git.  It uses a one
way encryption method that is very secure and you can only decode the secrets
if you gain access to the keys.

[[ kubernetes-kubeseal ]]
