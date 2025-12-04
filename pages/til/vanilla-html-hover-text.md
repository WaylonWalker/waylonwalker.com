---
date: 2025-09-16 11:39:41
templateKey: til
title: vanilla html hover text
published: true
tags:
  - html

---

I needed to display some hover text in a web app that I am using tailwind and
jinja on.  It has no js, and no build other than the tailwind. I want this to
remain <span style='cursor: help; color:yellow;' title='respective to the
python developer I am and the team it is used for'>simple</span>. Turns out
that you can use a span with a title attribute to get hover text in
HTML.

``` html
<p>
I needed to display some hover text in a web app that I am using tailwind and
jinja on.  It has no js, and no build other than the tailwind. I want this to
remain <span style='cursor: help; color:yellow;' title='respective to the
python developer I am and the team it is used for'>simple</span>.
</p>
```
