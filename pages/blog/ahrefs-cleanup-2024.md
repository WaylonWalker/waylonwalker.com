---
dateCreated: 2025-02-12 12:51:39
date: 2025-02-12 12:56:40
templateKey: blog-post
title: ahrefs-cleanup-2024
tags:
  - meta
  - blog
  - ahrefs
published: True

---

This post is a big work in progress, expect it to keep getting better.

## Initial Score

![image](https://dropper.wayl.one/api/file/b26d4352-1bce-43a1-942e-bd6d7bd7c11d.webp)

## 404 Not Found, generate a page for each tag

![image](https://dropper.wayl.one/api/file/c501e0f7-b3c1-4124-b6b4-727d7e3e95a8.webp)

## Title too long

![image](https://dropper.wayl.one/api/file/4184948f-3527-4a17-8c65-b61e75d9ec75.webp)

## 404 Not Found, comma separated tags

Another hit on 404's caused by tags, was tag parsing from thoughts into posts,
this cause links to the full comma separated list of tags rather than one per
tag.

![image](https://dropper.wayl.one/api/file/c01ebd69-5ac4-4d9b-b720-43a16f64f421.webp)

You can see on the website the whole dang set of tags was being treated as a single tag.

![image](https://dropper.wayl.one/api/file/398b3bc7-8cfe-4190-968d-73eb15e18ea2.webp)

## Broken images

![screenshot-2025-01-15T17-31-20-430Z.png](/api/file/b3a1e8de-9344-40b4-8020-9e75a59b5dd9.png)

## I burned all of my January Credits

 v

![image](https://dropper.wayl.one/api/file/cfed3e97-8dd4-4381-b38f-5dc6f40e7fad.webp)

![image](https://dropper.wayl.one/api/file/1ffbd8f7-1f81-40b9-b110-1b0f03bdd56f.webp)

## md files were Missing

I had several links out to the raw source of some pages generally hosted at
`{slug}.md`, but I had turned it off due to it causing builds to fail.

![image](https://dropper.wayl.one/api/file/db074f86-725a-4b34-a5e2-8424628f521e.webp)

Taking another look at the error it was obvious what was going on, thoughts
never had a file extension and Pathlib was throwing isADirecotryError because
the path was already a directory for the index.html, adding a .md to the path
for the thoughts plugin fixed it.

<https://github.com/WaylonWalker/waylonwalker.com/commit/e0bbc777efd5d0309a107b0d3e7355b2426e8c47>
