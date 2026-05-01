---
date: 2026-04-29 11:05:39
templateKey: til
title: testing copilot model flag
published: true
tags:
  - cli

---

Today I found a way to test model syntax, cause the clankers always get the
exact model name that copilot wants wrong.

``` bash
copilot --model claude-sonnet-4.5 -p "Reply with OK" --allow-all --no-ask-user -s
copilot --model gpt-5.4 -p "Reply with OK" --allow-all --no-ask-user -s
```
