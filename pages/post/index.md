---
date: 2026-02-28
templateKey: blog-post
title: index
slug: ""
published: True
jinja: True
aliases:
  - home
  - index

---

A curated view of my freshest blog posts, shots, pings, and thoughts, drawn
directly from the feeds that power this site.

## Last 5 Blog posts

{{ render_feed("blog-feed", 5, "card") }}

## Last 5 [TIL](/til/) posts

{{ render_feed("til-feed", 5, "card") }}

## Last 5 [[shots]]

{{ render_feed("shots", 5, "card") }}

## Last 5 [[ping]]

{{ render_feed("pings", 5, "card") }}

## Last 5 [Thoughts](/thoughts/)

{{ render_feed("thoughts-feed", 5, "card") }}
