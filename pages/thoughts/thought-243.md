---
title: '💭 Arch Linux - News: The xz package has been backdoored'
date: 2024-04-16T13:00:33
templateKey: link
link: https://archlinux.org/news/the-xz-package-has-been-backdoored/
tags:
  - linux
  - arch
published: true

---

> Check your system to see if you are vulnerable to the xz backdoor.

I found this line most pertanent to me.

> The xz packages prior to version 5.6.1-2 (specifically 5.6.0-1 and 5.6.1-1) contain this backdoor.

Also it appears that arch is not vulnerable as it does not directly link openssh to liblzma, so the known attack vecotor is not possible.  read to the end of the linked article for more.



[Original thought](https://archlinux.org/news/the-xz-package-has-been-backdoored/)
