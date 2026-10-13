---
date: 2025-01-03 10:49:47
templateKey: blog-post
title: /start
tags:
  - meta
  - slash
published: True
jinja: True
authors:
- waylon
- id: gpt-6.1-sol
  role: copy editor
editorial_history:
- schema_version: 1
  event_id: 9c60e8f3-c1f2-45fc-bcd9-412e86863e44:pages/blog/start.md
  author: gpt-6.1-sol
  role: copy-editor
  action: edited
  recorded_by: gpt-6.1-sol
  recorded_at: '2026-10-13T23:37:34.182278+00:00'
  base_commit: c17ef1c17f376ab8834a2053ce94c3c23b3b9563
  commit: 725f802db43dc81fa579d53c3a152eba9062853d
  path: pages/blog/start.md
  content_digest: sha256:eb7d2bf52e357169661da63ebc9cb0c52b124725888fab5c632eaeb1a3bb653e
  digest_version: editorial-v1
  file_url: https://github.com/waylonwalker/waylonwalker.com/blob/725f802db43dc81fa579d53c3a152eba9062853d/pages/blog/start.md
  diff_url: https://github.com/waylonwalker/waylonwalker.com/commit/725f802db43dc81fa579d53c3a152eba9062853d#diff-a7bb7c53ecd10407efe38a6385a9f5f3dd22a14517fd4d2a2c278d2472706189
  summary: Fixed slash page links on /start/ so generated descriptions render as
    readable text.
---

Welcome to waylonwalker.com, my small corner of the internet.  I currently have
{{ posts | length }} posts published,
here are some links to help you get started around here.

![305cfd06-db8a-412d-9a21-57c280e6137c.webp](https://dropper.waylonwalker.com/file/305cfd06-db8a-412d-9a21-57c280e6137c.webp)

## Feeds

I have quite a few different feeds that you can browse or subscribe to in your
rss reader, you can find them on my [[ feeds ]] page. #meta

## Slash posts

[Slash pages](https://slashpages.net/) are some evergreen pages that I will do my best to keep up to date,
they are typically not targeted to a specific moment in time, but designed to
be ever living.

{% for post in posts %}{% if "slash" in post.tags %}* [{{ post.title }}](/{{ post.slug }}/) - {{ post.description | striptags }}
{% endif %}{% endfor %}
