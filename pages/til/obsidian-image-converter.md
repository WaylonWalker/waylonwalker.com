---
date: 2024-07-30 21:09:35
templateKey: til
title: Obsidian Image Converter
published: true
tags:
  - obsidian
  - blog
---

I'm giving obsidian a go as an editor for my blog and one of the main things I
want to fix in my workflow is the ability to quickly drop in images.  on first
look through the community plugins I found Image Converter.  I set it up to
convert to webp and drop them in a git submodule.  I may make it something
other than a git repo in the future, but I've learned that adding images to my
blog repo quickly makes it heavy and hard to clone on other machines.

![obsidian-image-converter-20240731211310793.webp](https://dropper.waylonwalker.com/api/file/626d85b1-5588-45c4-a4f4-c372dc7c8ff3.webp)

Once the images are there they are pushed and deployed as their own site to
cloudflare pages.  I made a quick edit to my [[sick-wikilink-hover]] plugin for
my blog.  if it sees a wikilink ending in webp, convert the domain over to
obsidian-assets.waylonwalker.com, and clean up the remaining `"!  "` that the
python md-it library leaves behind.

!!! note
    after first try I needed to increase the width from 600 to 1400, the image in this post was unreadable.

This is part of me getting set up and [[trying-obsidian]]
