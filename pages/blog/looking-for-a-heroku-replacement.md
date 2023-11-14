---
date: 2023-11-13 20:29:46
templateKey: blog-post
title: Looking for a Heroku replacement, What I found was shocking!
tags:
  - homelab
  - self-hosted
  - webdev
  - python
published: False
---

I've long hosted a by personal blog as a static site on waylonwalker.com. It's
all markdown, converted to html, and shipped as is. It's been great, I've
moved it from Github Pages, to netlify, tried vercel for a minute, and have
landed on Cloudflare Pages currently. Each migration has not really been that
hard, it's just pointing ci to a different host after the site has built.

[![screenshot of https://pages.cloudflare.com/](http://shots.wayl.one/shot/?url=https://pages.cloudflare.com/&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://pages.cloudflare.com/)

## What about server side

Now the part that I have struggled with is how to cheaply host a server
rendered application that can just live on forever without me paying for it.
This is a harder problem as it costs more to keep servers spinning, memory, and
disk all ready for you to use at a moments notice.

## Honestly

[![screenshot of https://heroku.com](http://shots.wayl.one/shot/?url=https://heroku.com&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://heroku.com)

I never really deployed anything that useful on heroku, but it seems like the
klenex of the bunch that's why they are in the title. I've moved between
digital ocean and fly.io, and have had some great experiences with both. I
just don't want to build something that is going perpetually cost money, I'm
cheap and dont want to feel the burden of paying for something that I might not
be using all the time.

## fly.io

[![screenshot of https://fly.io](http://shots.wayl.one/shot/?url=https://fly.io&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://fly.io)

fly is absolutely amazing to get off the ground. Their cli is top notch. They
have servers all over the place and have a great interface to get your
application deployed close to your users. You just can't run all that much on
it before you end up off the free tier.

## serverless

These platforms so far have just not felt right for me, again, I have to pay
for them, many of them I have to worry about how hard they would get hit, and
often they are focused on javascript.

## What I am looking for

- easy to deploy
- cheap to host
- free to use
- generous free tier
- no chance of big bills
- reliable, not 9 9's, but mostly up.
- allows me to run a bunch of stuff that I lightly use
- that buttery smooth cli that I get out of fly.io
- runs containers

The last one is probably the most important. I don't get tons of time to work
on side projects, and they are mostly ideas I just want to get out there and
play with, the idea may flop quickly, but I want that DX to be easy to go from
nothing to publically deployed.

## What about going back to self hosting??

I have a Gateway FX6860 built in 2011, and was gifted to me around 2016. She
doesn't have much power to her, but she does have more than free tier power. I
have 8 dedicated cpu, 16GB RAM, 500GB boot disk, and a 4TB hard disk.

## Cloudflare tunnels

[![screenshot of https://www.cloudflare.com/products/tunnel/](http://shots.wayl.one/shot/?url=https://www.cloudflare.com/products/tunnel/&height=600&width=1200&scaled_width=1200&scaled_height=600&selectors=)](https://www.cloudflare.com/products/tunnel/)

Cloudflare Tunnels allow me to route traffic to my own server sitting right
next to me and have it publically accessible. They take care of ssl certs,
they support wildcard routes, and configuration is pretty easy. I can map
addresses to a port on the machine, wildcard to a reverse_proxy, and end with a 404.

## I'm missing that buttery smooth cli

At this point I'm hosting a few things that I use frequently, but I don't have
that buttery smooth deploy experience that I get from fly.io. I have to log
into the machine, edit some files, and docker compose up every time I want to
deploy.

[![screenshot of https://kubernetes.io/](http://shots.wayl.one/shot/?url=https://kubernetes.io/&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://kubernetes.io/)
