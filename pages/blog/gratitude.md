---
date: 2017-12-13
templateKey: blog-post
title: gratitude
tags:
  - gratitude
  - slash
published: True
jinja: True
description: I try to gratitude journal for 5 minutes each day, listing at least one thing I am grateful for.

---

{% for post in markata.feeds.gratitude_feed.config.description %}

{% for post in markata.feeds.gratitude_feed.posts %}

{.mb-0 .text-base}

## {{ post.title.replace("Gratitude ", "") }}

_{{ post.date }}_

{{ post.content }}
{% endfor %}
