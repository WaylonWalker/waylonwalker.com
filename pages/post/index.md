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
hero_tagline: "Software engineer, pipeline builder, and maker of things on the web. Always learning, always shipping."
hero_avatar: /8bitcc.png
hero_links:
  - label: Blog
    url: /blog/
  - label: Shots
    url: /shots/
  - label: TIL
    url: /til/
  - label: About
    url: /about/
  - label: Now
    url: /now/
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

{{ render_feed("blog-feed", 5, "card") }}

[See all blog posts &rarr;](/blog/){.home-see-more}

</div>

<div class="home-feeds-grid__col">

## Recent [TIL](/til/)

{{ render_feed("til-feed", 8, "card") }}

[See all TIL posts &rarr;](/til/){.home-see-more}

</div>

</div>
