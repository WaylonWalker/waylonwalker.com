---
date: 2025-01-20 13:55:37
templateKey: til
title: emoji in headless chrome in docker
published: true
tags:
  - docker

---

I recently noticed that my og images were missing emoji.  They were taken using
headless chrome in a container.  I fixed it by adding an emoji font in the
containerfile / dockerfile.

``` Dockerfile
RUN apt-get update && apt-get install -y \
    # Add fonts with emoji support
    fonts-noto-color-emoji \
    && rm -rf /var/lib/apt/lists/*
```

## Before

Here's what they were looking like with broken emoji fonts.

![image](https://dropper.wayl.one/api/file/6e9060f2-0e15-4f22-88b6-b6ec5ddb34de.webp)

## After

And now with the fixed emoji font.

![image](https://dropper.wayl.one/api/file/8ed5e338-50c2-4130-8cce-549ecc802f01.webp)

> I put thought bubbles on my thoughts posts and stars on my github stars posts
