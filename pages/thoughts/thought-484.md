---
title: '💭 How to configure base url for all requests using HTMX? - Stack...'
date: 2024-12-30T16:25:49
template: link
link: https://stackoverflow.com/questions/69456875/how-to-configure-base-url-for-all-requests-using-htmx
tags:
  - webdev
  - htmx
  - thoughts
  - thought
  - link
published: true

---

![[https://stackoverflow.com/questions/69456875/how-to-configure-base-url-for-all-requests-using-htmx]]

Today I learned how to configure the baseurl for htmx using the <base> tag.  This is pretty handy to be able to configure different baseurls.

``` html
  <base href="<scheme>://<netloc>/api/v1/">
  <button hx-post="clicked"
       hx-trigger="click"
       hx-target="#parent-div"
       hx-swap="outerHTML">
    Click Me!
  </button>
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
