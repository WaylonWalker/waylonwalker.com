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
intro_cards:
  - slug: components/about-intro
    heading: About
    link: /about/
  - slug: components/now-intro
    heading: /now
    link: /now/

---

<div class="home-shots-section">

## Latest [Shots](/shots/)

{{ render_feed("shots", 9, "card") }}

[See all shots &rarr;](/shots/){.home-see-more}

</div>

## Latest [Blog Posts](/blog/)

{{ render_feed("blog-feed", 5, "card") }}

[See all blog posts &rarr;](/blog/){.home-see-more}

## Recent [TIL](/til/)

{{ render_feed("til-feed", 5, "card") }}

[See all TIL posts &rarr;](/til/){.home-see-more}
