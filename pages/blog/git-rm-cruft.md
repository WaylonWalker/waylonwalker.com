---
templateKey: "blog-post"
title: remove git cruft
date: 2019-01-21
published: false
description:
tags:
  - git
---

## inspiration

My original inspiration for this post came from steven ostermiller's blog post
that no longer exists from my last check in May, 2024.

[https://blog.ostermiller.org/removing-and-purging-files-from-git-history/](https://blog.ostermiller.org/removing-and-purging-files-from-git-history/){.hoverlink}

I was able to find it on the way back machine though.

[https://web.archive.org/web/20240222195617/https://blog.ostermiller.org/removing-and-purging-files-from-git-history/](https://web.archive.org/web/20240222195617/https://blog.ostermiller.org/removing-and-purging-files-from-git-history/)

```bash
git log --all --pretty=format: --name-only --diff-filter=D | sed -r 's|[^/]+$||g' | sort -u
```

```bash
git filter-branch --tag-name-filter cat --index-filter 'git rm -r --cached --ignore-unmatch FILE_LIST' --prune-empty -f -- --all
```

```bash
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --aggressive --prune=now
```

```bash
git push origin --force --all
git push origin --force --tags
```

```bash
cd MY_LOCAL_GIT_REPO
git fetch origin
git rebase
git reflog expire --expire=now --all
git gc --aggressive --prune=now
```
