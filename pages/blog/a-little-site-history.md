---
date: 2026-10-20
title: A Little Site History
description: A winding history of waylonwalker.com, from the domain and early blog through hosting changes, Markata, thoughts, pings, and Markata Go.
published: true
draft: false
tags:
  - meta
  - blog
authors:
  - id: gpt-6-luna
    role: researcher and author
template: post
---

I went looking for the beginning of this site.  The trail is split between old
GitHub repositories, the current site, and a few projects on my Forgejo server.
Some dates are solid commit dates.  Others come from my own recollection written
down later.  This is the winding road I can reconstruct so far.

The earliest public clue is my own [about this site](/about-this-site/) page:
I registered the domain and started making content in 2017, after a rough year
in tech made me want a place and a body of work I controlled.  The Git history
does not reach that far.  The oldest surviving repository I found is
[`waylonwalker`](https://github.com/WaylonWalker/waylonwalker), whose first
commit is July 8, 2020.  That is the start of the Git trail, not the start of
the site.

::: road winding

- [A domain of my own](/about-this-site/) 2017
- [First surviving site repo](https://github.com/WaylonWalker/waylonwalker/commit/09b6b657ac43ee1dfb94815c40b2a3c1cafd42fe) July 2020
- [The Markata rebuild](https://github.com/waylonwalker/waylonwalker.com/commit/f3aad49a) March 2021
- [Notes find their way in](https://github.com/waylonwalker/waylonwalker.com/commit/9da75145) June 2021
- [Netlify gives way to Cloudflare Pages](/colophon/) by October 2021
- [The separate thoughts project starts](https://git.waylonwalker.com/waylon/thoughts/commit/b922026) July 2023
- [Thoughts join the site](https://github.com/waylonwalker/waylonwalker.com/commit/c5c28bad) September 2023
- [The homelab starts running site tools](https://git.wayl.one/waylon/shot-scraper-api/commit/3fa493c) October 2023
- [I start running Kubernetes at home](/kubernetes-6-months-in/) December 2023
- [Dropper begins storing my media](https://git.wayl.one/waylon/dropper/commit/a11cd70) December 2024
- [The main site gets a homelab build job](https://github.com/WaylonWalker/homelab-argo/commit/b5acd1d) January 2025
- [Forgejo enters the workshop](/trying-forgejo/) August 2025
- [Kubernetes becomes the site's home](/why-make-a-website-in-2025/) September 2025
- [Pings begin](https://github.com/waylonwalker/waylonwalker.com/commit/eef61427) December 2025
- [The Markata Go migration begins](https://github.com/waylonwalker/waylonwalker.com/commit/be02be8c) January 2026
- [A new home page takes shape](https://github.com/waylonwalker/waylonwalker.com/commit/c7d6f82d) March 2026
- [The Markata Go migration lands](https://github.com/waylonwalker/waylonwalker.com/commit/a26fc215) April 2026
- [Thoughts gets an Argo deployment](https://github.com/WaylonWalker/homelab-argo/commit/dd37bf7) May 2026

:::

## The site keeps moving

The first site was a blog, and the hosting moved around with it.  From the
posts and deployment history, I can trace Netlify, Cloudflare Pages, and then
the basement Kubernetes cluster.  GitHub Pages also appears in the repo's
deployment experiments, but the posts do not give me a clear date when it
served the main site.  Cloudflare Tunnel now carries the self-hosted site out
to the internet.

The code changed just as much.  In March 2021 I started a new version of the
site built with Markata, the static site generator I was making for myself.
The first commit is literally called `init v3`.  Markdown and frontmatter
became the durable part.  The generator could change without taking all the
writing with it.

The hosting trail is less tidy.  In February 2020, I wrote that the site had
been on Netlify for nearly two years, which puts that move around 2018.  By
October 2021, my deployment writeup says I had moved to Cloudflare Pages.  The
homelab repo shows the screenshot service using Kubernetes by October 2023.
It adds a build job for waylonwalker.com in January 2025, and in September
2025 I wrote that I was building the site in Kubernetes.  That narrows the
site's move from Cloudflare Pages to the homelab to sometime in 2025.  The
exact cutover day is still hiding from me.

Thoughts took a different route.  Its Fly.io config dates to July 2023, and
the service stayed on Fly.io for years while the main site could pull thoughts
into its feed.  In May 2026, the homelab Argo repo adds a Kubernetes
application for it.  That looks like the end of the long Fly.io chapter,
though the Argo commit alone does not prove the date Fly was shut down.

I started collecting notes in the site repo that spring.  In September 2023,
I added the thoughts plugin and began pulling short posts into the same place
as the longer articles.  Pings arrived later, in December 2025, as another
way to publish smaller bits while the idea is still warm.  Notes, thoughts,
and pings are different names for a similar itch: get the thing out of my
head and somewhere I can find it again.

In January 2026 I began moving the site from Python Markata to Markata Go.
The migration branch landed in April.  It was another rewrite of the
machinery, and another chance to shape the publishing system around how I
actually write.  The home page was rebuilt around the growing pile of posts,
notes, and small updates during the migration.

This is not a straight line from simple blog to finished platform.  It is a
long series of experiments, new homes, and new ways to put words on the web.
The useful part is that the domain and the writing kept coming along for the
ride.

## Sources

This timeline combines commit history from the old GitHub site repositories,
the Forgejo-hosted thoughts, Dropper, and shot-scraper-api projects, and the
homelab and homelab-argo repositories.  I cross-checked those with recollections
in [about this site](/about-this-site/), the deployment writeups, and the
[colophon](/colophon/).  The 2017 starting point comes from that recollection.
The 2020 date is the earliest surviving repository commit I found.  Hosting
cutovers are less completely recorded than code changes, so the main site's
move to Kubernetes is a window rather than a day.
