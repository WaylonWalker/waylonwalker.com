---
date: 2025-05-25 21:01:04
templateKey: til
title: javascript b64
published: true
tags:
  - javascript

---

I'm currently [[replacing-google-search-apps-with-self-hosted-web-apps]] and
decided to create a simple b64 encoder/decoder, just start typing to enter
text, escape to deselect, then e/d to encode/decode.

I'm trying to make these apps super simple, self hosted out of minio, static
html, and javascript.  It's been fun to get back to some simple interactive web
development like this. No build just a website that does something.  No broken
builds, no containers to deploy, just push to minio.

``` javascript
encoded = btoa(content);
decoded = atob(encoded);
```

Here is the result.

[![screenshot of https://b64.wayl.one](http://shots.wayl.one/shot/?url=https://b64.wayl.one&height=450&width=800&scaled_width=800&scaled_height=450&selectors=)](https://b64.wayl.one)
