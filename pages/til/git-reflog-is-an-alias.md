---
date: 2022-02-19 15:02:52.318805
templateKey: til
title: Git reflog is an alias for git log -g
tags:
  - git
  - cli

---


Right inside the git [docs](https://git-scm.com/docs/git-reflog#_description),
is states that the `git reflog` command runs `git reflog show` by default which
is an alias for `git log -g --abbrev-commit --pretty=oneline`

This epiphany deepens my understanding of git, and lets me understand that most
`git log` flags might also work with `git log -g`.


## full or short format

Here are some git commands for you to try out on your own that are all pretty
similar, but vary in how much information they show.

``` stat
# These show only first line of the commit message subject, the hash, and index
git reflog
git log -g --abbrev-commit --pretty=oneline

# similar to git log, this is a fully featured log with author, date, and full
# commit message
git log -g
```

## add files

If I am looking for a missing file, I might want to leverage `--name-only` or
`--stat`, to see where I might have hard reset that file, or deleted it.

```
git reflog --stat
git log -g --stat --abbrev-commit --pretty=oneline

git reflog --name-only
git log -g --name-only --abbrev-commit --pretty=oneline
```

## example

Here is an example where I lost my `docker-compose.yml` file in a git reset,
and got it back by finding the commit hash with `git reflog` and cherry picked
it back.

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

This just proves that its harder to remove something from git, than it is to
get it back.  It can feel impossible to get something back, but once its in, it
feels even more impossible to get it out.
