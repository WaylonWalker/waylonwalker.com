---
templateKey: blog-post
tags: ['linux', 'vim',]
title: You must use augroup with autocmd in vim | Here's how
date: 2021-12-08T08:43:43
published: true

---

If you are running vim autocmd's without a group, you're killing your
performance.  Granted your probably not sourcing your vimscript files with
autocmd's too often, but every time you source that vimscript you are adding
another command that needs to run redundantly.

https://youtu.be/2ITTn4Dl0lc

## This is what I had
_Not silky smooth_

For **WAAY** too long I have had something like this in my  vimrc or init.vim.
It formats my python for me on every save, works great except if I source my
dotfiles more than once I start adding how many times black runs.

``` vim
autocmd bufwritepre *.py execute 'Black'
```

## Why is a bare autocmd bad
_let me demonstrate_

Lets create a new file called `format.vim` and give it the `:so %`. Works
great, it starts telling me that its formatting.

``` vim
autocmd bufwritepre *.py :echo("formatting with black")
```

![too-many-formats](https://images.waylonwalker.com/vim-augroups-too-many-formats.GIF)

**BUT** as every time I give it the `:so %` it formats an extra time on every
single save.

## Setting up an augroup

I've been told I need an `augroup` to prevent duplicates. So I did it, and
nothing changes, it still ran as many times as it was sources on every save.

``` vim
augroup black
    autocmd bufwritepre *.py :echo("formatting with black")
augroup end
```

## Clearing out the augroup

What you need to do is clear out all commands in the augroup with `autocmd!`
right at the beginning of the group.

``` vim
augroup black
    autocmd!
    autocmd bufwritepre *.py :echo("formatting with black")
augroup end
```

## My Final silky smooth setup

Now this is what I have in my dotfiles for a silky smooth setup that does not
run automds like crazy as I am making changes to my dotfiles.

``` vim
augroup waylonwalker
    autocmd!
    autocmd bufwritepre *.py execute 'PyPreSave'
    autocmd bufwritepost *.py execute 'PyPostSave'
    autocmd bufwritepost .tmux.conf execute ':!tmux source-file %' autocmd bufwritepost .tmux.local.conf execute ':!tmux source-file %'
    autocmd bufwritepost *.vim execute ':source %'
augroup end
```


## Related Links

* [vim-help](https://vimhelp.org/autocmd.txt.html#%3Aaugroup)
* [youtube video](https://youtu.be/2ITTn4Dl0lc) for this article
