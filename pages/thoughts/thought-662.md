---
title: '💭 From Prisma Founder to LiveStore: Building local-first apps wi...'
date: 2025-05-31T20:58:05
template: link
link: https://www.youtube.com/watch?v=aKTbGIrkrLE&t=3260s
tags:
  - database
  - event
  - recommended
  - thoughts
  - thought
  - link
published: true

---

![[https://www.youtube.com/watch?v=aKTbGIrkrLE&t=3260s]]

This talk about live store really made me think about database transactions in a new way.  They are talking about live-store, and the complexity of distributed applications like a notes app with the ability to go offline and continue working.  The complexity of resyncing each instance is not simple, conflict resolution accross all the possible installs that may or may not even be online is a really hard problem.  They go deep on discussing an event driven paradigm that is driven off of a log of events and how this changes how we deal with databases.  Using the event log as the source of truth we can do things like forget about database migrations, we can replay all of the events onto a new database.  Its very interesting to rethink in terms of a log system that speaks in terms of understandable events (not table operations) as the source of truth for an application.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
