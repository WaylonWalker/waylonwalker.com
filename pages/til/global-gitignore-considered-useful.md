---
date: 2022-01-30 02:11:51.178788
templateKey: til
title: A Good Use for global .gitignore
tags:
  - git

---

I've never found a great use for a global `.gitignore` file.  Mostly I fear
that by adding a lot of the common things like `.pyc` files it will be missing
from the project and inevitibly be commited to the project by someone else.

## Personal Tools

Within the past year I have added some tools to my personal setup that are not
required to run the project, but works really well with my setup.  They are
`direnv` and `pyflyby`.  Since these both support project level configuration,
are less common, and not in most  `.gitignore` templates they make for great
candidates to add to a global `.gitignore` file.

## create the config

Like any `.gitignore` it supports gits wildignore syntax.  I made a
`~/dotfiles/git/.global_gitignore` file, and added the following to it.

```bash
.envrc
.pyflyby
```

Once I had this file, I stowed it into `~/.global_gitignore`.

``` bash
cd ~/dotfiles/
stow git
```

> Always stow your dotfiles, don't set yourself up for wondering why your next
> machine is not working right.

## stow note

Note, the reason that it is a `~/.global_gitignore` and not a `~/.gitignore` is
that I was unable to stow a `.gitignore file`.  They must be ignored by
default, and I was unable to figure out how to turn it back on.

## set the config

Next run this command to add the `~/.global_gitignore` to your gitignore as a
global excludesfile.

```bash
git config --global core.excludesfile ~/.global_gitignore
```

## commit it

Once you have done this you should have both your `~/dotfiles/git/.gitconfig`
and `~/dotfiles/.global_gitignore` ready to commit.

```bash
cd ~/dotfiles

git add git/.global_gitignore
git add git/.gitconfig

git commit -m "add global_gitignore"
```

## You didn't stow your .gitconfig

_the shame!_

No worries, lets get it into your dotfiles repo and stow it.

```bash
cd ~/dotfiles

# if you dont have a git directory make it.
mkdir git
mv ~/.gitconfig ~/devtainer/git
# now use stow to symlink it back to where it was
# so git works as expected.
stow git
```

## You dont have a dotfiles directory

_double shame 😲_

If you dont already have a dotfiles directry you should.  It is important for
it to be in your home directory for stow to work properly, if you really don't
want it there, look up how to configure stow to account for this.

```bash
# make a dotfiles directory and go there
mkdir ~/dotfiles
cd ~/dotfiles

# make it a git repo
git init

# if you dont have a git directory make it.

mkdir git
mv ~/.gitconfig ~/devtainer/git
# now use stow to symlink it back to where it was
# so git works as expected.
stow git
```
