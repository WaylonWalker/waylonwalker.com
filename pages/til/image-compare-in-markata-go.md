---
date: 2026-05-01 07:40:44
templateKey: til
title: image compare in markata go
published: true
tags:
  - webdev

---

`markata-go` now has web awesome integration for image compare.  It renders a
nice web component with a slider to compare two images.

::: wa-comparison
![d628ffba-de18-4fff-91a8-700f037df119.webp](https://dropper.wayl.one/file/d628ffba-de18-4fff-91a8-700f037df119.webp)
![](https://dropper.waylonwalker.com/file/ca30665f-1a15-453e-aab8-221901c7df99.webp)
:::

It's done with a class wrapper around the image components.

``` md
::: wa-comparison
![d628ffba-de18-4fff-91a8-700f037df119.webp](https://dropper.wayl.one/file/d628ffba-de18-4fff-91a8-700f037df119.webp)
![](https://dropper.waylonwalker.com/file/ca30665f-1a15-453e-aab8-221901c7df99.webp)
:::
```

Without `markata-go`'s web awesome integration, the above would look like:

``` html
<script type="module">
  import 'https://ka-f.webawesome.com/webawesome@3.6.0/components/comparison/comparison.js';
</script>

<wa-comparison>
  <img
    slot="before"
    src="https://dropper.wayl.one/file/d628ffba-de18-4fff-91a8-700f037df119.webp"
    alt="Grayscale version of kittens in a basket looking around."
  />
  <img
    slot="after"
    src="https://dropper.waylonwalker.com/file/ca30665f-1a15-453e-aab8-221901c7df99.webp"
    alt="Color version of kittens in a basket looking around."
  />
</wa-comparison>
```

