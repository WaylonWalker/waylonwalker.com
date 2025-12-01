---
date: 2024-04-18 20:40:41
templateKey: til
title: ipython f2
published: true
tags:
  - python

---

Today I accidentally ran f2 in ipython to discover that it opens your $EDITOR!
I use this feature quite often in zsh, it is bound to `<c-e>` for me, and since
I have my environment variable `EDITOR` set to `nvim` it opens nvim when I hit
`<c-e>`.  Today I discovered that Ipython has this bound to `F2`.  If you know
how to set it to `<c-e>` let me know I've tried, a lot.

``` bash
export EDITOR=nvim
ipython
<F2>
```

better yet add `export EDITOR=nvim` to your .zshrc

``` bash
# ~/.zshrc
export EDITOR=nvim
```
