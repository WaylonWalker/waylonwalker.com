---
templateKey: blog-post
tags: ['python']
title: How I Review Pipeline Code
date: 2021-03-21T00:00:00
published: false

---

I have started doing more regular PR's on my teams
[Kedro](https://waylonwalker.com/what-is-kedro) pipelines.  I generally take a
two phase approach to the review in order to give the reviewee both quick and
detailed feedback.


https://waylonwalker.com/what-is-kedro

## initial scan (Phase1)

* passing ci
* Variable Names
* Antipatterns
* No commented out code
* Docsttrings generally make sense


Phase1 is typically a quick scan over the PR right within the PR window in my browser.

### Passing CI

* flake8
* black
* isort
* interrogate
* pytest
* build

The very first thing that needs to happen is automated CI.  We use things like
flake8, black, isort, interrogate to ensure that everyone follows generic style
guides like pep8.  The project does a build within the PR, but no deploy.

## Variable Names

I strugle really hard to not impose my own opinion into the PR at this point,
and sometimes really want to change a lot of variable names.  Typically I make
sure they don't grow longer than necessary, too short, misspelled, or
inconsistent.  I make sure that I can follow the flow without gettign tripped
up by names.

## Antipatterns

I am not too much of a zealot of any paradigm.  I am mostly looking for
readability and consistency.  Many times as we dig into an antipattern the
response is "Well I tried to do it the other way, but hit this issue".
Generally we figure out the problem together and avoid the antipattern, or
understand that this is an edge case and leave a comment for our future selves
to know why it is the way it is.

## No Commented Code

One of the biggest scars of a hard problem solving session is leaving behind
all the other things you tried commented out with no context.  I am a fan of
keeping things clean, because its real easy to forget which line was working
next time you comment out the good one.  You have made your best choice, run
with it and get rid of the clutter..


---

## clone (Phase2)

At this point it depends on the complexity of the change and confidence of the
reviewee.  If their changes are simple enough and they are confident with the
results its probably good enough to just review the changes.  If its a bigger
change I want to see the pipeline myself.




## viz

* disconnects

## load data

## step through operations

## run sections

## run functions
