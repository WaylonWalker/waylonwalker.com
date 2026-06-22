---
title: 'AIs aren’t good rule followers'
date: 2026-04-14T15:16:11
template: link
link: https://x.com/unclebobmartin/status/2044065822067282396
tags:
  - llm
  - ai
  - thought
published: true

---

![[https://x.com/unclebobmartin/status/2044065822067282396]]

I've gotta agree with bob on this one, the first thing I did to my biggest brownfield project I wanted to use agents on BEFORE they did work was a hardened pre-commit.yaml, ci, hardened type checking and linting. SECOND get rid of bad inconsistent patterns, let them replicate consistency, force them to pass checks.  Agents will follow all of your markdown suggestions _most_ of the time, enough for you to become complacent if you let it.  They are goal seeking, if you put them to a task you thought was possible that is not given your constraints, they will try to find a way given enough tokens.  I dont see this ever changing, its one thing that makes them great, it just needs to be kept in check.
