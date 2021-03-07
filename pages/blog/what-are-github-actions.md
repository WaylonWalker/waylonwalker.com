---
templateKey: blog-post
related_post_label: Check out this related post
tags:
- actions
title: What Are GitHub Actions
date: 2020-03-16T05:00:00.000+00:00
status: published
description: GitHub actions are an amazing tool that allows us to run code based
  on triggers inside of our repo.  Their is a large and growing community of actions
  inside the marketplace to use with very little effort.  Best of all they are free
  for public repositories, and private repos have a very generous free tier.
cover: "/static/what-are-github-actions.png"

---
<style>
h2 img { width: 100%; box-shadow: .5rem .5rem 3rem #141F2D, -.5rem -.5rem 3rem rgba(255,255,255,.1);}
img{ max-width: 100% !important;}
</style>

I have been diving deep into Github actions for about a month now and they are wicked good!  They allow you to run any sort of arbitrary code based on events in your repo, webhooks, or schedules.  They are very reasonably priced.  The interface that GitHub hs developed for them is top-notch!  It's so good I have done 90% of my editing of them right from github.com.

## TLDR

> some interaction to your repository **triggers** code to run.


## ![Online Editor](https://images.waylonwalker.com/gh-actions-header-online-editor.png)


The online editor for actions is pretty amazing.  When creating a new workflow it automatically sets up a new blank workflow or a workflow from the marketplace for you in your `.github/workflows` directory.  This is all it takes to get an action running, a `yaml` or `yml` file in the `.github/workflows` directory.


![github actions online editor](https://images.waylonwalker.com/gh-actions-editor.png "github actions online editor")

The editor does a great job of detecting syntax errors, misplaced keys.  It also does a great job at autocompletion.  As you type it will suggest keys that are accepted by the workflow syntax.  There is an embedded side pannel with docs and the marketplace to the right.


## ![Event Triggering](https://images.waylonwalker.com/gh-actions-header-event-triggering.png)


see this article from GitHub for a full set of details: [https://help.github.com/en/actions/reference/events-that-trigger-workflows](https://help.github.com/en/actions/reference/events-that-trigger-workflows "https://help.github.com/en/actions/reference/events-that-trigger-workflows")

You can trigger actions to run based on about any interaction with the repo that you can imagine, push, PR, webhooks, follows, create a branch, delete a branch, deployment, fork, wiki, issues, comments, labels, milestones, just check out the GitHub article for the full list.


### ![push/pr](https://images.waylonwalker.com/gh-actions-header-push-pr.png)

The most common and default trigger you will come across is the `on push`.  This means that on every push/pull_request the given action will run.  This is typically at the start of the file and will trigger the workflow for the whole file.

``` yaml
# Trigger the workflow on push or pull request
on: [push, pull_request]
```

You can also filter to only run on specific branches.  You probably only want to run your release workflow on the main branch, but want linting and testing on all branches.

``` yaml
push:
  branches:
   - main
pull_request:
  branches:
    - main

```
### ![schedule](https://images.waylonwalker.com/gh-actions-header-schedule.png)

It is also possible to set up your workflows to run on a schedule.  I have set a few of these up myself to do things such as updating/auditing npm dependencies and checking if the site is up.

``` yaml
on:
  schedule:
    # * is a special character in YAML so you have to quote this string
    - cron:  '*/15 * * * *'
```

### ![watch](https://images.waylonwalker.com/gh-actions-header-watch.png)

One issue that I have with GitHub actions is that there really isn't a good way to manually run workflows.  A workaround I found is that you can run a workflow when the repo is starred.

``` yaml
on:
  watch:
    types: [ started ]
```

If you have a public repo with some traction, you might want to avoid this hack, but if you did want to use it on a repo that may potentially get some stars randomly make sure that you filter to only your stars.

``` yaml
on:
  watch:
    types: [ started ]

jobs:
  run-on-star:
    runs-on: ubuntu-latest
    steps:
      - name: ✨ you starred your own repo
        if: github.actor == 'WaylonWalker'
```


## ![Free for public repositories](https://images.waylonwalker.com/gh-actions-header-free.png)

GitHub offers quite a generous free tier to get you started.

![gh-actions-free-tier](https://images.waylonwalker.com/gh-actions-free-tier.png "github actions free tier")

I think that GitHub's pricing just shows its commitment to the open-source.  Any public repo has unlimited build minutes!  I believe this goes for not only Linux actions, but  the more expensive windows and mac actions as well.

![github actions free for public repos](https://images.waylonwalker.com/gh-actions-free--for-public.png "GitHub actions free for public repos")


## ![Secrets](https://images.waylonwalker.com/gh-actions-header-secrets.png)

You will find that a lot of actions need things such as a GitHub personal access token.  You may even be hitting a third party API such as twitter or Gmail that require an API key.  These are things that need to be kept secret **DO NOT** put these as raw text inside your action.  The first tutorial I followed to deploy to GitHub pages did this 🤦‍♂️ and I followed.


![github built-in secret store](https://images.waylonwalker.com/gh-actions-built-in-secret-store.png "GitHub built-in secret store")

GitHub offers a wonderful secrets manager.  From your repository go to settings > secrets.  You can just add settings/secrets to the URL of your repo to get there as well.  From there add a new secret.  Now your secret is accessible by secret key using `${{ secrets.<your-key> }}` from anywhere in your workflows `yml` file.

GitHub has done an amazing job at hiding these secrets.  Anywhere that I have seen try to echo these secrets out into the console or anywhere just shows ***.  I am not sure if you can 100% rely on this, but they appear to have done a good job with it.

## ![Live Logs](https://images.waylonwalker.com/gh-actions-header-live-logs.png)

One great feature of actions is the live logs.  As you are developing them it is likely that you are anxiously watching them with anticipation.  Watching those logs go, and turn green is a great experience.

![github actions live logs](https://images.waylonwalker.com/gh-actions-live-logs.png "github actions live logs")



## ![Marketplace](https://images.waylonwalker.com/gh-actions-header-marketplace.png)

As with all things open source, much of the power of actions comes through the community and in actions case the marketplace.  Reusable actions can be deployed to the github marketplace.  Here they can be found from search, starred, and example workflows can be copied in one click.

![github actions marketplace](https://images.waylonwalker.com/gh-actions-marketplace.png "github actions marketplace")

I find that many times while I can write all of the code necessary in a shell script to do most of what I need, there is already an action in the marketplace that takes care of everything for me.  In fact there are usually several to choose from.



# #Discuss

* What Actions are you excited about?
* Are you using actions today?
* What struggles have you encountered with actions?
* Do you like these silly image headers I used? Do they kill A11y? I attempted to use good alt text to counter.
