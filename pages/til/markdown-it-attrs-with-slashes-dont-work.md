---
date: 2025-02-01 11:21:10
templateKey: til
title: markdown it attrs with slashes dont work
published: true
tags:
  - webdev
  - blog
jinja: True

---


Attrs does not like '/' characters in its classes, so to use some tailwind
classes with custom values we must make new classes in our tailwind input css.

``` css
.cinematic {
  @apply aspect-[2.39/1];
}
```

Given the following markdown with attrs added to the image and to the paragraph
block.

``` markdown
![screenshot-2025-01-31T14-50-00-094Z.png](https://dropper.waylonwalker.com/api/file/50cfa8dc-9d46-4f02-877b-688fa5510a83.png){.aspect-[2.39/1]}

![screenshot-2025-01-31T14-50-00-094Z.png](https://dropper.waylonwalker.com/api/file/50cfa8dc-9d46-4f02-877b-688fa5510a83.png){.cinematic}

{.cinematic}
![screenshot-2025-01-31T14-50-00-094Z.png](https://dropper.waylonwalker.com/api/file/50cfa8dc-9d46-4f02-877b-688fa5510a83.png)
```

We get the following output with only the middle one working correctly.

![screenshot-2025-01-31T14-50-00-094Z.png](https://dropper.waylonwalker.com/api/file/50cfa8dc-9d46-4f02-877b-688fa5510a83.png){.aspect-[2.39/1]}

![screenshot-2025-01-31T14-50-00-094Z.png](https://dropper.waylonwalker.com/api/file/50cfa8dc-9d46-4f02-877b-688fa5510a83.png){.cinematic}

{.cinematic}
![screenshot-2025-01-31T14-50-00-094Z.png](https://dropper.waylonwalker.com/api/file/50cfa8dc-9d46-4f02-877b-688fa5510a83.png)

!!! Note
    The inline version of `.cinematic` works, but `.aspect-[2.39/1]` does not,
    it turns into text after the image.  The block version with the class
    before the image applies to the paragraph, not the image.
