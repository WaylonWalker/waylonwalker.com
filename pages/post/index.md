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

---

<div class="home-shots-section">

## Latest [Shots](/shots/)

{{ render_feed("shots", 12, "card") }}

[See all shots &rarr;](/shots/){.home-see-more}

</div>

<div class="home-main-rail">
<div class="home-main-content">

## Latest [Blog Posts](/blog/)

{{ render_feed("blog-feed", 5, "card") }}

[See all blog posts &rarr;](/blog/){.home-see-more}

## Recent [TIL](/til/)

{{ render_feed("til-feed", 5, "card") }}

[See all TIL posts &rarr;](/til/){.home-see-more}

</div>
<aside class="home-sidebar">

<div class="home-sidebar-section">

## Slash Pages

<div class="home-slashes">
<a href="/now/" class="home-slash-link">/now</a>
<a href="/about/" class="home-slash-link">/about</a>
<a href="/colophon/" class="home-slash-link">/colophon</a>
<a href="/ai/" class="home-slash-link">/ai</a>
<a href="/yep/" class="home-slash-link">/yep</a>
<a href="/nope/" class="home-slash-link">/nope</a>
<a href="/top4/" class="home-slash-link">/top4</a>
<a href="/verify/" class="home-slash-link">/verify</a>
<a href="/feeds/" class="home-slash-link">/feeds</a>
<a href="/analytics/" class="home-slash-link">/analytics</a>
</div>

</div>

<div class="home-sidebar-section">

## Latest [Thoughts](/thoughts/)

{{ render_feed("thoughts-feed", 5, "card") }}

[See all thoughts &rarr;](/thoughts/){.home-see-more}

</div>

<div class="home-sidebar-section">

## Recent [Pings](/pings/)

{{ render_feed("pings", 5, "card") }}

[See all pings &rarr;](/pings/){.home-see-more}

</div>

</aside>
</div>
