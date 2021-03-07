---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Should I switch to Zeit Now
date: 2020-02-06T22:38:00Z
status: published
description: Should I switch to Zeit Now.  Netlify build times are starting to creep
  in.
cover: "/static/should-i-switch-to-zeit-now.png"

---
# Netlify

I have happily had my personal site [waylonwalker.com](https://waylonwalker.com) hosted on netlify for nearly 2 years now.  In fact I have hosted about a dozen different toy projects to play with on there, 4 of which have gone far enough to get a custom domain name.  They are fast to deploy and consistently do so on every `git push` to main.


## Zeit

I have recently started playing with zeit again.  I really like their cli tool, its dead simple and makes sense.  I tried the netlify one early on and dont think I really gave it much of a chance. I was able to backup a site we were modifying by saving everything locally (literally control+s) and running `now` in the command line.

While I was on the site I realized that when switching to gatsby v2 I had deployed it to now.sh while testing, before cutting over to the updated one on netlify.  It has been building every version since without issue!

> It has been building every version since without issue!

## What I am using

* gatsby
* forestry.io

I am using gatsby to build my site, and I do use forestry.io as a cms to be able to edit/manage posts online.  I think forestry is part of my problem in that it has added extra builds.  Every time I upload an image or save a post, even a draft, it pushes to production.


## Why Switch

This is just a side hobby for me.  I do not make any $$ off of it, and I do not want to pay for anything I do not have to.  As I am stepping up my blogging I have already hit 50% of my build quota only 1 week into the month on netlify.  I really like what netlify is doing for the JAMstack community, but I would rather build everything locally and push to GHPages for this project than have to pay for it.

## What Are your suggestions

Do you use Zeit?

Where do you host your gatsby.js site?
