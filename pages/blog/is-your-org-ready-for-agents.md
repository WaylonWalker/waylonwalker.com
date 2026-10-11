---
date: 2026-10-03T23:18:48Z
templateKey: blog-post
title: "Is Your Org Ready For Agents"
tags:
  - "Agents"
published: true
authors:
  - waylon
  - id: gpt-6-luna
    role: copy editor
    details: "Corrected spelling and grammar with GPT-6 Luna."
editorial_history:
- schema_version: 1
  event_id: bed11545-87fe-4d62-851a-71086e431cc1:pages/blog/is-your-org-ready-for-agents.md
  author: gpt-6-luna
  role: copy-editor
  action: edited
  recorded_by: gpt-6-codex
  recorded_at: '2026-10-11T15:07:10.314188+00:00'
  base_commit: 5de74ebc0a1023cf815006572f5cb63816ad81db
  commit: d3b1fe7083dbeffea0e28578ec8c1d0b2833e478
  path: pages/blog/is-your-org-ready-for-agents.md
  content_digest: sha256:372b3d4777136bb531601f8e77ad49f799462f7dcf092ce87748ce05f5036200
  digest_version: editorial-v1
  file_url: https://github.com/waylonwalker/waylonwalker.com/blob/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478/pages/blog/is-your-org-ready-for-agents.md
  diff_url: https://github.com/waylonwalker/waylonwalker.com/commit/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478#diff-72ac156f49b50f9ae8cfec87ff3ee2231152ee5499f2882e8f58de6aef3cd50c
  summary: Imported GPT-6 Luna copy edits after the owner confirmed exclusive authorship
    of these post diffs.
---

Listening to this video and feeling inspired.  It's crazy how the Conference ==AI Engineer== feels like such a hype bro conference ready to tell you just do more, let go, you're cooked if you're not on the train, gaslighting you to believe something they lack evidence for.  But what it really is, is a group of talks that are done by some of the best engineers trying to make it through this transition just like the rest of us.  Drawing the lines between the past and the current.  How do you get comfortable with the current without letting go, without giving in to shipping slop, but shipping real good work with confidence.

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

Can you, to the best of your ability, say what you are about to ship is of high quality and provides new features with fewer bugs?  Can you prove that your code compiles?  Can you prove that your code is not going to shit the bed given a valid input type from the user?

## CI

Everything done in testing, done automatically and blocking merge into the main branch.

## CD

Once you have passed all of your tests and made the merge, do you have a system to build good reliable repeatable artifacts.  Does it include the smallest possible surface area for attack, thinking heavily about supply chain attacks at this point in time.

## OTEL

_Monitoring with logs, spans, and traces_

Can you see bugs in production, who is affected by them, and make good decisions about how to fix them, what to fix, and whether to roll back or fix forward?

## Flexible Infrastructure

Can you roll back quickly?

Can you roll out a new release quickly?
