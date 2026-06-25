---
date: 2025-01-03 10:49:47
templateKey: blog-post
title: /start
tags:
  - meta
  - slash
published: True
jinja: True

---

Welcome to waylonwalker.com, my small corner of the internet.  I currently have
{{ posts | length }} posts published,
here are some links to help you get started around here.

![305cfd06-db8a-412d-9a21-57c280e6137c.webp](https://dropper.wayl.one/file/305cfd06-db8a-412d-9a21-57c280e6137c.webp)

## Feeds

I have quite a few different feeds that you can browse or subscribe to in your
rss reader, you can find them on my [[ feeds ]] page.

## Slash posts

[Slash pages](https://slashpages.net/) are some evergreen pages that I will do my best to keep up to date,
they are typically not targeted to a specific moment in time, but designed to
be ever living.

{% for post in posts %}{% if "slash" in post.tags %}* [[ {{ post.slug }} ]] - {{ post.description }}
{% endif %}{% endfor %}
