---
date: 2024-04-15 21:19:21
templateKey: til
title: Tailwind Animations
published: true
tags:
  - webdev

---

I learned that tailwind animations are pretty easy to add only needing a few
classes.  For some reason though my brain broke, thinking that I could
dynamically change the number and you can't cause there are only so many pre
compiled classes without using an arbitrary value with brackets.

Here are the classes that I used to transition my colors very slowly.

``` html
<div id="square"
      class="transition-colors ease-in-out duration-700">
</div>
```

And the entire square element.

``` html
<div id="square"
      class="w-16 h-16 bg-rose-500 rounded border border-4 border-rose-800 hover:bg-indigo-600 hover:border-yellow-500 transition-colors ease-in-out duration-700">
</div>
```
