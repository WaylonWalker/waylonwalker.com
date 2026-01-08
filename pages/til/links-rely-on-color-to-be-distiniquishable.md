---
date: 2024-12-17 20:25:12
templateKey: til
title: Links rely on color to be distiniquishable
published: true
tags:
  - webdev

---

Today i got hit by this accessibility issue on my site.  Low contrast links are
not distiniquishable.  I had not seen this error title before it was new to me,
maybe I have bad memory or maybe it's new to me.

![screenshot-2024-12-18T02-25-53-014Z.png](https://dropper.waylonwalker.com/api/file/24b4e31f-60db-47b8-b67c-07c4d4b6fb71.webp)

I ended up dropping the background color of the site down a notch as I didn't
really care for the semi-dark brown anyways.  I'm liking the near black
`bg-zinc-950` much better now.

![screenshot-2024-12-18T02-45-53-807Z.png](https://dropper.waylonwalker.com/api/file/8b4f2087-3f24-4212-ad00-74f294aff114.webp)

Now I got that 100 A11y score in lighthouse.

![screenshot-2024-12-18T03-02-18-934Z.png](https://dropper.waylonwalker.com/api/file/17497676-3730-4875-9e10-c6d121ba537a.webp)
