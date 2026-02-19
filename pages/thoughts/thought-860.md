---
title: '💭 You already have a git server: (Maurycy''s blog)'
date: 2025-10-29T13:04:20
template: link
link: https://maurycyz.com/misc/easy_git/
tags:
  - git
  - thoughts
  - thought
  - link
published: true

---

![[https://maurycyz.com/misc/easy_git/]]

It's so easy to forget low level tech sometimes.  Things that are dead simple and just work without a hitch.  `git` is one of those rock solid things thats very easy to remember all that it does, this is a classic use case.

This just works

``` bash
cd /parent/directory/for/repo
git clone ssh://username@server/path/to/repo
```

In order to recieve you must update the remote to allow recieve.

``` bash
git config receive.denyCurrentBranch updateInstead
```

Now you can pull update push.  

It's funny how this was the way I first learned to do Continuous Deployment to a RHEL7 machine, also how Heroku worked, but its so easy to forget this solution is there.  I come across it every few years and immediately have a few use cases in mind.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
