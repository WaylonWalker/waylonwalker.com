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
