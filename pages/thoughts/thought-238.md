---
title: '💭 google chrome - Webkit scrollbar CSS, always a white box in co...'
date: 2024-04-09T16:55:55
template: link
link: https://stackoverflow.com/questions/35968553/webkit-scrollbar-css-always-a-white-box-in-corner
tags:
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://stackoverflow.com/questions/35968553/webkit-scrollbar-css-always-a-white-box-in-corner]]

This is how you fix the stupid corner section of a double scroll bar being white on a dark theme site.


``` css
::-webkit-scrollbar-corner {
  background: rgba(0,0,0,0);
}
```

The question included an example image where you can see white squares everywhere there are horizontal and vertical scroll bars.

![the corner](https://i.stack.imgur.com/P6b7f.png)

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
