---
title: '💭 How to configure base url for all requests using HTMX? - Stack...'
date: 2024-12-30T16:25:49
templateKey: link
link: https://stackoverflow.com/questions/69456875/how-to-configure-base-url-for-all-requests-using-htmx
tags:
  - webdev
  - htmx
published: true

---

> Today I learned how to configure the baseurl for htmx using the <base> tag.  This is pretty handy to be able to configure different baseurls.

``` html
  <base href="<scheme>://<netloc>/api/v1/">
  <button hx-post="clicked"
       hx-trigger="click"
       hx-target="#parent-div"
       hx-swap="outerHTML">
    Click Me!
  </button>
```

[Original thought](https://stackoverflow.com/questions/69456875/how-to-configure-base-url-for-all-requests-using-htmx)
