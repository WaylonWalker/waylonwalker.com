---
title: '💭 page-break-after - CSS: Cascading Style Sheets | MDN'
date: 2023-11-30T02:38:49
templateKey: link
link: https://developer.mozilla.org/en-US/docs/Web/CSS/page-break-after
tags:
  - webdev
  - css
published: true

---

> I'm working on something that might go to print, so I want the page breaks to happen somewhat in my control as the content author.  As I do my writing I break my content up in to many short sections using h2, sometimes an h3.  These are generally short sections that go together, should stay together, and typically are not too lengthy to cause a large white space in print.

I found a way in css to only allow page breaks to happen on h2 and h3, and it turned out perfect, suck it WSIWIG editors


``` css
* {
  page-break-before: avoid;
}

h2,
h3 {
  page-break-before: auto;
}
```

[Original thought](https://developer.mozilla.org/en-US/docs/Web/CSS/page-break-after)
