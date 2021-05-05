---
templateKey: blog-post
tags: ['linux', 'bash']
title: Create a Virtual File Gallery with Symlinks
date: 2021-05-05T08:23:33
status: published

---

Creating a directory that is a union of several directories can be achieved
with a few symlinks at the command line.

## Creating a Virtual File Gallery

Here is how I am creating a virtual directory of all my projects that is a
combination of both work and not-work projects.  I am creating symlinks for
every directory under `~/work` and `~/git`.

``` bash
rm -rf ~/projects
mkdir ~/projects
ln -sf ~/work/* ~/projects
ln -sf ~/git/* ~/projects
```

> ⚠ Notice that first I am recreating the directory each time, this will ensure
> that any project that is deleted from their actual directory is removed from
> the virtual gallery.
 
 ## Updating the gallary

 Since they are links they are always kept up to date without any extra work,
 all the data is still in the same place it started.  But as new directories
 are added to any of the virtual directories they will not be automatically
 added to the virtual gallery.

* cron
* bashrc/zshrc

If you're concerned about system resources you can add it to a cron job to run
at a regular schedule that makes sense to you.  For me I just popped those 4
lines right in my `~/.zshrc`.  Its a bit overkill, maybe bloat, but it runs in
an impercieveable amount of time.

## Automatically CD to the real directory

When you cd into a `~/projects/my-proj` directory your `$PWD` will still be
`~/projects/my-proj`.  I did not want this for my use case, I wanted to follow
the symlink to the real directory.  I found there were two options that worked
for me.


```
alias cd='cd -P'
set -o physical
```

> Add either of these to your `.bashrc`/`.zshrc` to follow symlinks to the
> actual directory.

