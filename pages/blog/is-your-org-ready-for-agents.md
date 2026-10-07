---
date: 2026-10-03T23:18:48Z
templateKey: blog-post
title: "Is Your Org Ready For Agents"
tags:
  - "Agents"
published: true

---

Listening to this video and feeling inspired.  Its crazy how the Conference ==AI Engineer== feels like such a hype bro conference ready to tell you just do more, let go, you're cooked if your not on the train, gaslighting you to believe something they lack evidence in.  But what it really is, is a group of talks that are done by some of the best engineers trying to make it through this transisition just like the rest of us.  Drawing the lines between the past and the current.  How do you get comfortable with the current without letting go, without giving in to shipping slop, but shipping real good work with confidence.

https://youtube.com/watch?v=Se8jHLliLXE

> It turns out that good ==Developer Experience== is also good ==Agent Experience==

## Checklist

I'm sure I'm missing a lot here, but this is what I'm thinking off the cuff.  If you dont have these you **need** to ==rethink== the first job for your new agents to begin work on your codebase.

* [ ] testing, linting, sast, type checking
* [ ] continuous integration
* [ ] continuous delivery
* [ ] local development
* [ ] Monitoring with logs, spans, and traces
* [ ] flexible infrastructure

## Testing
_do new changes cause regressions to working features_

Can you to the best of your ability say what you are about to ship is of high quality and provides new features with fewer bugs?  Can you prove that your code compiles?  Can you prove that your code is not going to shit the bed given a valid input type from the user?

## CI

Everything done in testing, done automatically and blocking merge into the main branch.

## CD

Once you have passed all of your tests and made the merge, do you have a system to build good reliable repeatable artifacts.  Does it include the smallest possible surface area for attack, thinkig heavily about supply chain attacks at%his point in time.

## OTEL

_Monitoring with logs, spans, and traces_

Can you see bugs in production, who is affected by them and make good decisions around how to fix, what to fix, rollback vs fix forward.

## Flexible Infrastructure

Can you rollback quickly?

Can you rollout a new release quickly?
