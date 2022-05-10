---
date: 2022-05-10 14:57:35
templateKey: til
title: Bash function to edit scripts faster
tags:
  - bash

---

I am often editing my own scripts as I develop them. I want to make a better
workflow for working with scripts like this.

## Currently

Currently I am combining `nvim` with a `which` subshell to etit these files
like this.

> for now lets use my todo command as an example

``` bash
nvim `which todo`
```

## First pass

On first pass I made a bash function to do exactly what I have been doing.

```bash
ewhich () {$EDITOR `which "$1"`}
```

The `$1` will pass the first input to the which subshell.  Now we can edit our todo script like this.

```bash
ewich todo
```

>  Note, I use bash functions instead of aliases for things that require input.

## Final State

This works fine for commands that are files, but not aliases or shell
functions.  Next I jumped to looking at the output of `command -V $1`.

* if the command is not found, search for a file
* if its a builtin, exit
* if its an alias, open my `~/.alias file to that line`
* if its a function, open my `~/.alias file to that line`

``` bash
ewhich () {
case `command -V $1` in
    "$1 not found")
        FILE=`fzf --prompt "$1 not found searching ..." --query $1`
        [ -z "$FILE" ] && echo "closing" || $EDITOR $FILE;;
    *"is a shell builtin"*)
        echo "$1 is a builtin";;
    *"is an alias"*)
        $EDITOR ~/.alias +/alias\ $1;;
    *"is a shell function"*)
        $EDITOR ~/.alias +/^$1;;
    *)
        $EDITOR `which "$1"`;;
esac
```

## a bit more ergo, and less readable

To make it easier to type, at the sacrifice of readability for anyone watching
I added a single character `e` alias to ewhich.  So when I want to edit
anything I just use `e`.

```bash
alias e=ewhich
```

## Results

Here is a quick screencast of how it works.

<video autoplay="" controls="" loop="true" muted="" playsinline="" width="100%">
     <source src="https://images.waylonwalker.com/ewhich.webm" type="video/webm">
     Sorry, your browser doesn't support embedded videos.
</video>
