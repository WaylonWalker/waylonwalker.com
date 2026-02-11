---
date: 2026-02-11 09:28:02
templateKey: blog-post
title: How To Run 5 Agents In Parallel Feb 2026 Edition
tags:
  - ai
  - llm
  - agentic
published: false

---

Are developers really running 5 agents in parallel?  How the Heck do they keep
up with the changes?  This seems Impossible.

I was listening to Syntax.fm this morning and heard this question, and thought
I'd throw in my take, which is probably pretty similar to Wes and Scott's.

https://www.youtube.com/watch?v=NrBQI9So5lM&list=PLLnpHn493BHHNUfHN5lDf11UD8jQ5Bpzl&index=1&t=99s

## Yes

Yes, developers are running 5 agents in parallel.  It's not that hard it
requires you to shift from thinking about the weeds and seeing the forest see:
[[ pm-not-babysitter ]].  It requires effort and diligence.  Most importantly
it requires planning, it requires agents, it requires tooling.

Is anyone doing this all day?  Probably not. At least not outside of the
startup companies that are building out tools to do this.  Yes there are some,
there's always outliers, but its going to be rare.  To have multiple agents
running in parallel add day you need a lot of tokens, access to good models,
and right now a low to medium risk application.

The big news right now is that Anthropic did what took google two years to do
around 2008 (make a prototype browser render basic web pages) in 2 weeks.  This
took a swarm of agents running, a good plan (the modern browser is probably the
most openly spec'd piece of software ever to exist, so they had a lot to go
on).  But this is also zero risk.  If it doesn't render there are no sales
lost, no traffic accidents, no security breaches, no missed deadlines.

## not with chat

chatbots like chatgpt, are not getting you to run 5 agents in parallel.  Maybe
you take a sip of your coffee while it spits out its response, but you don't
have enough time to jump between many of them.  If this is your experience so
far, I understand how confusing it would be to think that someone is running 5
agents in parallel.  But they are, and they are doing it with tools that are
not chatbots.

## PLANNING

This is the core of what it takes to keep agents running for long periods of
time in Feb 2026.  Agents need something to do, telling them to turn the circle
green, then blue, then to a rectangle, is not it, They will have this done in
seconds. You probably could have done it just as fast and better.

For the plan itself, Send agents off to research.  Agents are not good at
solving problems without a good plan, but this does not mean you have to
tediously write out the plan from scratch.  They are really good a reading docs,
specs, standards, finding them on the web.  Reading your codebase to understand
where and how a bug might be happening.  They are really good at running bash,
browser automation, they can reproduce your bugs for you and provide detailed
logs with expected and actual behaviors in your plans.

!!! Note

    If you are trying to solve a production problem in an environment where you
    have risk and dont want agents running wild in, dont let them in, or scope
    their permissions.  They are really good at understanding they cant access
    and writing a script for you, one that you can review to ensure they are
    gathering facts and not chaning production servers.  Then you can run it
    yourself and paste the results back in.  Sure there are better ways, but
    without any set up this works.

Executing plans, if you have well scoped and documented work for the agent to
do, as of right now they are happy to keep working.  I dont think there yet
exists any sort of best practice here yet.  I prefer to keep it out of the
agent tools plan mode only because that is so deeply tied to the session.  If
you get context poisoning or a shit compaction your session might be hosed
and unrecoverable, I'm sure you could go into the agents session files and do
something to get it back, but I've yet to need one back that bad to really
care.

What you need is a system that agents can access to tell them what to do, a
simple markdown file works, GitHub issues work, I'm sure boards, and kanban
work if it has an api the agent can understand.

