---
date: 2022-06-28 12:31:10
templateKey: til
title: Two new shell aliases for git
status: 'published'
tags:
  - git

---

![Astronaut doing a mic drop with explosion](https://stable-diffusion.waylonwalker.com/000172.3260819219.webp)

Recently I added two new bash/zsh aliases to make my git experience just a tad
better.

## trackme

Most of our work repos were recently migrated to new remote urls, we scriped
out the update to all of the repos, but I was left with a tracking error for
all of my open branches.  To easily resolve this I just made an alias so that I
can just run `trackme` anytime I see this error.

```txt
There is no tracking information for the current branch.
    Please specify which branch you want to merge with.
    See git-pull(1) for details

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream develop origin/<branch>
```

### getting the branch

The following command will always return the currently checked out branch name.

``` bash
git symbolic-ref --short HEAD
```

Injecting this into the suggested `git` command as a subshell gives us this
alias that when ran with `trackme` will automatically fix tracking for my
branch.

``` bash
alias trackme='git branch --set-upstream-to=origin/$(git symbolic-ref --short HEAD)'
```

## rebasemain

I sometimes get a bit lazy at checking main for changes before submitting any
prs, so again I made a quick shell alias that will rebase main into my branch
before I open a pr.

``` bash
alias rebasemain='git pull origin main --rebase'
```

## The Aliases

Here are both of the alias's, feel free to steal and modify them into your
dotfiles.  If you are uniniatiated a common starting place to put these is
either in your `~/.bashrch` or `~/.zshrc` depending on your shell of choice.

``` bash
alias trackme='git branch --set-upstream-to=origin/$(git symbolic-ref --short HEAD)'
alias rebasemain='git pull origin main --rebase'
```
