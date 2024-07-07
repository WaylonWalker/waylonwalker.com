---
date: 2024-07-07 10:24:28
templateKey: blog-post
title: reader
tags:
  - catalytic
published: False

---

In 2024 I built my own reader after years of being bitter about google killing
reader more than a decade prior.

!!! seealso
  All the way back in 2020 I made a post on what I wanted to build into my own
  reader.  It went long forgotten until I tried to make this post and slugs
  clashed. [[ reader-2020 ]]

## Built on markata

I built it on top of my own static site generator [[ markata ]], feedparser ([[
parsing-rss-python ]]), some jinja templating, and tailwind.

After putting all the work I have into markata, it makes projects like this
fairly easy to build out with just a custom loader to load new posts in.
