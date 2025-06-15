---
date: 2024-05-30 13:45:54
templateKey: blog-post
title: markata
tags:
  - python
  - markata
  - slash
published: true
jinja: true
---

This post is a work in progress.

Markata is the static site generator that I created to build my website [[
about-this-site ]].  I built it for me and I enjoy using it.  I know everying
it can do and I can extend it to do more easily.  I have set it up for some
friends to also use it and am proud that it helps them publish their content.

It's a meme to create your own static site generator to make your website.  Yes
its funny, I don't recommend it if your not ready for the level of work that
comes with it, but at the end of the day it's very rewarding and a great way to
learn.

## Static Sites were all the rage

**JAMStack was 🔥**

Gatsby and Next.js hit the scene as the next generation of static site builders
and were getting big around the time I started building my site in 2017.  They
were based on react.  I dove into react and learned it enough to build my
website, but I really lacked the depth of knowledge in the js ecosystem to
really work on it effectively.  For instance when it got slow, it was hard for
me to profile and find out why.  What I really wanted was my site written in
python, which I knew the ecosystem for very well, but I did not find the
existing site generators easy to extend to do the things I needed.  Naively I
thought it would be easier to just build my own than learn how to make one do
what I wanted it to.  Not invented here syndrome hitting hard.

!!! Note "In their Defense"
    I really lacked the depth of knowledge in the js ecosystem to really work on
    it (gatsby) effectively.

## Plugins all the way down

I started building this as I dove deeper into the [[ kedro ]] framework for Data
Engineering pipelines.  They use a plugin framework for allowing users to
extend it called pluggy.  I had a great experience extending kedro using pluggy
and wanted to build something with based on pluggy when I had started markata.

[[ pluggy-minimal-example ]]

## More Posts

I have more posts about markata in the [[markata-feed]].

{% for post in markata.feeds.markatafeed.map(reverse=True) %}

* [{{post.title}}](/{{post.slug}}) - {{post.date}}
{% endfor %}
