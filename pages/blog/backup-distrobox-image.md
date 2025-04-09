---
date: 2025-04-09 17:35:50
templateKey: blog-post
title: backup distrobox image
tags:
  - linux
  - containers
  - distrobox
published: True

---

Today I'm upgrading my distrobox, but don't want to end up in a situation where
I can't get anything done becauase I work out of my distrobox.

``` bash
distrobox ls
distrobox stop devtainer
distrobox create --clone devtainer --name devtainer-20250409
distrobox enter devtainer
```
