---
title: '💭 florimondmanca/arel: Lightweight browser hot reload for Python...'
date: 2023-10-08T15:22:23
template: link
link: https://github.com/florimondmanca/arel
tags:
  - webdev
  - fastapi
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/florimondmanca/arel]]

arel is a "Lightweight browser hot reload for Python ASGI web apps"

I just implemented this on my thoughts website using fastapi, and it's incredibly fast and lightweight.  There just two lines of js that make a web socket connection back to the backend that watches for changes.


When in development mode, this snippet gets injected directly on the page and does a refresh when arel detects a change.

``` js
const ws = new WebSocket("ws://localhost:5000/hot-reload");
ws.onmessage = () => window.location.reload();
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
