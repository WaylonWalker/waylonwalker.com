---
title: '💭 Email Address Obfuscation · Cloudflare Web Application Firewal...'
date: 2024-07-04T15:18:11
template: link
link: https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/
tags:
  - blogging
  - thoughts
  - thought
  - link
published: true

---

![[https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/]]

I recently started seeing email-decode.min.js show up on my blog posts, and I wondered what the heck ?  I didn't put it there.  Turns out that cloudflare put it there from pages to safely serve email addresses for me.

inspecting the page without js running we can see that the mailto email is swapped out for _email protected_.  Neat feature.

``` bash
❯ curl --silent https://waylonwalker.com/diskcache-as-debounce/ | grep email
<a class="decoration-pink-500 hover:decoration-pink-300 hover:text-pink-100" href="/cdn-cgi/l/email-protection#a4ccc1c8c8cbe4d3c5ddc8cbcad3c5c8cfc1d68ac7cbc9" rel="me"><span class="__cf_email__" data-cfemail="630b060f0f0c2314021a0f0c0d14020f0806114d000c0e">[email&#160;protected]</span></a>
<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script></body>
```

Looking deeper into this article it looks like this feature comes from Scrape Shield and enabling Email Address Obfuscation.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
