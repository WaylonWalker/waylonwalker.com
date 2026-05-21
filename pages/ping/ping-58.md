---
date: 2026-05-20 20:39:22
templateKey: ping
title: never leave after deploy
published: true
tags:
  - ping

---

I almost for got [[ rules ]] 4 today, rollout when smooth late in the day right
before a vacation day (terrible time to deploy I admit not my clearest plan).
Race conditions are a b****, all around on this one.  The app I was concerned
about won the race to deploy first and was fine by itself, then another app had
a race condition inside itself that killed it
