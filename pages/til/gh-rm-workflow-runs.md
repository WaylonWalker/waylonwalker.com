
---
date: 2022-09-01 19:12:34
templateKey: til
title: GitHub Actions Delete all Workflow Runs
status: 'published'
tags:
  - bash

---

Today I ran a bunch of actions, but I wanted to clean up all the runs that I
used to get it setup so that I had a good clean history to refer back to later.

I found [this post](https://devx.pw/gists/batch-delete-workflow-runs/)

``` bash
gh api \
    repos/waylonwalker/hatch-version-action-example/actions/runs | \
    jq '.workflow_runs[].id' | \
    xargs -n1 -I % gh api repos/waylonwalker/hatch-version-action-example/actions/runs/% -X DELETE
```
