---
date: 2025-10-21 18:43:00
templateKey: til
title: Don't copy your gitignore to stignore
published: true
tags:
  - homelab

---

Today I learned that while `.stignore` and `.gitignore` look very similar they
are not.  My obsidian directory had been locked up for a few weeks and I had no
idea why until I logged into the web ui and saw errors.  The errors were some
confusing regex validator not matching.  I don't know what the exact error was,
but I went in and only ignored the files I cared about instead of the entire
gitignore.  Primarily I was getting conflicts in my `.git` directory.
