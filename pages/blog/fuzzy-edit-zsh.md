---
templateKey: blog-post
tags: ['linux', 'bash']
title: Fuzzy File Editor from zsh
date: 2021-11-29T11:34:47
status: draft

---

https://youtu.be/PQw_is7rQSw

I am often in a set of tmux splits flying back and forth, accidently close my
editor, so when I come back to that split and hit my keybinds to edit files I
enter them into zsh rather than into nvim like I intended.  Today I am going to
sand off that rough edge and get as similar behavior to nvim as I can with a
couple of aliases.

## what's an alias

If you have never heard of an alias before it's essentialy a shortcut to a
given command.  You can pass additional flags to the underlying command and
they will get passed in.  Most of the time they are just shorter versions of
commands that you run often or even like in this case a common muscle memmory
typo that occurs for you.


## My new alias's for fuzzy editing files from zsh

Here are the new aliases that I came up with to smooth out my workflow.  These
give me a similar feel to how these keys work in neovim but from zsh.

``` bash
# fuzzy select file to edit
alias p='nvim `fzf --preview="bat --color always {}"`'

# give me the same syntax as edit while in neovim
alias :e='nvim '
```

Follow the [YouTube channel](https://youtube.com/waylonwalker) or the [rss
feed](https://waylonwalker/rss/) to stay up to date.


## Related links

* [playlist for my dotfiles challenge](https://www.youtube.com/playlist?list=PLTRNG6WIHETAj0nR_WYAxxGjd7kXch5zj)