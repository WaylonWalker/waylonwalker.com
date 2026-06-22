---
title: 'CSS @media print issues with background-color; - Stack Overflow'
date: 2023-11-30T03:00:52
template: link
link: https://stackoverflow.com/questions/3893986/css-media-print-issues-with-background-color#answer-14784655
tags:
  - webdev
  - css
  - thought
published: true

---

![[https://stackoverflow.com/questions/3893986/css-media-print-issues-with-background-color#answer-14784655]]

Get those print colors exact

``` css
body{
  -webkit-print-color-adjust:exact !important;
  print-color-adjust:exact !important;
}
```
