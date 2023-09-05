---
templateKey: blog-post
tags:
- git
- cli
title: git push without setting upstream
date: 2020-02-04T12:18:00Z
published: true

---

Finally after years of hand typing out a full `git push --upstream
my_really_long_and_descriptive_branch_name` I found there is a setting to
automatcally push to the current branch. More realisitically I just did a `git
push` let git yell at me, and copying the suggestion.

## git config

``` bash
git config --global push.default current
```

This one setting will now `git push` to the current branch without yelling at
you that your upstream does not match your current branch.  This helps me ship
chnages faster as I am constantly chnaging projects and branches.
