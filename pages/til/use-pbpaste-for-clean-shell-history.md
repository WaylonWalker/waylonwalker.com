---
date: 2025-03-17 12:00:00
templateKey: til
title: Use pbpaste for clean shell history
published: true
tags:
  - linux
  - cli
---

Using `pbpaste` for command substitution keeps sensitive or long URLs out of
your shell history. Instead of typing `git clone
https://github.com/user/repo-with-long-name.git`, copy the URL to clipboard and
run `git clone "$(pbpaste)"`. This prevents the URL from appearing in
`~/.bash_history` or `~/.zsh_history`.

To get pbpaste working on both Xorg and Wayland, add this to your shell config:

```bash
if [[ $(command -v wl-copy) ]]; then
    alias pbcopy='wl-copy'
    pbpaste() { wl-paste; }
elif [[ $(command -v xclip) ]]; then
    alias pbcopy='xclip -selection clipboard'
    pbpaste() { xclip -selection clipboard -o; }
fi
```

The function approach (instead of alias) enables command substitution, while
the quotes around `$(pbpaste)` handle spaces and special characters safely.

Now you can use it.

``` bash
git clone "$(pbpaste)"
```

More importantly secrets can stay out of your history.

``` bash
export GITHUB_TOKEN="$(pbpaste)"
export AWS_ACCESS_KEY_ID="$(pbpaste)"
export AWS_SECRET_ACCESS_KEY="$(pbpaste)"
export DATABASE_URL="$(pbpaste)"
```
