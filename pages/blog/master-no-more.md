---
templateKey: blog-post
related_post_label: Check out this related post
tags: 
  - git
title: Master No More
date: 2020-06-11T05:00:00Z
status: published
description: It's been a long time coming.  We use some very harsh language
    within tech so much sometimes that we become numb to it.  It's time to do
    my very small part in this movement and purge this language from my active
    repos starting with this blog right here.
cover: '/static/master-no-more.png'

---

It's been a long time coming.  We use some very harsh language within tech so much sometimes that we become numb to it.  It's time to do my very small part in this movement and purge this language from my active repos starting with this blog right here.

https://waylonwalker.com/refactor-in-cli

> this post follows my method of refactoring code bases from the command line,
> read more about that in this article.

## c-s-f

First off browsing through the content of my blog I found many references to master.  I cannot completely whole-sale find and replace each one of them, because some of them are links that I do not own.  Any set of instructions got upgraded from `master` to `main`


``` diff
-  git checkout master
+  git checkout main
```

There were countless cases of examples like this to comb through, but it feels good to have them purged of old language.


## rename routes


Following yesterdays post, I am going to rename my markdown files

> /static/_redirects

### shorteners

``` diff
- /gdfm              /blog/today-i-learned-git-diff-feature-master/
- /blog/gdfm         /blog/today-i-learned-git-diff-feature-master/
+ /gdfm              /blog/today-i-learned-git-diff-feature-main/
+ /blog/gdfm         /blog/today-i-learned-git-diff-feature-main/
```

### redirect posts

``` diff
+ # master -> main
+
+ /blog/today-i-learned-git-diff-feature-master/   /blog/git-diff-feature-main/
```

### redirect external links to repo

``` diff
- /redirects      https://github.com/WaylonWalker/waylonwalkerv2/edit/master/static/_redirects
+ /redirects      https://github.com/WaylonWalker/waylonwalkerv2/edit/main/static/_redirects
```

More info on refactoring your blog routes with netlify here.

[![gracefully redirect cover image](https://images.waylonwalker.com/gracefully-redirect.png)](https://waylonwalker.com/gracefully-redirect/)


## _"Edit This post"_ Links

I literally just added _"edit this post"_ links to my rss feed and my blog feed.  This was a simple find and replace inside of my blog template and `gatsby-config.js`

## Don't Forget about CI

If you have build/deploy processes that specifically run on master or not on master dont forget to change those to main.  I did everything in a single commit and as soon as I pushed to main it started deploying gloriously.

``` diff
name: 🌱 Deploy site

on:
  push:
    branches:
-      - master
+      - main
```

## Now the fun part
_removing **master** completely_

I mostly just followed this [post by Scott Hanselman](https://www.hanselman.com/blog/EasilyRenameYourGitDefaultBranchFromMasterToMain.aspx).

``` bash
git branch -m master main
git push -u origin main
```

Then from GitHub go to settings>default branch> select main and accept the risk involved.

After your default is set to main, you have no use for master in your life anymore, time to purge it completely once and for all.  Go to <repo>/branches and trash it.

![delete master](https://images.waylonwalker.com/delete-master.png)


## Stop the Bleeding


I like how Scott included this nice alias for starting from main from the beginning.

``` bash
git config --global alias.new '!git init && git symbolic-ref HEAD refs/heads/main'
```

## See the Full Diff

If you happen to want to see the full diff of my change you can see it [here](https://github.com/WaylonWalker/waylonwalkerv2/commit/4bd26ba8faaf7c72e01cc4946d989e3284302cd0).



