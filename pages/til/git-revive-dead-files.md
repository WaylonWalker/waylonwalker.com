---
date: 2022-02-18 15:44:02.824187
templateKey: til
title: Revive files from the dead with git
tags:
  - git
  - cli

---

Git reflog can perform some serious magic in reviving your hard work
from the dead if you happen to loose it.

## caveat

You must git commit!  If you never commit the file, git cannot help you.
You might look into your trashcan, filesystem versions, onedrive, box, dropbox.
If you have none of this, then you are probably hosed.

## practice

I really like to practice these techniques before I need to use them so
that I understand how they work in a low stakes fashion.  This helps me
understand what I can and cannot do, and how to do it in a place that
does not matter in any way at all.

This is what I did to revive a dropped `docker-compose.yml` file.  The
idea is that if I can find the commit hash, I can `cherry-pick` it.

``` bash
git init
touch readme.md
git add readme.md
git commit -m "add readme"
touch docker-compose.yml
git add docker-compose.yml
git commit -m "add docker-compose"
git reset 3cfc --hard
git reflog
# copy the hash of the commit with my docker-compose commit
git cherry-pick fd74df3
```

## reflog

Here was the final reflog that shows all of my git actions.  **note** I
did reset twice.

``` bash
❯ git reflog --name-only
0404b6a (HEAD -> main) HEAD@{0}: cherry-pick: add docker-compose
docker-compose.yml
3cfcab9 HEAD@{1}: reset: moving to 3cfc
readme.md
9175695 HEAD@{2}: cherry-pick: add docker-compose
docker-compose.yml
3cfcab9 HEAD@{3}: reset: moving to 3cfc
readme.md
fd74df3 HEAD@{4}: commit: add docker-compose
docker-compose.yml
3cfcab9 HEAD@{5}: reset: moving to HEAD
readme.md
3cfcab9 HEAD@{6}: commit (initial): add readme
readme.md
```
