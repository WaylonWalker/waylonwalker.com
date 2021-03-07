---
templateKey: 'blog-post'
title: remove git cruft
date: 2019-01-21
status: draft
description:
tags:
    - git
---


## inspiration

https://blog.ostermiller.org/removing-and-purging-files-from-git-history/

``` bash
git log --all --pretty=format: --name-only --diff-filter=D | sed -r 's|[^/]+$||g' | sort -u
```
``` bash
git filter-branch --tag-name-filter cat --index-filter 'git rm -r --cached --ignore-unmatch FILE_LIST' --prune-empty -f -- --all
```

``` bash
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --aggressive --prune=now
```

``` bash
git push origin --force --all
git push origin --force --tags
```

``` bash
cd MY_LOCAL_GIT_REPO
git fetch origin
git rebase
git reflog expire --expire=now --all
git gc --aggressive --prune=now
```
