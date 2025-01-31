---
date: 2025-01-03 10:49:47
templateKey: blog-post
title: start
tags:
  - meta
  - slash
published: True
jinja: True

---

Welcome to waylonwalker.com, my small corner of the internet.  I currently have
{{ markata.feeds.archive.posts | length }} posts published,
here are some links to help you get started around here.

![2fcdafc0-f152-4fa9-ac91-799acd9084d3-239-1.webp](https://dropper.wayl.one/api/file/1896de8d-abd9-4652-95df-b41dc7eaf48b.webp)

## Feeds

I have quite a few different feeds that you can browse or subscribe to in your
rss reader, you can find them on my [[ feeds ]] page.

## Slash posts

[[ slashes ]]

[Slash pages](https://slashpages.net/){.hoverlink} are some evergreen pages that I will do my best to keep up to date,
they are typically not targeted to a specific moment in time, but designed to
be ever living.

{{ '\n'.join(markata.feeds.slashes.map('f"* [[ {post.slug} ]] - {post.description}"', sort='slug')) }}
