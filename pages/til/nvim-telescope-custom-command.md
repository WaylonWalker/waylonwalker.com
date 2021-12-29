---
date: 2021-12-27T20:24:48
templateKey: til
title: Opening files in vim from output of command
tags:
  - vim

---

Many command line tools can output a list of files, this is quite powerful.
I often want to search for something, then open it from a fuzzy picker.  This
can be done with fzf in the terminal, but often I am already in vim and I want
to open it inside my current session.

## Telescope
_how to pass a custom command to telescope_

Telescope is the fuzzy file finder I use every day inside of neovim.  Its pretty
fantastic and easy to extent like this.  This first example I am only passing in
files from the current working directory by using `ls`.

``` vim
:Telescope find_files find_command=ls
```

This brings up a normal Telescope picker with results from the `ls` command.

## More arguments
_how to pass a muli-argument command to telescope_

Adding more arguments can be done by comma separating them as shown in the
example below.  This command will run the silver-searcher, search for all
occurences of nvim inside of a markdown file, and return only the filepaths so
Telescope can pick from them.

```vim
:Telescope find_files find_command=ag,nvim,--md,-l
```
