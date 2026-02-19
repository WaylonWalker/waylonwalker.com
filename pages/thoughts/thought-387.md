---
title: '💭 Wes Bos on X: "Are you using position: absolute; to overlap el...'
date: 2024-09-13T15:43:03
template: link
link: https://x.com/wesbos/status/1834242925401694490
tags:
  - webdev
  - css
  - thoughts
  - thought
  - link
published: true

---

![[https://x.com/wesbos/status/1834242925401694490]]

This is a pretty incredible use of css grid to overlay items overtop of each other without needing to resort to `position: absolute` and the side effects that it brings.


``` css
.wrap {
  display: grid;
  & > * {
    grid-row: 1;
    grid-column: 1;
  }
}
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
