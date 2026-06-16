---
date: 2026-06-16 08:16:58
templateKey: blog-post
title: Prompt Seagulls
tags:
  - tech
published: True

---

I was listening to @syntaxfm this morning and @wesbos said at
[328s](https://www.youtube.com/watch?v=8A2MCNKC_hQ&t=328s) "The prompt seagulls
are driving me nutty".  100% hard agree Wes.  Now I didnt just come off of a
conference where they dropped fable 5.  I've not logged into twitter in months,
but I see it around work.

!!! warning prompt-seagulls

    "Prompt, PR-ompt, promt, PROMT"

## [[ rule-1 ]]

Asking for the prompt as a first question here, is a clear sign you are looking
for magic.  What are the magical incantations I must pass to all master clanker
to get it to do the things that I want.  Wrong, there is no magic prompt to
get impressive results, its people that know and understand their craft that
get amazing results.  They have taste.  They have design in mind, They see
what the end product should be.  They are guiding the model to do what they
want and are not surprised when they get it.


!!! warning prompt-seagulls

    "Prompt, PR-ompt, promt, PROMT"

## process

No one is one shotting their work and kicking up their feet for the other 39
3/4 hours of the work week.  Theres process and methodology to it.  Develop the
right skill files, the right AGENTS.md, instructions, all of the other things.
This puts the ball in your court telling the models how you want these things
done without deep prompting.

!!! warning prompt-seagulls

    "Prompt, PR-ompt, promt, PROMT"

## taste

If you want to build products that humans use and enjoy you must bring some
level of domain expertise.  You should know a bit about your product, your
customer, and how the underlying tech you are working with works.  You should
understand the basics of how websites are built and laid out or how a cli
operates.  If you don't you will inevitably build out something that does the
job, but is not intuitive, does not look good, or feel good, and no one can
figure out how to use it, cause no one, especially these days, no one is
reading the docs.

!!! warning prompt-seagulls

    "Prompt, PR-ompt, promt, PROMT"

## testing

Actually try to use your product, can you?  Can you hit errors?  You probably
should be able to one way or another if you are accepting input from a user
they are bound to be able to input something you cannot just automatically
recover from.  In these cases does it make sense, can you easily see what you
were supposed to do, or why it was wrong?  Does it work on various resolutions?
This goes for about everything these days, web or terminal.  Can you read the
output on a full screen easily?  What about a half screen?  If you're a Philz
coffee mac fanboi with slinging a top of the line 8k display, does it even work
on what a mere mortal might be trying to use?

!!! warning prompt-seagulls

    "Prompt, PR-ompt, promt, PROMT"

##  Good starting point

Ai repeats patterns it finds, its very good at repeating patterns it finds
nearby.  If your existing codebase is not consistent, and riddled with
pitfalls, it will be replicated and be digging larger holes for you to dig up
later.

!!! warning prompt-seagulls

    "Prompt, PR-ompt, promt, PROMT"

##  Old School Checks

Automated checks are a hard requirement for me these days, lint, type check,
secret scan, cve scanning.  All of these things help drive consistency and
helps reliability.

!!! warning prompt-seagulls

    "Prompt, PR-ompt, promt, PROMT"

##  Actually Read Some of the code

Now for the most controversial, un-vibe coder thing... Actually try to read the
code.  You might notice some things.  Somethings like regression testing, and
supporting old versions, old formats, duplicating schemas.  AI is really good
at waking up from a cold state, assuming everything it sees is in production
with real users and writing a lot of code.  It will do things like supporting
the version that it made 5 minutes ago and never shipped for eternity.  Have
your clankers review too, that's also fine, not a substitute for you taking a
look.  Even if you are not finding the tiny bugs here, you will understand more
about how your project works, the direction its going, and be able to catch
directionally wrong shifts.


