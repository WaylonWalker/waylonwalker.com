---
title: '💭 cURL Command Without Using Cache | Baeldung on Linux'
date: 2023-08-21T13:39:41
template: link
link: https://www.baeldung.com/linux/curl-without-cache#adding-the-pragma-http-header
tags:
  - curl
  - cli
  - thoughts
  - thought
  - link
published: true

---

![[https://www.baeldung.com/linux/curl-without-cache#adding-the-pragma-http-header]]

Busting cache with curl.  I'm not sure how much gets cached by curl, but I have ran into several cases where I am looking for new content and I want to ensure the content is new and no chance of being cached.

This article suggests 3 different techniques.

``` bash
curl -H 'Cache-Control: no-cache, no-store' http://www.example.com
curl -H 'Pragma: no-cache' http://www.example.com
curl http://www.example.com/?xyzzyspoon
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
