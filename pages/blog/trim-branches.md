---
templateKey: blog-post
tags: ['git', 'bash', 'linux']
title: Trim unused git branches
date: 2021-05-07T09:47:24
published: true

---


## Trim branches no longer on origin

```bash
git remote prune origin --dry-run
git remote prune origin
```

## Find branches already merged

``` bash
git checkout main
# list remote branches that have already been merged into main
git branch -r --merged
# list local branches that have already been merged into main
git branch --merged
```
