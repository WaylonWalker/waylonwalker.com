---
date: 2025-12-09 10:21:17
templateKey: til
title: web snow fall
published: true
tags:
  - webdev

---

I found snow-fall component from
[zachleat](https://www.zachleat.com/web/snow-fall/), and its beautiful... to
me.  I like the way it looks, its simple and whimsical.

## Install

There is an npm package `@zachleat/snow-fall` if that's your thing.  I like
vendoring in small things like this.

``` bash
curl -o static/snow-fall.js https://raw.githubusercontent.com/zachleat/snow-fall/refs/heads/main/snow-fall.js
```

I generally save it in my justfile so that I remember how I got it and how to
update.... yaya I could use npm, but I don't for no build sites.

``` bash
get-snowfall:
    curl -o static/snow-fall.js https://raw.githubusercontent.com/zachleat/snow-fall/refs/heads/main/snow-fall.js
```

## Usage

Now add the component to your page.

``` html
<!-- This belongs somewhere inside head -->
<script type="module" src="snow-fall.js"></script> <!-- Adjust the src to your path -->

<!-- This belongs somewhere inside body -->
<!-- Anything before will be below the snow. -->
<snow-fall></snow-fall>
<!-- Anything after will show above the snow. -->
```
