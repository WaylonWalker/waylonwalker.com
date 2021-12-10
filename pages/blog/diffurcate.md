---
templateKey: blog-post
tags: ['linux', 'bash', 'git']
title: Code Review from the comfort of vim | Diffurcate
date: 2021-12-04T11:34:47
status: published

---

I often review Pull requests from the browser as it just makes it so easy to see
the diffs and navigate through them, but there comes a time when the diffs get
really big and hard to follow.  That's when its time to bring in the comforts of
vim.

https://youtu.be/5NKaZFavM0E

## Plugins needed

This all stems from the great plugin by
[AndrewRadev](https://github.com/AndrewRadev).  It breaks a down
into a project.  So rather than poping into a pager from git diff,
you can pipe to diffurcate and it will setup a project in a tmp
directory for you and you  can browse this project just like any
other except it's just a diff.

``` vim
Plug 'AndrewRadev/diffurcate.vim'
```

## My aliases

First to quickly checkout PR's from azure devops I have setup an alias to fuzzy
select a pr and let the `az` command do the checkout.

``` bash
alias azcheckout='az repos pr checkout --id $(az repos pr list --output table | tail -n -2 | fzf | cut -d " " -f1)'
```

Next I have a few aliases setup for checking diffs.  The first one checks what
is staged vs the current branch, the others check the current branch vs main or
master.

```
alias diffstaged="git diff --staged | nvim - +Diffurcate '+Telescope find_files'"
alias diffmain="git diff main.. | nvim - +Diffurcate '+Telescope find_files'"
alias diffmaster="git diff master.. | nvim - +Diffurcate '+Telescope find_files'"

diffcommit() {
    git diff $1 | nvim - +Diffurcate '+Telescope find_files'
}

```

## Links

* [diffurcte.vim](https://github.com/AndrewRadev/diffurcate.vim)
