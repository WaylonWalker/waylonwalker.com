---
templateKey: blog-post
tags: []
title: Maintianing multiple git repos with mu-repo
date: 2021-06-10T10:44:17
published: false

---

## Quickstart

``` bash
# installation
pip install mu-repo

## register repos
mu register --recursive
mu list

# run git commands
mu status --short
mu diff -U0 --color | bat

# run shell commands
mu sh $(grep -iRl "KEDRO_GID=0" | xargs sed -i "s/KEDRO_GID=0/KEDRO_GID=5/g")
```

## Registering Repos
``` bash
mu register --all
mu register --all
mu register --recursive

mu unregister --all
```

https://waylonwalker.com/bash/

> I have similar command line related shortcuts in my bash notes

## Full Help

``` bash
mu --help

* mu register repo1 repo2: Registers repo1 and repo2 to be tracked.
* mu register --all: Registers all subdirs with .git (non-recursive).
* mu register --current: Registers all subdirs with .git (non-recursive).
* mu register --recursive: Registers all subdirs with .git (recursive).
* mu unregister repo1 repo2 | --all: Stops tracking some repository.
* mu list: Lists the currently tracked repositories.
* mu set-var git=d:/bin/git/bin/git.exe: Set git location to be used.
* mu set-var serial=0|1: Set commands to be executed serially or in parallel.
* mu get-vars: Prints the configuration file.
* mu fix-eol: Changes end of lines to '\n' on all changed files.
* mu find-branch [-r] *pat*:
    Finds all branches matching a given pattern (or simply mu fb).
* mu git-init-config: Initial git configuration (username, log, etc.)
* mu --version: Prints its version
* mu auto-update: Automatically updates mu-repo
  (using git -- if it was installed from the repo as in the instructions).

* mu dd:
     Creates a directory structure with working dir vs head and opens
     WinMerge with it (doing mu ac will commit exactly what's compared in this
     situation).

     Also accepts a parameter to compare with a different commit/branch. I.e.:
     mu dd HEAD^^
     mu dd 9fd88da
     mu dd development

* mu sh <command line>
   Allows calling any command line in the registered repositories
   e.g.: mu sh ls -la will call ls -la on all registered repositories.

* mu clone: Cloning multiple repos from a base url.
  Use mu clone --help to open browser with more details.

* mu <command> repo:<repo1>,<repo2>
   Allows specifying target repositories for a single command:
   e.g.: mu st repo:repo1,repo2: Will do st on repo1 and repo2.

* mu group: Repository grouping

  * mu group add <name> [--empty]:
      Creates new group with current repositories, unless --empty is given
  * mu group rm <name>: Removes a group
  * mu group switch <name>: Switches to an existing group
  * mu group reset: Stops using the current group (uses all repos again).
  * mu group: With no parameters, just lists current groups

  Use mu register normally to add repositories to the current group
  Use mu list to list repositories in the current group

Shortcuts:

mu st         = Nice status message for all repos (always in parallel)
mu co branch  = git checkout branch
mu mu-branch  = git rev-parse --abbrev-ref HEAD (print current branch)
mu up         = git fetch origin curr_branch:refs/remotes/origin/curr_branch
mu up --all   = git fetch origin (always in parallel)
mu upd | sync = up/diff incoming changes
mu a          = git add -A
mu c msg      = git commit -m "Message" (the message must always be passed)
mu ac msg     = git add -A & git commit -m (the message must always be passed)
mu acp msg    = same as 'mu ac' + git push origin current branch.
mu p          = git push origin current branch.
mu rb         = git rebase origin/current branch.
mu shell      = On msysgit, call sh --login -i (linux-like env)
mu fb [-r] pat= Shortcut for find-branch

Any other command is passed directly to git for each repository:
I.e.:

mu pull
mu fetch
mu push
mu checkout release

Note: Actions considered safe may always be executed in parallel (i.e.: mu st)

Note: Passing --timeit in any command will print the time for the command.
```
