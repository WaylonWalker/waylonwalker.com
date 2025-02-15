---
date: 2025-02-15 09:28:48
templateKey: til
title: newlines in css before
published: true
tags:
  - webdev

---

I'm building in a [[ fragmentions ]] implementation into my blog, I wanted to
add some text before the fragment to indidate that it was the highlighted
fragment that someone may have intended to share with you.

To get a newline in a `:before` I need to use `\A` and `white-space: pre-line`.

``` css
body :target::before,
body [fragmention]::before {
    content: "Highlighted Fragment:\A";
    white-space: pre-line;
    @apply font-bold text-yellow-600;
}
```

Here is what it looks like on my not yet live implementation of fragmentions.

![screenshot-2025-02-15T15-43-06-372Z.png](/api/file/fb693b92-3744-45a5-9220-bd914162f435.png)
