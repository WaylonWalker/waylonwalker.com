---
date: 2025-09-02 19:44:20
templateKey: blog-post
title: When To Vibe Code
tags:
  - ai
  - llm
published: True

---

I enjoyed this post from Theo and think it deserves re-iterated, revisited, and
to remind myself of some of these things.

<https://youtu.be/6TMPWvPG5GA?si=guQem4R8dLOMBntP&t=1356>

## The skill/read spectrum

![screenshot-2025-09-03T00-32-08-321Z.png](https://dropper.waylonwalker.com/api/file/209e62d2-4687-4ce0-880b-c7375867f616.png)

The first diagram describes that there has become a spectrum of agentic coding
from vibe coding where you don't ready anything, to looking at everything in
detail, across a group of people who don't have a clue what the code says to
people who could do it way better if they took the time.

### The importance spectrum

He argues here that its ok to bounce between A,B, and D, but C becomes
dangerous.  I'd argue that he brought up a 3rd spectrum that is important later
on, "how critical is this".  I think the I don't know, don't care, didn't read,
but the thing did its job is quite fine, but don't know, don't care, mission
critical is the main issue we are seeing with agentic coding, primarily in the
didn't read but critical Zone.

## The Rules

This is the list that prompted this post, I think it serves as a good reminder
when you should care a bit more.

![screenshot-2025-09-03T00-24-17-121Z.png](https://dropper.waylonwalker.com/api/file/3093511a-f1fd-49cb-8152-bc6c60cc80e2.png)

## You still need to know how code works if you want to be a coder

If you want to get good, you need to put in the reps, do the practice, learn to
debug the strange looking error messages and not just pass them to ChatGPT.

## There's a lot of code worth having that is not worth writing or reading

As professionals we have a lot of code that we read more than we write, will
get executed millions of times over the next 10 years that its in service, pay
close attention to this and probably set aside the llm.

We also write a lot of that is ran only a few times, maybe its a special
report, or a shell script to bootstrap something.  It might be a POC service
that you build out only ever on your machine, you get your idea out in front of
users or try it yourself and find the mistakes before you spend weeks building
it yourself.

## you can't be mad at vibe coding AND be mad at left-pad

This one is interesting that he was very strongly for.  The idea is that no one
ever reads the code from libraries they use, or the diffs of new versions
(outside of google where everything is literally vendored into the monolith).
If you don't care about all of those dependencies, you cannot get mad at vibe
coding.

I'll argue here a smidge, but I agree with the premiss.  Left-pad was probably
written by someone smarter than average.  It was definitely used by **far**
more people and projects, therefore was battle tested to no end.  This was the
real reason this stuff got in everywhere.  People are probably not good enough
to catch all the odd edge cases for `js`, especially if front end is not their
specialty.

## [Vibe code is a type of legacy code](https://blog.val.town/vibe-code)

Vibe coding is a type of legacy code, but as a type of debt that we opt into,
not one that has accumulated over time and we have opted not to take care of.
Both are types of code that no one reads, no one remembers existed.

> When someone needs to change legacy code they don't, they take a hammer to it
> and rewrite it from scratch.

## If the tools are better than you, stop using them

Theo has a good example here.  Critial business components to his businesses
have switched to using `Effect`.  It solves async issues with ease, but melts
the brain of anyone seeing it for the first time.  He admits that he does not
code as much anymore and thus he sucks at it, but knows that if he is ever to
learn it one bit he must turn off the LLM and put in the work to do it himself.

You will not get any better at this by copy pasting from ChatGPT.  It is too
easy to put your brain aside, paste error messages, and copy the reponse in. Or
worse with agents tell them `fix this`.  Unlike the days of Stack Overflow, you
had to understand your problem well enough to search it.  You had to understand
the answers enough to integrate the solution, you had to understand if the
solution was even for your problem in the first place.  There was much more
brain work that had to happen even then when the answers were basically given
to you.

## Fin

Lastly Theo does not bring this rule, up, but if you are writing text for
humans to read, you shall not copy paste from ChatGPT without thoroughly
editing and reading for yourself first, this is considered [[ ai-slop ]] and
you should be ashamed.
