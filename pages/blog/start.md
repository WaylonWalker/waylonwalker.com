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

<!-- markata feeds need counts -->
{% set title_count = 0 %}
{% for post in markata.feeds.archive.posts %}
    {% if post.title is not none %}
        {% set title_count = title_count + 1 %}
    {% endif %}
{% endfor %}
{{ title_count }}

Welcome to waylonwalker.com, my small corner of the internet.  I currently have
{{ title_count }} posts published, here are some links to
help you get started around here.

## Feeds

I have quite a few different feeds that you can browse or subscribe to in your rss reader, you can find them on my [[ feeds ]] page.

## Slash posts

[[ slashes ]]

[Slash pages](https://slashpages.net/){.hoverlink} are some evergreen pages that I will do my best to keep up to date,
they are typically not targeted to a specific moment in time, but designed to
be ever living.

{{ '\n'.join(markata.feeds.slashes.map('f"* [[ {slug} ]] - {description}"', sort='slug')) }}
