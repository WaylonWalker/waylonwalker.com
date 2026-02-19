---
title: '💭 Database Remote-Copy Tool For SQLite (draft)'
date: 2024-10-05T20:56:49
template: link
link: https://simonwillison.net/2024/Oct/4/sqlite-rsync/
tags:
  - sqlite
  - thoughts
  - thought
  - link
published: true

---

![[https://simonwillison.net/2024/Oct/4/sqlite-rsync/]]

Simon shared a really cool new utility tool for sqlite ispired by rsync.  It checks hashes of each sqlite page and syncs pages.  So if nothing in the database has changed it will only require 0.5% the bandwidth as a copy would.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
