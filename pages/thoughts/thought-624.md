---
title: '💭 THE STANDUP - Coding DIRTY Episode 7'
date: 2025-05-07T18:00:09
templateKey: link
link: https://www.youtube.com/watch?v=hbEWfC4k-Gw
tags:
  - dev
  - testing
published: true

---

> > "Gradually roll out your releases to a small group of people"


~ roughly what prime said (I'm listening live)

This really hit home with me, tests can be so good at making sure that we dont repeat bugs and that laser focused things work, tests are generally small and focused, but this does not replace some sort of integration testing.  These days very few things are written as a monolith, and hence there are a lot of interactions that really need to play well together accross various systems.

They call out Crowdstrike here, which took down the world blue screening critical windows systems everywhere in 2024.  It was revealed that a small changed was rushed through and skipped critical rollout paths since it seemed like a small change.  Crowdstrike also runs at a super low kernel level of access and a small memory bug can kill the system.

[Original thought](https://www.youtube.com/watch?v=hbEWfC4k-Gw)
