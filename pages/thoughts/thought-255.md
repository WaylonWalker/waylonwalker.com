---
title: '💭 </> htmx ~ The response-targets Extension'
date: 2024-04-30T18:00:54
templateKey: link
link: https://htmx.org/extensions/response-targets/
tags:
  - htmx
  - webdev
published: true

---

> The htmx response-targets extension allows me to respond to errors from the backend and do normal htmx swaps.

> !!! note
    by default htmx will only swap on 200 and 300 responses

Load the extension in head

``` html
<script src="https://unpkg.com/htmx.org@1.9.12/dist/ext/response-targets.js"></script>
```

Use  the extension on an endpoint that might return a 400.


``` html
<div hx-ext="response-targets">
    <div id="response-div"></div>
    <button hx-post="/register"
            hx-target="#response-div"
            hx-target-5*="#serious-errors"
            hx-target-404="#not-found">
        Register!
    </button>
    <div id="serious-errors"></div>
    <div id="not-found"></div>
</div>
```

[Original thought](https://htmx.org/extensions/response-targets/)
