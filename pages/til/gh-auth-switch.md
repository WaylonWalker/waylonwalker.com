---
date: 2025-12-07 10:55:55
templateKey: til
title: gh auth switch
published: true
tags:
  - gh
  - cli
  - github

---

When using two GitHub accounts the gh cli gives very easy `gh auth switch` workflow from the cli.

!!! hint from the docs

  gh auth switch --help
  Switch the active account for a GitHub host.

  This command changes the authentication configuration that will
  be used when running commands targeting the specified GitHub host.

  If the specified host has two accounts, the active account will be switched
  automatically. If there are more than two accounts, disambiguation will be
  required either through the `--user` flag or an interactive prompt.

``` bash
# list accounts
gh auth status
# switch accounds (interactive if more than 2, i've never seen this personally)
gh auth switch
```
