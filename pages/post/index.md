---
date: 2026-02-28
template: home.html
title: Waylon Walker
slug: ""
published: True
jinja: True
description: "Software, automation, and building things on the web."
aliases:
  - home
  - index
hero_first_name: Waylon
hero_last_name: Walker
hero_tagline: "Father of two, husband, blog engine from scratch, kubernetes in the basement."
hero_avatar: /8bitcc.png
hero_links:
  - label: Just F&*$ing use K8s
    url: /just-fucking-use-kubernetes/
  - label: we beat trailmakers
    url: /we-beat-trailmakers/
  - label: Hollow Knight Keeb Run
    url: /hollow-knight-home-row-layout/
  - label: Make Minio Access Key
    url: /make-minio-access-key/
intro_cards:
  - heading: About
    slug: components/about-intro
    link: /about/
  - heading: Now
    slug: components/now-intro
    link: /now/

---

<div class="home-shots-section">

## Latest [Shots](/shots/)

{{ render_feed("shots", 9, "card") }}

[See all shots &rarr;](/shots/){.home-see-more}

</div>

<div class="home-feeds-grid">

<div class="home-feeds-grid__col">

## Latest [Blog Posts](/blog/)

{{ render_feed("blog", 5, "card") }}

[See all blog posts &rarr;](/blog/){.home-see-more}

</div>

<div class="home-feeds-grid__col">

## Recent [TIL](/til/)

{{ render_feed("til-feed", 8, "card") }}

[See all TIL posts &rarr;](/til/){.home-see-more}

</div>

</div>
