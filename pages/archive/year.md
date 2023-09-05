---
date: 2022-08-24 20:06:34
templateKey: til
title: Highlighting text ranges with Rich | python
published: false
tags:
  - python
config_overrides:
  head:
    text:
      - value: |
          <style>
          h2 { position: sticky; top: 0; }
          </style>
---

{% for year in markata.map("date.year", filter='published')|unique %}

## {{ year }}

{% for post in markata.map('post', filter="published and date.year == "+year|string, sort='date') %}

- [{{ post.title }} - {{ post.date.month }}/{{ post.date.day }}](/{{ post.slug }})
  {% endfor %}
  {% endfor %}
