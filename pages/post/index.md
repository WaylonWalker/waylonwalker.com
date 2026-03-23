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

## Latest [Blog Posts](/blog/)

{{ render_feed("blog-feed", 3, "card") }}

<div class="home-split-feeds">
<div class="home-split-col">

## Recent [TIL](/til/)

{{ render_feed("til-feed", 3, "card") }}

</div>
<div class="home-split-col">

## Recent [Pings](/pings/)

{{ render_feed("pings", 3, "card") }}

</div>
</div>

<div class="home-shots-section">

## Latest [Shots](/shots/)

{{ render_feed("shots", 3, "card") }}

</div>

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

## Latest [Thoughts](/thoughts/)

{{ render_feed("thoughts-feed", 3, "card") }}
