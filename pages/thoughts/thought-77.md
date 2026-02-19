---
title: '💭 How to Use HTML to Open a Link in a New Tab'
date: 2023-08-09T13:44:01
template: link
link: https://www.freecodecamp.org/news/how-to-use-html-to-open-link-in-new-tab/
tags:
  - html
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://www.freecodecamp.org/news/how-to-use-html-to-open-link-in-new-tab/]]

Most of the time when creating links in html you want to maintain the default behavior, as this is what users are going to expect, but sometimes your site behaves such that it does not fit, and it does something unexpected anyways.  in this case you might want to make the default behavior to open the link in a new tab rather than relying on users to control click.

Use this with restraint as this can make your site feel janky and do things that do not feel natural to the web.

``` html
<p>Check out <a href="https://www.freecodecamp.org/" target="_blank" rel="noopener noreferrer">freeCodeCamp</a>.</p>
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
