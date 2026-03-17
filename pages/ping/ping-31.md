---
date: 2026-03-16 21:01:44
templateKey: ping
title: Thinking about ai productivity again
published: true
tags:
  - ping
  - ai
  - llm
  - agents

---

Thinking about AI productivity again.  It's allowing massive amounts of work to
get done, to levels that humans cannot physically type out in some cases.  But
not all of this work is necessarily high value work.  Right now I'm working on
one of the biggest PRs to an internal cli library.  Probably the largest PR
I've ever done professionally.  It touches all of the cli, refactors every
command, reaches into the business logic layers to drive deeper separation.  I
reaches into the common layers to drive consistency.  It ensures that every
command (50 or so) has similar flags, supports --plain, --no-color.  It specs
out contracts to ensure that data goes out stdout, any extra goes out stderr.
This makes everything unix pipe friendly. There was quite a bit of research and
prep that went in, that turns out to already be distilled down into clig.dev.
The point is that this is all good work.  It will make the product consistent,
repeatable, expected, and most of all boring.  Most of the time, it will just
work.  Since we did it ahead of a lot of other agentic work on the product its
establishing good patterns for the product moving forward.  But its low value
work.  We wouldn't have likely put humans on this work wholesale and fixed
critical paths as they came up.  Its not cutting cost, selling more product, or
driving critical business decisions.  Yes it's worth it now, but it would not
have bee in the past.

