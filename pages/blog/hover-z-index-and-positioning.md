---
date: 2025-01-23 15:54:07
templateKey: blog-post
title: hover z-index and positioning
tags:
  - webdev
  - tailwindcss
published: True

---

I broke my [[ sick-wikilink-hover ]] recently in a refactor, today I did some
diving in to figure out what happened.

## Before

As you can see in the screenshot below, the link is in a list of links, and
when the hover image pops up it sits behind all of the other text.  The z-index
of the list-item is supposed to be raised above the others on hover.

![image](https://dropper.wayl.one/api/file/b3158b49-5c0f-4e52-b3e3-47ba67f5c801.webp)

Manually setting z-index to 20 in the inspector I noticed this message from
devtools, _"The position: static property prevents z-index from having an
effect. Try setting position to something other than static."_, looking back at
some of my refactoring I had relative in an old template and it was lost.

![image](https://dropper.wayl.one/api/file/1c7fb24c-b77d-4962-adfc-8e2eb5e6145c.webp)

## After

After properly setting position to relative on the list-item, the hover image
is raised above the others.

![image](https://dropper.wayl.one/api/file/ef207afb-a3a5-463a-a615-fdfe8a4256c5.webp)
