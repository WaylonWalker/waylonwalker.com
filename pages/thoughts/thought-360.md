---
title: '💭 add quick-tap-ms and require-prior-idle-ms · WaylonWalker/zmk-...'
date: 2024-07-25T13:40:14
template: link
link: https://github.com/WaylonWalker/zmk-config-42block/commit/cb2cda4cf7b3776995dbc2e8608b60670a2cf8b2
tags:
  - keyboard
  - zmk
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/WaylonWalker/zmk-config-42block/commit/cb2cda4cf7b3776995dbc2e8608b60670a2cf8b2]]

Even after switching to my hm and ht behaviors I am running into some issues where sometimes I am still accidentally hitting mods(&hm) and layers(&ht) while typing and it's been getting frustrating.  My main issue has been on &ht, they are configured the same so I suspect that my pinkies just move a bit slower over the keys than my pointer/middle finger.

I just added `quick-tap-ms` and `require-prior-idle-ms` to my &hm and &ht behaviors, and a few intentionally sloppy passes through monkeytype seem to show that its working well.  A few days of trying this will tell whether it was a good fix or if I have maybe gone too far the other way.

The end goal here is to be able to roll over keys faster without worrying about hitting other layers or mods.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
