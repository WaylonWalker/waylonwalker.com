---
title: '💭 How I use Obsidian Templater'
date: 2024-12-22T17:12:50
template: link
link: https://thoughts.waylonwalker.com/post/455
tags:
  - meta
  - thoughts
  - shots
  - thoughts
  - thought
  - link
published: true

---

![[https://thoughts.waylonwalker.com/post/455]]

Ok, second post on this one.  I am sending only head requests, so I want to see the first request for the image, which happens in the chrome extension after pressing submit.  It will not yet come from cloudflare so I am interested in what it looks like just streaming out of object sorage.  This time I have the inspector open on the tab.

---

As expected I got a cloudflare cache miss on first hit.

![image](https://dropper.wayl.one/api/file/a9fdbb56-ce1b-42cd-9598-81c36eb758e2.webp)

But the overall performance of 351ms to get the image was not bad considering it takes several seconds to get the image fresh.

![image](https://dropper.wayl.one/api/file/fa623194-aa14-4fdb-a5ac-2a39beafbf1e.webp)

---

Now closing the chrome extension popup, and hitting the main thoughts page again gives me a cache hit from Cloudflare's CDN.

![image](https://dropper.wayl.one/api/file/861880a5-4f2d-47e7-b19f-f4e8eaa34139.webp)

And the total request time goes from 351ms to 21ms with the Cloudflare CDN, quite impressive!

![image](https://dropper.wayl.one/api/file/f8927bab-a63b-453f-aaad-d6af68f5e6c0.webp)

---

Sorry with how meta these last two posts were, I needed a second post to get that fresh request graph from.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
