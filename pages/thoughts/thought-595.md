---
title: '💭 Build UIs that don''t suck - YouTube'
date: 2025-04-15T13:50:53
templateKey: link
link: https://www.youtube.com/watch?v=-h9rH539x1k
tags:
  - tailwindcss
  - webdev
  - css
published: true

---

> How to make an entire clickable without presenting the entire content of the card as the link title.  These videos are great, I've ran into these types of problems so many times, and definitely did not know about things like isolate to keep the z-index scoped to one element.

* isolate - scope z-index inside this element so that it does not leak out.
* [.relative [.absolute, inset-0, z-10]] - the inset zero is a modern shorthand for zeroing all sides, top-0, right-0, bottom-0, left-0.

[Original thought](https://www.youtube.com/watch?v=-h9rH539x1k)
