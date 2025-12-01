---
date: 2024-06-09 10:06:30
templateKey: blog-post
title: What I'm learning in 2024
tags:
  - catalytic
published: True

---

2024 has been a learning fueled year, Diving deep into things I never would
have previously thought I would.  It's been a bit of a mix of the 🔥hot twitter
trends, and exactly what tech twitter tells you not to do.  It just goes to
show community is great, the tech community is filled with strong opinions, but
you need to think about what really makes sense for you, your career and your
customers (or lack there of).

## tech

* k8s
* tailwind
* fastapi
* htmx
* jinja
* opnsense

## successful one day builds

* play-outside
* reader
* thoughts
* thoughts chrome-extension

## Kubernetes

Damn did I sleep on k8s for way took long.  This is like exactly what I've
needed for a lot of things.  It's a perect example of what happens when you
listen to the tech community tell you.

[[ looking-for-a-heroku-replacement ]]

I started looking for something to make my homelab deployments easier at home.
Previously I needed to ssh into my server and fuss around with docker compose.
This just did not feel right for me to go into production and fiddle with it
like this.

In my search I keep seeing kubernetes crop up as the best solution.  I held off
for a long time, until I finally decided to give it a go.  I'm not sure if I
got lucky or what but my first few applications that I migrated in went
smooth as could be.

I chose to run k3s as this seemed like the lowest power consumption, easiest to
manage, and still allowed me to run multiple nodes.  At this point I was unsure
if I would use multiple nodes, but I did not want to take away the option out
of the gate.

I wrote a follow up article on my experience 6 monthts in.

[[ kubernetes-6-months-in ]]

## tailwind

Again I wrote off tailwind for a long time.  This time tech twitter really
likes it and tells me I should use it, but I already know css and I just don't
see the point of needing to use a framework.

It wasn't until thePrimeagen roughly said all css classes are shitty, everyone
writes shitty css classes, and you might as well use the same shitty css
classes everywhere that it really hit me, and I gave it a shot.

[[ a-case-for-tailwindcss ]]

What I really found was that having a designer lay out all of the rhythm,
spacing, and colors for you is really powerful.

I now have this site fully styled with tailwind, and even use md-it-attrs that
allow me to pop extra classes right in markdown and style posts like
[this]{.text-indigo-500 .text-lg}

## fastapi

I've been using fast api for a little while now but using it more and more in
2024.  It has a lot of really great ideas with dependency management, and
pydantic for moving data in and out of routes.

Here are some of the posts I've made about fastapi, theres defitely more to
come here, I have some Ideas that I am honing down around meeting users where
they are so that routes return the appropriate content type based on their
explicitly requested content type or assumed by user agent.

[[ fastapi-static-content ]]

[[ fastapi-jinja-url-for-with-query-params ]]

## htmx

I have posts about htmx going back to [[ htmx-get ]] on 3/25/2022.  I've been
interested for awhile, but just didn't really have the platform to use it till
recently.  My public content has been all static built content for a long time,
but now I am building applications for myself that are server rendered such as
[[ thoughts ]] and [[ odb-play-outside ]].  I've had more use cases
for using htmx.

The last pre-release of markata from 6/15/2022 now supports feed partials.
This gives me a really easy way to pop things like recent posts on the bottom
of every single page.  I'm sure I can do this with jinja, but htmx makes it
really easy to do and understand.  If its up and running you will now see a
Recent posts seciton below the article on this page powered by htmx.

## jinja

I've been using jinja for years now, but its mostly been some template
variables here, some loops there.  Now that I am putting fastapi and htmx to
work I am really learning how to setup and design templates properly.  Building
up from a good re-usable base, including partials that so that pages can be
rendered as full pages or partials.

## just

I have long been using my shell history to re-run complex shell commands that I
use to build projets, compile tailwind, build docker images, run docker in
local development.  Most of the time they are not complex, but sometimes are
something that would take me a few minutes to remember if I lost my shell
history without it being documented

I've started storing all these things that I can in just.  If its something
that I get from my shell history I start thinking about how it would belong in
a justfile.  I've tried a few others over the years but they always seem tied
to a language or build tool, just is language agnostic and runs in any
terminal.  Worst case, someone does not want to install it they can copy paste
out of the justfile.

Biggest benefit is that it communicates to others what I do when I am working
on a project.  There are some good competitors like runbook that run readmes,
but just has been working great for me and easy to use.
