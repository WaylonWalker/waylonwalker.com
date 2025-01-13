---
date: 2025-01-02 10:21:23
templateKey: blog-post
title: colophon
tags:
  - blog
  - meta
  - webdev
  - slash
published: True
jinja: True

---

> [Colophon](https://indieweb.org/colophon) a page that describes how the site is made, with what tools, supporting what technologies

## Author

![Waylon Walker's Profile Picture](https://images.waylonwalker.com/profile.webp)

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
* cloudflare pages

see more about these components in [[ about-this-site ]]

## meta

Some evergreen pages that are more about me or this site from the [[ meta ]] feed.

{% for post in markata.feeds.meta.posts %}* [[ {{post.slug}} ]] - {{post.description}}
{% endfor %}
