---
templateKey: blog-post
title: 📝 Git Notes
date: 2026-01-15 09:05:21 
published: true
description: Waylon Walker's Git Notes
tags:
- git

---

## See old revisions of one file

``` bash
git log --oneline -- <file>
git log -n 2 --oneline -- <file>
```

## Checkout an old revision of a file

``` bash
git checkout <commit> -- path/to/file
```

## fuzzy pick a file and check out an old revision

``` bash
#!/usr/bin/env bash
set -euo pipefail

file="${1:-}"

if [[ -z "${file}" ]]; then
  file="$(git ls-files | fzf --prompt="select file > ")" || exit 0
fi

if [[ -z "${file}" ]]; then
  exit 0
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not a git repository." >&2
  exit 1
fi

if ! git ls-files --error-unmatch -- "${file}" >/dev/null 2>&1; then
  echo "File is not tracked by git: ${file}" >&2
  exit 1
fi

choice="$(
  git log --follow --pretty=format:'%h %ad %s' --date=short -- "${file}" |
    fzf --ansi --no-sort --reverse \
        --preview-window=down:70% \
        --prompt="checkout revision > " \
        --preview "git show --color=always {1}^..{1} -- '${file}' 2>/dev/null || git show --color=always {1} -- '${file}'"
)"

if [[ -z "${choice}" ]]; then
  exit 0
fi

commit="$(awk '{print $1}' <<<"${choice}")"
git checkout "${commit}" -- "${file}"
```
