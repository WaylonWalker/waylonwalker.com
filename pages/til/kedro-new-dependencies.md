---
templateKey: til
tags: ['kedro', 'python']
title: Add New Dependencies to Your Kedro Project
date: 2022-01-28T21:30:48

---

As you work on your kedro projects you are bound to need to add more
dependencies to the project eventually.  Kedro uses a fantastic command
`pip-compile` under the hood to ensure that everyone is on the same version of
packages at all times, and able to easily upgrade them.  It might be a bit
different workflow than what you have seen, let's take a look at it.

## git status

Before you start mucking around with any changes to dependencies make sure that
your git status is clean.  I'd even reccomend starting a new branch for this,
and if you are working on a team potentially submit this as its own PR for
clarity.

``` bash
git status
git checkout main
git checkout -b add-rich-dependency
```

## requirements.in

New requirements get added to a requirements.in file.  If you need to specify
an exact version, or a minimum version you can do that, but if all versions
generally work you can leave it open.

``` bash
# requirements.in
rich
```

Here I added the popular `rich` package to my `requirements.in` file.  Since
I am ok with the latest version I am not going to pin anything, I am going to
let the pip resolver pick the latest version that does not conflict with any of
my dependencies for me.

## build-reqs

The command `kedro build-reqs` will tell kedro to recompile the
`requirements.txt` file that has all of our dependencies pinned down to exact
versions.  This ensures that all of our teammates and production workflows use
the same exact versions of packages even if new ones are released after we
installed on our development machines.

``` bash
kedro build-reqs
```

## git add

Now that we have our new dependencies ready to go commit those to git, and
submit a PR for them if you are working on a team.  This is a good way to
document the discussion of adding new dependencies to your teams project.

``` bash
git add requirements.in
git add requirements.txt
git status
git commit -m "FEAT updated dependencies with rich"
git push
# go make a pr
gh pr create --title "feat add rich to dependencies" --body "I added rich as a dependency, and ran pip-compile"
```
