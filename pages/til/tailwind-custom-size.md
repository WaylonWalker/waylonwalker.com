---
date: 2024-04-12 21:21:42
templateKey: til
title: tailwind arbitrary values
published: true
tags:
  - webdev

---

I learned not to fear the arbitrary size feature of tailwind.  While building
out [reader.waylonwalker.com](https://reader.waylonwalker.com) I kept getting
content flowing off the screen, and struggling to keep it on the screen.  I
really felt that I should be able to do this with vanilla tailwind, but after
some encouragement from Twitter I decided to lean on arbitrary values and it
worked.

Don't fear the arbitrary values.

``` html
<li class="max-w-[100vw]">
</li>
```

Learn more about using-arbitrary-values from their docs
[docs](https://tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values)
