---
title: 'Render-blocking on purpose'
date: 2024-07-11T17:55:28Z
template: link
link: https://fullystacked.net/render-blocking-on-purpose/
tags:
  - html
  - webdev
  - thought
published: true

---

![[https://fullystacked.net/render-blocking-on-purpose/]]

You can explicitly make a script render blocking, nothing will be rendered until this js is ready.


``` html
<script blocking="render" 
        src="important.js" 
        defer></script>
```
