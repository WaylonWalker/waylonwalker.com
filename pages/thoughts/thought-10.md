---
title: '💭 jq Cheat Sheet'
date: 2023-07-28T14:59:37
templateKey: link
link: https://lzone.de/cheat-sheet/jq
tags:
  - jq
  - ijq
  - json
published: true

---

> A nice cheat sheet for jq. jq looks so nice, but it so quickly gets overwhelming on how to select what you want.  I was able to make a jq contains query.

``` bash
curl  https://thoughts.waylonwalker.com/posts/ | jq '.[] | select(.title | contains("python"))'
```

[Original thought](https://lzone.de/cheat-sheet/jq)
