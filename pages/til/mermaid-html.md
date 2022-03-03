---
date: 2022-03-03 14:40:01.862861
templateKey: til
title: Simple Plain Text Diagrams in HTML
tags:
  - webdev
  - webdev
  - webdev

---

Since GitHub started supporting mermaid in their markdown I wanted to
take another look at how to implement it on my site, I think it has some
very nice opportunities in teaching, documenting, and explaining things.

The docs kinda just jumped right into their mermaid language and really
went through that in a lot of depth, and skipped over how to implement
it yourself, turns out its pretty simple. You  just write mermaid syntax
in a div with a class of mermaid on it!

``` html
<script src='https://unpkg.com/mermaid@8.1.0/dist/mermaid.min.js'></script>
<div class='mermaid'>
graph TD;
a --> A
A --> B
B --> C
</div>
```

>  You  just write mermaid syntax in a div with a class of mermaid on
>  it!

The above gets me this diagram.

<script src='https://unpkg.com/mermaid@8.1.0/dist/mermaid.min.js'></script>
<div class='mermaid'>
graph TD;
a --> A
A --> B
B --> C
</div>

This feels so quick and easy to start getting some graphs up and running, but
does lead to layout shift and extra bytes down the pipe.  The best solution in
my opionion would be to forgo the js and ship svg.  That said, this is do dang
convenient I will be using it for some things.
