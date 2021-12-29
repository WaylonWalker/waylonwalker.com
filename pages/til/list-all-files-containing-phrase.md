---
date: 2021-12-31T20:24:48
templateKey: til
title: List all the files containing a phrase
tags:
  - vim
  - linux
  - bash

---

One of the most useful skills you can acquire to make you faster at
almost any job that uses a computer is getting good at finding text in
your current working diretory and identifying the files that its in.  I
often use the silver searcher `ag` or ripgrep `rg` to find files in
large directories quickly.  Both have a sane set of defaults that ignore
hidden and gitignored files, but getting them to list only the filenames
and not the matched was not trivial to me.

> I've searched throught he help/man pages many times looking for these
> flags and they always seem to evade me.

## ag

Passing the flag `-l` to ag will get it to list only the filepath, and
not the match. Here I gave it a `--md` as well to only return markdown
filetypes.  `ag` supports a number of filetypes in a very similar way.

``` bash
ag nvim --md -l
```

## rg

Giving `rg` the `--files-with-matches` flag will yield you a similar set
of results, giving only the filepaths themselves and not the match
statement.  Also passing in the `-g "*.md"` will similarly yield only
results from markdown files.

``` bash
rg --files-with-matches you -g "*.md"
```
