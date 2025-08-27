---
date: 2025-08-27 10:10:51
templateKey: blog-post
title: I'm Out On Agents
tags:
  - python
published: True

---

Its the year 2025 and we are only a few years into having 6 months to live
before ai takes our jobs, and the big push right now is agents, managing
agents.  I will fully concede to I'm not doing it right, or a future state gets
better than where we are right now, but right now they kinda suck.

!!! Transparency
    
    I'm sitting offline right now as I write this, These are my feels, no
    research, no links, no ai, just vibes.

## Chat

Chat is what really kicked off ai uses and goes back as old as computers, but
it always sucked.  Then chatgpt rocked the world with the biggest launch day in
history and showed us that it could actually be pretty good.  Unethically
trained on everything they could get their hands on, burning cities worth of
electricity to train, and keep training to stay ahead of the competition.  It
does a damn good job.  There are tells, and if you see enough of it there is a
lot that turns to slop, but if you had never seen it before, there is no way
you would assume that it was not a computer.

It does a damn good job at being average, it can do what seems like everything
not related to security and authentication at a pretty average level.  This is
its super power.  Whenever you are trying to bridge between something you know
and something new, you can get a pretty good answer, and likely spot the bs in
what you know.

## Agents

Now that our models have gotten better, hardware has gotten bigger, better, and
a lot more of it, we can really expand context windows really wide.  With that
brought the use of agents, these tools get context from sources on their own
and often are given read/write access to your computer.  Depending on the model
these things will branch out to make small changes that look no worse than a
formatter on every goddam line of your codebase.  Except they are not a
formatter, they are not backed by ast checks.  They do not have any guarantees.

> They take the fun out of creation.

The emphasis now becomes on the code review.  All you have to do is ask it to
makes changes for you.  Bring in your expertise of what changes should be next,
or even just punt to asking it what comes next.  I've yet to talk to someone
that is diligent enough to read everything it spits out in excruciating detail
to the point that it does not cause significant issues.

You see here is the thing, its average.  With a little bit of context it can do
average work.  It is not an expert.  On the surface this feels fine, making
crud endpoints has been done for decades, and average developers crush these
things every day no problem.

> It's Average at best

You know what is not average?  Your knowledge of the use case you are solving.
You may not feel like an expert, but given that there are likely about 5 people
working in your codebase, you are a fukin expert at that thing.  The average
person off the street takes time to onboard, often months, or years for someone
to really understand the business you are working in.  These things don't have
that.

## I'm not letting it in shit that I care avout

I was early to the game to codeium, even used the predecessor for awhile, I was
early to chat gpt, I was early to windsurf and the possibilities that agentic
ides brought.  I will be late on letting agents touch my production code bases.
The few times I've tried for changes that seem easy enough, but more work than
what I want to do at the time, I've regretted it.  It's only left behind a mess
that it cant deal with anymore, runs in circles trying to solve any problem,
and I'm left with shit that feels like a house of cards that breaks anytime you
touch it.

## I will continue to POC

As much of a mess as these things, make they are super useful to vibe code
ideas, move quickly and try different approaches to a problem.  They let you
make a proof of concept that you can get in front of team mates, bosses, or
users.

Honestly I still prefer the chat interface.  It feels like a nice balance of
using my brain, and knowing that I am punting on something.  Do I need to know
the whole `ffmpeg` interface to grab a thumbnail for my webapp, no, would I
actually like to learn it someday, yes, but I don't need to right now I just
need a goddamn thumbnail.

For the most part I am still slotting these things into the codebase myself,
but occasionally I have it do an entire module, and even more rare I pull out
agents and have it do all the work.  The further away from the code I get, the
less I care about it and just want it done.

## I will laugh at this post in 2 years

The way I see it agentic coding is not here to stay, it sucks.  There is one
two ways to go this was a blip in the radar that we laugh at for giving ai
companies all our data for free so they could fuck up our products.  Or they
actually get pretty good and we all become architects that peek at the code if
we really need to.  I think for the second to become true its going to take a
lot of time, consumer hardware will need to catch up, local llms will need to
work a lot better than they do now.  Even if we still need to call out to the
big boys for some heavy work getting the context right for them locally would
make a huge difference.  Currently local llms are too slow and dumb.

So will this bubble pop or explode, we can only wait to find out.
