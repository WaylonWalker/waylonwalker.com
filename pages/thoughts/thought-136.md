---
title: '💭 Twitter Requires full image_urls'
date: 2023-10-17T17:30:09
template: link
link: None
tags:
  - webdev
  - meta
  - twitter
  - thoughts
  - thought
  - link
published: true

---

![[None]]

Yet again twitter cards were causing me pain.  This time it was me not realizing that they require full urls, and not relative or abolute urls.

> This was not working

``` html
    <meta name="twitter:image" content="/shot/?path={{ request.url|quote_plus }}" content-type='image/png'/>
```

> This does work with a full url

``` html
    <meta name="twitter:image" content="https://thoughts.waylonwalker.com/shot/?path={{ request.url|quote_plus }}" content-type='image/png'/>
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
