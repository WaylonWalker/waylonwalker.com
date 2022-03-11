---
date: 2022-03-10 19:19:34.621410
templateKey: til
title: Git Checkout Worktree
tags:
  - git
  - cli
  - linux

---

So worktrees, I always thought they were a big scary things.  Turns out they
are much simpler than I thought.

## Myth #1
_no special setup_

I thought you had to be all in or worktrees or normal git, but not both.  When
I see folks go all in on worktrees they start with a bare repo, while its true
this is the way you go all in, its not true that this is required.

## Lets make a worktree

Making a worktree is as easy as making a branch.  It's actually just a branch
that lives in another place in your filesystem.

``` bash
# checkout a new worktree called compare based on main in /tmp/project
git worktree add -b compare /tmp/project main

# checkout a new worktree called compare based on HEAD in /tmp/project
git worktree add -b compare /tmp/project

# checkout a worktree from an existing feature branch in /tmp/project
git worktree add /tmp/project my-existing-feature-branch
```

> The worktree that you create is considered a _linked worktree_, while the
> original worktree is called the _main worktree_

Note that I put this in my tmp directory because I don't expect it to live very
long, my recent use case was to compare two files after a big formatting
change.  You put these where you want, but dont come at me when your /tmp gets
wiped and you loose work.

 ## Myth #2
 _they are hidden mysterious creatures_

Just like branches git has some nice commands to help us understand what
worktrees we have on our system.  Firstly we have something very specific to
worktrees to list them out.

``` bash
git worktree list
```

gives the output

``` bash
/home/u_walkews/git/git-work-play  b202442 [main]
/tmp/another                       d9b2cf1 [another]
```

Even the branch command gives a bit different output for a worktree.

``` bash
git branch
```

gives this output, notice the + denotes an actively linked worktree, and the *
gives the active branch.  If you cd over to the worktree directory, these will
switch roles.

``` bash
+ another
  just-a-branch
* main
```

## You can only checkout a branch in one place

If you try to checkout a branch that is checked out in a linked worktree, you
will be presented with an error, and it will not let you check out a second
copy of that branch.

```
❯ git checkout another
fatal: 'another' is already checked out at '/tmp/another'
```

## Myth #3
_once you go worktree, you worktree_

Once you have worktrees on your system, you have a few ways to get rid of them.
Using git's way feels much superior, but if your a doof like me and didn't read
the manual before you `rm /tmp/another -rf` you will notice that the worktree
is still active.  If you run `git worktree prune` it will clean that right up.

``` bash
git worktree remove another

rm /tmp/another
git worktree prune
```

## It won't let you remove if you have changes

This makes me think that `remove` is a much safer option.  If you have
uncommitted changes, `git worktree remove` will throw an error, and make you
commit or use `--force` to remove the worktree.

``` bash
❯ git worktree remove another
fatal: 'another' contains modified or untracked files, use --force to delete it
```

## RTFM
_read the friendly manual_

There is a ton more information in the man page for worktrees, these are just
the parts that seemed really useful to me out of the gate.

``` bash
man git worktree
```
