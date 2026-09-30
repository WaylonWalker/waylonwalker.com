---
date: 2026-09-30T00:14:58Z
templateKey: blog-post
title: "The Vomit Prompt"
tags:
  - "Ai, llm"
published: true

---
I heard Lex Friedman talk about this method he uses to create Greenfield apps really fast and he claimed worked really well with the latest Gen models at the time.  This was during the DHH round 2, 5 hour interview.

Lex asked if DHH uses voice chat at all.  DHH claimed it was too uncanny for him.  Too weird.  He said he still likes to feel like he is chiseling out something by hand.  He has interacted with a computer for a **quarter of a ==CENTRUY==** to write open source code by typing into it with a keyboard, and it feels weird to talk to it.

Lex went on to say next time you have a _greenfield_ project, something you want to come out good somewhat specific for you, and not have to fuss with it, turn on the mic and just word vomit for 20 minutes.  The models do **surprisingly** well at this.

Today I was feeling the weight of 20 or so PR's opened up mostly by agents awaiting my review.  This whole things sits on my shoulders.  I'm the one that gets the calls when its down, and I'm the one with the final say, but gawd it can be a drain to actually give each a good review and get them landed.

So I started a prompt.  The initial prompt was going to be a sentence or so...

> "write me a script to list all of my prs, prioritize, rank readiness"

This later turned into a 20 minute word vomit that included otel, database, API, sync engine, deterministic checks outside of ci, things like checking version and labeling the pr, pierre diffs (damn these are good) and copilot harness to conduct a preliminary review and auto fixes before I review.

I let that cook in opus 5.5 for about 45 minutes to an hour and went to a meeting, at the end of the meeting I saw it was running in my browser.  In absolute shock I had to hold the meeting over for 10 minutes to share with a coworker.

Both of us were in awe at how well this one shot did some things that we tried to get models to do 6 months ago and they just did a terrible job.  They were all seemingly bad at using azure and required such a well thought out plan that no one had time to just nail something like this in 20 minutes in the morning.

After using it for a day there's things I'm going to change workflow wise to make it better for me.  Things that I would probably simply accept as the truth in a tool, but since I have full access to it I'm going to not pick it and make it glorious. Because I can.  

Rather than bitch how we have to use shitty ass tools we can just ask for good ones.  I know this is not the case everywhere for everything.  I know there's much more complex software.  But the bar is being raised and you can just build shit.  Heck it seems  like all you need to do is ask for it.