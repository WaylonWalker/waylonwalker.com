---
date: 2025-11-18 18:39
templateKey: blog-post
title: Another Big Cloud Outage Nov 2025
published: true
tags:
  - cloud
---

Today I woke up to finding out that cloudflare hade a widespread outage.  My [[Reader]] uses tailwind cdn for styles and it was down. Otherwise it was not so impactful to me and felt kike they were quick to have it up.

> I'm not really researching here, just jotting thoughts down from a parking lot waiting for pickup.

It feels like we are seeing a lot of these lately.  They feel much more frequent.  It feels like a whole industry was sold on 9's and reliability of big cloud that we just aren't getting.  

There's a huge push to go back to self hosting, racking and stacking.  I think this is great.  I love it.  I'm a big proponent for ownership and self hosting.  It's not the right move for everything and everyone, and is certainly not something to make a knee jerk reaction about in the moment of frustration.

There's a lot of things that are just impossible to do yourself, cdn caching, edge compute, ddos protection.

These companies are not magic they are vulnerable to changes just like you and I.  It really feels like more and more of these are due to misconfigurations, and small bugs introduced.  As we see big tech downsize and lean more on ai that likes to do big code changes I dont see it getting better soon.  Theres a lot of things we can all armchair quarterback about here, better testing, review, canary deployment, staged rollouts, rigorous review.  All great things.  I can hear Uncle Bob talking about rigor, giving a shit, and following principles.  

We are at odds of reliability and speed.  This critical infrastructure runs so many important things in our lives it feels like it deserves a professional engineer signoff on changes.  Documentation of changes and testing done between changes.  This would all but hault forward progress, taking us back to the level of physical components and manufacturing.

How do you decide what needs this rigor and how to regulate it when companies are incentized by number go up.

The answer right now is that we can't and if you are managing critical infrastructure you need to take these outages into account in your disaster recovery plan and understand what you are willing to allow go down on failure.
