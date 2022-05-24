---
date: 2022-05-24 12:12:09
templateKey: til
title: git merge ours
status: 'draft'
tags:
  - git

---

Sometimes you have a pretty old branch you are trying to merge into and you are
absolutely sure what you have is what you want, and therefore you don't want to
deal with any sort of merge conflicts, you would rather just tell git to use my
version and move on.

## update main

The first step is to make sure your local copy of the branch you are moving
into is up to date.

``` bash
git checkout main
git pull
```

## update your feature branch

It's also worth updating your feature branch before doing the merge. Maybe you
have teammates that have updated the repo, or you popped in a quick change from
the web ui. It's simple and worth checking.

``` bash
git checkout my-feature
git pull
```

## start the merge

Merge the changes from main into `my-feature` branch.

```
git merge main
```

Now is where the merge conflict may have started. If you are completely sure
that your copy is correct you can `--ours`, if you are completely sure that
`main` is correct, you can `--theirs`.

```
git checkout --ours .
git merge --continue
```

This will pop open your configured `git.core.editor` or `$EDTIOR`. If you have
not configured your editor, it will default to vim.  Close vim with `<escape>:x`, accepting the
merge message.

Now push your changes that do not clash with main and finish your pr.

```
git push
```
