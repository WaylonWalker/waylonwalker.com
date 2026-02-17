---
title: '💭 Wes Bos on X: "Are you using position: absolute; to overlap el...'
date: 2024-09-13T15:43:03
templateKey: link
link: https://x.com/wesbos/status/1834242925401694490
tags:
  - webdev
  - css
published: true

---

> This is a pretty incredible use of css grid to overlay items overtop of each other without needing to resort to `position: absolute` and the side effects that it brings.


``` css
.wrap {
  display: grid;
  & > * {
    grid-row: 1;
    grid-column: 1;
  }
}
```

[Original thought](https://x.com/wesbos/status/1834242925401694490)
