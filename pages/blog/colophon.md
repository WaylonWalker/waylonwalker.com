---
date: 2025-01-02 10:21:23
templateKey: blog-post
title: /colophon
tags:
  - blog
  - meta
  - webdev
  - slash
published: True
jinja: True

---

> [Colophon](https://indieweb.org/colophon) a page that describes how the site
> is made, with what tools, supporting what technologies

## Author

![Waylon Walker's Profile Picture](https://dropper.waylonwalker.com/file/305cfd06-db8a-412d-9a21-57c280e6137c.webp)

All posts on this site are written by [Waylon
Walker](https://waylonwalker.com), the typical content has changed and evolved
over time.  I go back and make a few corrections, but for the most part things
stay pretty much as they were published originally.

see more in [[ about ]]

## tech

This site is a static site build with my own static site generator [[ markata
]], [[ thoughts ]] or as Simon Willison calls it a [link
blog](https://simonwillison.net/2024/Dec/22/link-blog/#atom-everything) posts
are pulled in as a regular posts, all is hosted on cloudflare pages.

* [[ markata ]]
* [[ thoughts ]]
* ~~GitHub Pages~, ~netlify~, ~cloudflare pages~, basement kubernetes.

see more about these components in [[ about-this-site ]]

## Basement Kubernetes

==Yes== I run kubernetes in my basement.  ==Yes== it is build on a hodge podge of trash and enough new parts to get it to work.  **No** this does not have 100% uptime, my house looses power, flaky deploys sometimes have brief outages.  

Tip of the at to low tech mag.  Leaning in on building cool things on the weird edges of the internet.  Not being so tied to 9 9s, infinite uptime, instant gratitude always on demand.

![embed](https://solar.lowtechmagazine.com/about/the-solar-website/)

This is part of the ==_charm_== now.  I know that its a common _trope_  something twitter likes to laugh at and poke fun at.  I'll wipe my tears away with my six figure job that I am able to do really well because I have a place to low risk do new tech on a platform that is very similar to what makes $$ in infrastructure.  I think I will be okay, and if I have an outtage, we will lean into that as the charm of a side project running on kubernetes in my basement that does not get quite the same level of attention as work I get paid to do and includes crazy new things I'm not yet willing to try in a real app with paying users.

Everything from the git repo, the site build, the production traffic all routes through hardware that I own and can touch, no one can turn off and stop.  I rely on one cloudflare tunnel to get it out to the public otherwise its all on me.

## Analytics

I ==do not== track users, I respect the privacy of my readers and do not track
their information.  I do track [[ analytics ]] on my own writing a post rate.
Its more of an interesting history of the site.

I try to take some time each year to review and highlight some of the highs and lows, some of the different trends on that [[ analytics ]] page.  Its a fun summary of year over year.

## meta

Some evergreen pages that are more about me or this site from the [[ meta ]] feed.

{% for post in markata.feeds.meta.posts %}* [[ {{post.slug}} ]] - {{post.description}}
{% endfor %}
