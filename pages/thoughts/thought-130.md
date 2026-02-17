---
title: '💭 How To Create a Custom Scrollbar'
date: 2023-10-11T19:11:49
templateKey: link
link: https://www.w3schools.com/howto/howto_css_custom_scrollbar.asp
tags:
  - webdev
  - css
published: true

---

> Default scrollbars on a dark theme website are just the ugliest thing.  This page covers all the pseudo selectors needed to style the scrollbar.

``` css
/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #888;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
```

[Original thought](https://www.w3schools.com/howto/howto_css_custom_scrollbar.asp)
