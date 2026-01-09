---
date: 2026-01-09 08:19:29
templateKey: blog-post
title: Og-Sample
tags:
  - python
published: True

---

I'm making an effort to make my og images better yet again, I'm going for that
next 10% better.  I really like my og images, but there are some title sizes
that overflow.  This page is a page to help debug.  How I make these og images
is for another day.

## Script

I use my own static site generator [[markata]].  I can use it to generate a
list of posts wrapped in their og image.  I use itertools to do a groupby so
that I can do roughly every 5 characters larger, and see a wide variety of
sizes.

``` python
from markata import Markata
from itertools import groupby

markata = Markata()
lens = [{'length': len(post.title), 'title': post.title, 'slug': post.slug} for post in m.posts]
lens_sorted = sorted(lens, key=lambda x: x["length"])

groups = {
    k: list(g)
    for k, g in groupby(lens_sorted, key=lambda x: (x["length"] // 5) * 5)
}

posts = [g[0] for g in groups.values()]
ogs = [ f'[![{post["title"]}](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/{ post["slug"] }/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/{ post["slug"] }/og/)' for post in posts]
print("\n\n".join(ogs))

```

## OG-Sample

[![sample](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/sample/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/sample/og/)

[![Kedro](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/kedro/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/kedro/og/)

[![Weeknote 0](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/weeknote-0/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/weeknote-0/og/)

[![Upcoming Stream](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/upcoming-streams/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/upcoming-streams/og/)

[![Codeit Bro Interview](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/codeit-bro-interview/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/codeit-bro-interview/og/)

[![⭐ Doomlab7 homelab-argocd](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/doomlab7-homelab-argocd/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/doomlab7-homelab-argocd/og/)

[![⭐ heathdbrown python_code_tips](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/heathdbrown-python-code-tips/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/heathdbrown-python-code-tips/og/)

[![Making good documentation in python](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/making-good-documentation-in-python/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/making-good-documentation-in-python/og/)

[![What DataScientists Should Know About S3](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/s3-datascience/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/s3-datascience/og/)

[![⭐ nvim-treesitter nvim-treesitter-textobjects](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/nvim-treesitter-nvim-treesitter-textobjects/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/nvim-treesitter-nvim-treesitter-textobjects/og/)

[![⭐ dataengineerone kedro-streaming-twitter-pipeline](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/dataengineerone-kedro-streaming-twitter-pipeline/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/dataengineerone-kedro-streaming-twitter-pipeline/og/)

[![How I Quickly Capture Screenshots directly into My Blog](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/screenshot-to-blog/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/screenshot-to-blog/og/)

[![Looking for a Heroku replacement, What I found was shocking!](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/looking-for-a-heroku-replacement/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/looking-for-a-heroku-replacement/og/)

[![💭 My Bed Doesn't Work Because of AWS Outage? TheStandup - YouTube](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/thoughts-853/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/thoughts-853/og/)

[![Dont Starve Together Session One - Getting Into It With A Clockwork Bishop](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/dont-starve-together-session-one---getting-into-it-with-a-clockwork-bishop/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/dont-starve-together-session-one---getting-into-it-with-a-clockwork-bishop/og/)

## shots

I also do [[ shots ]] posts that change the og template quite a bit by adding
the image to the page.  I'll do the same script, but add a filter to the
images.

``` python
from markata import Markata
from itertools import groupby

markata = Markata()
lens = [{'length': len(post.title), 'title': post.title, 'slug': post.slug} for post in m.filter('templateKey=="shots" and "family" not in tags')]
lens_sorted = sorted(lens, key=lambda x: x["length"])

groups = {
    k: list(g)
    for k, g in groupby(lens_sorted, key=lambda x: (x["length"] // 5) * 5)
}

posts = [g[0] for g in groups.values()]
ogs = [ f'[![{post["title"]}](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/{ post["slug"] }/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/{ post["slug"] }/og/)' for post in posts]
print("\n\n".join(ogs))
```

[![Funk Track 1](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/funk-track-1/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/funk-track-1/og/)

[![Hornet On A Bench](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/hornet-on-a-bench/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/hornet-on-a-bench/og/)

[![Apple Boxes Complete](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/apple-boxes-complete/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/apple-boxes-complete/og/)

[![Bambu Poop Flinger Jammed](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/bambu-poop-flinger-jammed/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/bambu-poop-flinger-jammed/og/)

[![First Fingerboard In The Press](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/first-fingerboard-in-the-press/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/first-fingerboard-in-the-press/og/)

[![Wyatt Drew A Watertower In Aesprite](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/wyatt-drew-a-watertower-in-aesprite/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/wyatt-drew-a-watertower-in-aesprite/og/)

[![Design For Bosch Colt Dust Collection V1](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/design-for-bosch-colt-dust-collection-v1/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/design-for-bosch-colt-dust-collection-v1/og/)

[![Dont Starve Together Session One - Nooo Luuucy](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/dont-starve-together-session-one---nooo-luuucy/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/dont-starve-together-session-one---nooo-luuucy/og/)

[![Dont Starve Together Session One - Setting Up Base](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/dont-starve-together-session-one---setting-up-base/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/dont-starve-together-session-one---setting-up-base/og/)

[![Dont Starve Together Session One - Opening Up The Garden](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/dont-starve-together-session-one---opening-up-the-garden/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/dont-starve-together-session-one---opening-up-the-garden/og/)

[![Dont Starve Together Session One - First Encounter With A Tall Bird](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/first-encounter-with-a-tall-bird/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/first-encounter-with-a-tall-bird/og/)

[![Dont Starve Together Session One - Getting Into It With A Clockwork Bishop](https://shots.waylonwalker.com/shot/?url=https://dev.waylonwalker.com/shots/dont-starve-together-session-one---getting-into-it-with-a-clockwork-bishop/og/&height=600&width=1200&scaled_width=1200&scaled_height=600&format=jpg&v=2)](https://dev.waylonwalker.com/shots/dont-starve-together-session-one---getting-into-it-with-a-clockwork-bishop/og/)

