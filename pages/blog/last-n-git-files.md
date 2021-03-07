---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: List the latest files to change in a git repo
date: 2020-10-08T05:00:00Z
status: 'false'
description: ''
cover: ''

---



``` bash
while read file; do echo $(git log --pretty=format:%ad -n 1 --date=raw -- $file) $file; done < <(git ls-tree -r --name-only HEAD | grep static/stories) | sort -r | head -n 3 | cut -d " " -f 3
```
