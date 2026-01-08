---
date: 2025-02-02 14:35:02
templateKey: til
title: tailwind aspect
published: true
tags:
  - webdev
  - tailwindcss

---

I've been back to putting some images on my blog lately and thinking about
making them a bit thinner through the use of aspect ratio for simplicity.  I'm
leaning pretty heavy on tailwindcss these days due to some weird quirks of
markdown-it-attrs I cannot have slashes in classes from markdown so I made a
`.cinematic` class to achieve this.

``` css
.cinematic {
  @apply aspect-[2.39/1];
}
```

Example

![screenshot-2025-01-31T14-50-00-094Z.png](https://dropper.waylonwalker.com/api/file/50cfa8dc-9d46-4f02-877b-688fa5510a83.png){.cinematic}
