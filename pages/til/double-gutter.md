---
date: 2026-02-14 09:12:42
templateKey: til
title: double gutter
published: true
tags:
  - webdev

---

I keep forgetting about the double gutter problem with nested containers.  When
you put padding on a parent and the child also has padding, you get twice the
spacing you wanted.

## The Problem

```css
.container {
  padding: 2rem;
}

.child {
  padding: 2rem;
}
```

Now your content is 4rem from the edge.  Not what I meant at all.

## The Fix

Either remove padding from the parent or use `box-sizing: border-box` and plan
for it.  I usually just drop the parent padding when I realize what I have done.