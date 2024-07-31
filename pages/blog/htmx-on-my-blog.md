---
date: 2024-06-15 20:50:12
templateKey: blog-post
title: I've added htmx to my blog
tags:
  - webdev
  - markata
published: false
jinja: true
---

I've added htmx to my blog.  It's extra bloatware that I long avoided, but it's
so damn convenient.

Ok so it's not bloatware, but it's not the theme I was going for.  I wanted my
site to be as lightweight as possible.  I had at one point gone too far and had
Mb's of react that did not provide any value for the end user.

<div hx-get='/recent-thoughts/partial' hx-trigger='load'></div>

<div hx-get='/recently-written/partial' hx-trigger='load'></div>

## can it be done with jinja

<div>
{% with feed = markata.feeds.recent_thoughts %}
{% include 'feed_sm_partial.html' %}
{% endwith %}
</div>

## Feed Partials

[[ markata ]] pre-release 0.8.1.dev10 has been released with support for feed
partials on [pypi](https://pypi.org/project/markata/0.8.1.dev10/).

## It's now part of my blog

Commit
[aa233](https://github.com/WaylonWalker/waylonwalker.com/commit/aa23361e8606b62f7e4ca1a9305e6975fcdbc088)
added support for recent posts on each page to be loaded off of this partial.
