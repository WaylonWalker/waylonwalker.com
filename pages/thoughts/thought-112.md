---
title: '💭 Pagefind | Pagefind — Static low-bandwidth search at scale'
date: 2023-09-20T01:04:41
template: link
link: https://pagefind.app/
tags:
  - webdev
  - search
  - wasm
  - thoughts
  - thought
  - link
published: true

---

![[https://pagefind.app/]]

Pagefind is absolutely insane.  I've tried a number of static site searches, and found them all hard to get get going, clunky and not the best experience as a user or developer.

I setup pagefind in about 2 minutes on my site where it found and indexed 833 pages in 2 minutes.

The only downside I see so far is that it is a lot of bandwidth to the user.  On simulated slow 3G you can definitly feel it, but not terrible.  Anything slower and its going to start feeling frustrating.

> edit: I have actually fully deployed it on waylonwalker.com, and its fast!

create the index

``` bash
npx -y pagefind --site public --serve
```

Then I put this on a page, it looks really nice on a white background, but would need some work to drop into a dark theme.

``` html
<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<script src="/pagefind/pagefind-ui.js"></script>
<div id="search"></div>
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        new PagefindUI({ element: "#search", showSubResults: true });
    });
</script>
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
