---
date: 2022-02-27 16:34:31.736146
templateKey: til
title: git diff-filter
tags:
  - git

---

Git commands such as `diff`, `log`, `whatchanged` all take a flag called
`--diff-filter`.  This can filter for only certain types of diffs, such
as added (A), modified (M), or deleted (D).

## Man page

You can find the full description by searching for `--diff-filter` in
the `man git diff` page.

``` bash
--diff-filter=[(A|C|D|M|R|T|U|X|B)...[*]]
    Select only files that are Added (A), Copied (C), Deleted (D), Modified (M), Renamed (R), have their type (i.e. regular file, symlink, submodule, ...)
    changed (T), are Unmerged (U), are Unknown (X), or have had their pairing Broken (B). Any combination of the filter characters (including none) can be used.
    When * (All-or-none) is added to the combination, all paths are selected if there is any file that matches other criteria in the comparison; if there is no
    file that matches other criteria, nothing is selected.

    Also, these upper-case letters can be downcased to exclude. E.g.  --diff-filter=ad excludes added and deleted paths.

    Note that not all diffs can feature all types. For instance, diffs from the index to the working tree can never have Added entries (because the set of paths
    included in the diff is limited by what is in the index). Similarly, copied and renamed entries cannot appear if detection for those types is disabled.
```

## Try it out

Open up a git repo and play around with this, here are some example that
I played with that seemed useful to me.

``` bash
# find when any files were deleted
git log --diff-filter D

# find when all files were added
git log --diff-filter A

# only one specific file
git log --diff-filter A -- readme.md

# partial match to a single file
git log --diff-filter A -- read*

# Find when all python files were added
git log --diff-filter A -- *.py
```
