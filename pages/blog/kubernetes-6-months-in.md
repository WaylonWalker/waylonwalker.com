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
blindly using its output so I have tried to use it less and less.  I'm now not solely leaning on it, but using it to get out quick POCs with low friction.

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
