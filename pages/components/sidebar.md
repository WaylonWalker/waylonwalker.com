---
title: Sidebar
slug: components/sidebar
published: false
jinja: true
description: "Homepage sidebar content -- included by home.html via include_post."

---

## Slash Pages

{{ render_slashes() }}

## Latest [Thoughts](/thoughts/)

{{ render_feed("thoughts-feed", 5, "card") }}

[See all thoughts &rarr;](/thoughts/){.home-see-more}

## Recent [Pings](/pings/)

{{ render_feed("pings", 5, "card") }}

[See all pings &rarr;](/pings/){.home-see-more}
