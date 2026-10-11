---
date: 2026-09-30T00:14:58Z
templateKey: blog-post
title: "The Vomit Prompt"
tags:
  - "Ai, llm"
published: true
authors:
  - waylon
  - id: gpt-6-luna
    role: copy editor
    details: "Corrected spelling and grammar with GPT-6 Luna."
editorial_history:
- schema_version: 1
  event_id: bed11545-87fe-4d62-851a-71086e431cc1:pages/blog/the-vomit-prompt.md
  author: gpt-6-luna
  role: copy-editor
  action: edited
  recorded_by: gpt-6-codex
  recorded_at: '2026-10-11T15:07:10.332316+00:00'
  base_commit: 5de74ebc0a1023cf815006572f5cb63816ad81db
  commit: d3b1fe7083dbeffea0e28578ec8c1d0b2833e478
  path: pages/blog/the-vomit-prompt.md
  content_digest: sha256:aaba93b5adf07a17bef11e956720f5b529880cd4e1289128ee88751395e6bd0c
  digest_version: editorial-v1
  file_url: https://github.com/waylonwalker/waylonwalker.com/blob/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478/pages/blog/the-vomit-prompt.md
  diff_url: https://github.com/waylonwalker/waylonwalker.com/commit/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478#diff-f73199c0c9286db2cac3da4e3aa782f010895a45bd018eea57e2486be86956c2
  summary: Imported GPT-6 Luna copy edits after the owner confirmed exclusive authorship
    of these post diffs.
---
I heard Lex Friedman talk about this method he uses to create Greenfield apps really fast and he claimed worked really well with the latest Gen models at the time.  This was during the DHH round 2, 5 hour interview.

Lex asked if DHH uses voice chat at all.  DHH claimed it was too uncanny for him.  Too weird.  He said he still likes to feel like he is chiseling out something by hand.  He has interacted with a computer for a **quarter of a ==CENTURY==** to write open source code by typing into it with a keyboard, and it feels weird to talk to it.

Lex went on to say next time you have a _greenfield_ project, something you want to turn out well and fit your needs, and not have to fuss with it, turn on the mic and just word vomit for 20 minutes.  The models do **surprisingly** well at this.

Today I was feeling the weight of 20 or so PR's opened up mostly by agents awaiting my review.  This whole thing sits on my shoulders.  I'm the one that gets the calls when it's down, and I'm the one with the final say, but gawd it can be a drain to actually give each a good review and get them landed.

So I started a prompt.  The initial prompt was going to be a sentence or so...

> "write me a script to list all of my prs, prioritize, rank readiness"

This later turned into a 20 minute word vomit that included otel, database, API, sync engine, deterministic checks outside of ci, things like checking version and labeling the pr, pierre diffs (damn these are good) and copilot harness to conduct a preliminary review and auto fixes before I review.

I let that cook in opus 5.5 for about 45 minutes to an hour and went to a meeting, at the end of the meeting I saw it was running in my browser.  In absolute shock I had to hold the meeting over for 10 minutes to share with a coworker.

Both of us were in awe at how well this one shot did some things that we tried to get models to do 6 months ago and they just did a terrible job.  They were all seemingly bad at using azure and required such a well thought out plan that no one had time to just nail something like this in 20 minutes in the morning.

After using it for a day there are things I'm going to change workflow wise to make it better for me.  Things that I would probably simply accept as the truth in a tool, but since I have full access to it I'm going to nitpick it and make it glorious. Because I can.  

Rather than bitch about how we have to use shitty ass tools we can just ask for good ones.  I know this is not the case everywhere for everything.  I know there's much more complex software.  But the bar is being raised and you can just build shit.  Heck it seems  like all you need to do is ask for it.