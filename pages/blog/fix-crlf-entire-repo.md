---
templateKey: blog-post
tags: ['python', ]
title: fix crlf for entire git repo
date: 2021-03-22T00:00:00 
status: draft

---

## Final Result

``` bash
git checkout main
git reset --hard
git rm -rf --cached .
echo "* text=auto" > .gitattributes
git add .
```
