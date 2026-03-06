---
title: '💭 We need to have a talk... - YouTube'
date: 2025-01-02T03:04:14
template: link
link: https://www.youtube.com/watch?v=_VQl_HTk9PM&t=2607s
tags:
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://www.youtube.com/watch?v=_VQl_HTk9PM&t=2607s]]

Theo does a fantastic history of serverless here.

## Kubernetes shit

Theo can't have an infra video without shitting on k8s.  Specifically people who have never touched k8s pushing fear of k8s to large audiences of people who have never touched k8s.  If you are a webdev who solely lives in webdev space and never touches as much as a dockerfile listen to him.  If you touch infra at all try it before you take his opinion at face value.

![image](https://dropper.wayl.one/api/file/a84ec689-e84f-458a-b1d6-fec85b310023.webp)

## Serverless shines in high variance

If you plan on having traffic spikes 10x your regular traffic for something like black friday, serverless might be right for your use case.

## stateless programming

He argues that targeting a stateless deployment of serverless leads to better code.  I'd like to see more examples here.  Maybe most of the code bases I work on already do this.  I've never targeted a serverless deployment, but I've targeted horizontally scaled deployments many times and they feel like they have the same targets.  For instance if I spin up 8 pods for my application or uvicorn with 3 workers I have to target statelessness, all of the state must live in the database and cannot live in memory.  Even if I target 1 instance in a containerized environment I have to be ready for restarts at any point in time.

I might be missing something here, but I don't see how this point applies to serverless.

## Scale to Zero Services

![image](https://dropper.wayl.one/api/file/a06523f8-35e1-46cf-83b8-fd6be0831d93.webp)

https://www.youtube.com/watch?v=_VQl_HTk9PM&t=2607s

Companies that can run on scale to zero can allow your shitty side projects that have no users run for free indefinitely because it costs them nothing.  He compares planetscale running mysql vs Turso running SQLite stored in s3.

## Everything he covers is really cloud to cloud

He compares early deployments of LAMP and MEAN stack running on one server then jumps to serverless.  It feels like he is missing the angle of owning your own hardware.  This might just be the experience difference between theo and DHH.  DHH works on one focused company, Theo is jumping around between startups.

## Ok I get some of it

At the end he covers a dumb side project that has branch deploys.  It had a 100s of deploy still running, some very old, some never even touched, vercel can do this because it costs them nothing if its not running.  What I didn't think about right away is that there is probably a backend component to this.  

In my python backends I often have deploy environments, but since they don't scale to zero they have at least some cost even if its small, with this I cannot just keep hundreds of them running because that cost would add up.

I would argue that this is hardly useful, because you can checkout any old version and run it locally, and you rarely are going to need to poke through these old branch deploys.  But in that case that you need to quickly do this serverless is definitely superior.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
