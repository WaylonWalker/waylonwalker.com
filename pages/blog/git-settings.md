---
templateKey: blog-post
tags: ['git', 'linux']
title: How I configure git
date: 2021-06-25T20:50:45
published: false

---

Git can be a bit tricky to get configured correctly.  I often stumble into
config issues weeks after setting up a new machine that I did not even notice.
These are my notes to remind me how I configure git.

## Identity

``` bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

## rebase


## editor


``` bash
git config --global core.editor nvim
```


## default branch


``` bash
git config --global init.defaultBranch main
```

## push to current bransh wihtout setting upstream

``` bash
git config --global push.default current
```

## Autostash

``` bash
git config pull.rebase true
git config rebase.autoStash true
```
