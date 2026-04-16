---
templateKey: blog-post
title: Waylon Walker
tags:
  - meta
  - slash
date: 2021-11-20T10:38:00
published: true
jinja: True

---

## Hi, Hello, I'm Waylon

Husband, dad of two, and hobbyist builder of things on the internet.

When I'm not wrangling data pipeline platforms or building web platforms,
you'll find me [[ tags/gaming | gaming ]] with my kids, making art, or skating
around the neighborhood.  Reliving my mechanical engineering days with my 3d
printer.  Winding down at the end of the day binge-watching Big Bang Theory
with my wife.

## What I Do

I'm a Senior Software Engineer who specializes in data pipelines and
Python-based web platforms. I help teams turn messy data into reliable systems
that actually work.

## Why I Built This Site

_from scratch_

I got tired of:
- Build times that took forever
- Node modules folders that became black holes
- Bloated pages that took ages to load
- SEO tools that felt like an afterthought

So I built my own platform from scratch using **pluggy** and **diskcache**.
It's under-funded, over-dreamed, barely documented, and I love it. This site is
my sandbox for learning, teaching, and sharing ideas on my own terms.

## Infrastructure

Because apparently I don't have enough hobbies, I also run this site from a
**[[ tags/kubernetes | Kubernetes ]] cluster in my basement**. Nothing says "I
love DevOps" like maintaining your own bare-metal cluster just to host a static
blog.

## Explore

Curious about the tech? Check out [[ about-this-site ]] for my philosophy on
this space, or [[ colophon ]] for the full stack breakdown.

## Meta Pages

Evergreen pages about me and this site:

{% for post in markata.feeds.meta.posts %}* [[ {{post.slug}} ]] - {{post.description}}
{% endfor %}

 
