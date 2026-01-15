#!/usr/bin/env bash
set -euo pipefail

file="${1:-}"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not a git repository." >&2
  exit 1
fi

# If file specified, filter stashes containing it; otherwise show all
if [[ -n "${file}" ]]; then
  stash_list="$(git stash list --pretty=format:'%gd %cr %s' | while IFS= read -r stash_line; do
    stash_ref="$(awk '{print $1}' <<<"${stash_line}")"
    if git diff --name-only "${stash_ref}^..${stash_ref}" 2>/dev/null | grep -qF "${file}"; then
      echo "${stash_line}"
    fi
  done)"
else
  stash_list="$(git stash list --pretty=format:'%gd %cr %s')"
fi

if [[ -z "${stash_list}" ]]; then
  echo "No stashes found${file:+ containing: ${file}}" >&2
  exit 0
fi

# Select stash
stash_choice="$(echo "${stash_list}" | fzf --ansi --no-sort --reverse \
  --preview-window=down:70% \
  --prompt="select stash > " \
  --preview "git stash show -p {1} --color=always"
)"

if [[ -z "${stash_choice}" ]]; then
  exit 0
fi

stash_ref="$(awk '{print $1}' <<<"${stash_choice}")"

# If no file specified, let user select one from the stash
if [[ -z "${file}" ]]; then
  file="$(git diff --name-only "${stash_ref}^..${stash_ref}" | 
    fzf --ansi --no-sort --reverse \
      --preview-window=down:70% \
      --prompt="select file > " \
      --preview "git show --color=always ${stash_ref}:{} 2>/dev/null || echo 'Preview unavailable'"
  )" || exit 0
fi

if [[ -z "${file}" ]]; then
  exit 0
fi

# Checkout the file from the stash
git checkout "${stash_ref}" -- "${file}"
