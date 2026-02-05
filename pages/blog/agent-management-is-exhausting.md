---
date: 2026-01-26T14:38:35
templateKey: blog-post
title: Agent Management Is Exhausting
published: true
tags:
  - ai
  - llm
  - agents
---

The state of development in early 2026 is all wrapped around learning how to
manage many agents running in parallel. Everyone's trying to figure out the
workflow.

## The Plan Is Everything

The secret I've discovered is a good, well-defined plan. This could be a
markdown file or a GitHub issue. Agents are actually great at writing these for
you. They'll include reproduction steps, outline changes needed, and structure
the work.

**This** is your opportunity to step in. Read the plan. Look for hallucinations.
Spot where it's going off track. Edit the plan before the agent starts coding.

I had one today where it laid out reproduction steps beautifully, but I could
add context about network requests that completely changed the approach. This
editing phase is what most people are missing right now. Skip it and you'll
watch your agent solve the wrong problem with impressive efficiency.

## The Pace Problem

Here's what nobody warned me about: managing these things is *exhausting*.

Depending on the day, agents move so damn fast. I can barely research, find, and
raise issues as fast as Claude can implement features and fixes. It's like
trying to speedrun a Minecraft seed when you just figured out how to craft a
pickaxe.

## A Different Kind of Work

This stretches a different part of my brain than I'm used to using. I'm learning
new skills around:

- Issue tracking and management at high velocity
- Knowing which models handle which tasks best
- Spotting when a session is about to go sideways from context bloat or bad
  compaction

I had a session yesterday where the context got poisoned with a wrong
assumption. The agent spent 20 minutes building on that false premise before I
caught it. That's 20 minutes of perfectly executed code solving the wrong
problem entirely.

## Worth It, But Hard

I'm not going to hype-bro you and say this is easy or that you're wrong to be
skeptical. If you have the opportunity to work with agents, it's worth learning
proper techniques.

It's not easy. It requires actual management skills, not just
prompting skills. And yeah, I'm tired.
