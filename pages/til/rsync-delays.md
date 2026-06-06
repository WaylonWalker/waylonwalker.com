---
date: 2026-06-04 17:31:53
templateKey: til
title: rsync delays
published: true
tags:
  - bash

---

I've been deploying my site old school for most of this year, rsync to a volume
mounted to nginx.  I ran into an issue today where I updated my site and all of
the pages updated first, followed by upload.  The issue this created was that
the new cache busted css files were not up yet and the site had no styles for a
brief period during upload.

I found that delaying updates and delaying deletes until the new content exists
first solves this problem pretty well.  Theres still possiblility of jank while
uploading to a live directory and not doing some sort of hot swap, but I'm good
with this low budget option for now.

``` bash
sync:
	rsync -rlt --delete --omit-dir-times \
	--info=progress2 \
	--delay-updates \
	--delete-delay \
	./output/ \
	server:/mnt/mysite
```
