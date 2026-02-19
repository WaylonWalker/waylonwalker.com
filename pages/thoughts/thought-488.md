---
title: '💭 Why Your Backend Shouldn''t Serve Files - YouTube'
date: 2024-12-31T16:24:28
template: link
link: https://www.youtube.com/watch?v=aybSXT9ZJ8w
tags:
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://www.youtube.com/watch?v=aybSXT9ZJ8w]]

Lane from boot.dev madde this fantastic video about serving files on the internet.  It has me wondering if I need to rethink a few of my things that I have built.  I have a few things I am serving media from, but I have very aggressive cloudflare cache rules on them, so each file should only be uploaded about once per year.

My problem going straight out of minio right now is how do i set headers for cache control on it.  If I can't set the cache control and everything is coming out of minio this does not solve my problems.

---

I went back and played with presigned urls and you can in fact control and set response headers, this is definitely the way and I have been wrong.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
