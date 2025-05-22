---
date: 2025-05-22 14:02:28
templateKey: blog-post
title: gratitude
tags:
  - gratitude
published: True
jinja: True

---

{% for post in markata.feeds.gratitude_feed.posts %}

{.mb-0 .text-base}

## {{ post.title.replace("Gratitude ", "") }}

_{{ post.date }}_

{{ post.content }}
{% endfor %}
