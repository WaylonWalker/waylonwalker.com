---
title: '💭 jq Cheat Sheet'
date: 2023-07-28T14:59:37
template: link
link: https://lzone.de/cheat-sheet/jq
tags:
  - jq
  - ijq
  - json
  - thoughts
  - thought
  - link
published: true

---

![[https://lzone.de/cheat-sheet/jq]]

A nice cheat sheet for jq. jq looks so nice, but it so quickly gets overwhelming on how to select what you want.  I was able to make a jq contains query.

``` bash
curl  https://thoughts.waylonwalker.com/posts/ | jq '.[] | select(.title | contains("python"))'
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
