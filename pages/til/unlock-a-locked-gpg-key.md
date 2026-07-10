---
date: 2026-07-10 14:26:00
templateKey: til
title: unlock a locked gpg key
published: true
tags:
  - python

---

I ran into an issue where my `pinentry` was unable to connect, blocking me from
doing commits.  You can use this to continue signing commits.

``` bash
export GPG_TTY=$(tty)
gpg-connect-agent updatestartuptty /bye

printf test | gpg \
  --local-user 9A47900E81415D65C32C630066E2BF2B4190EFE4 \
  --pinentry-mode loopback \
  --sign >/dev/nul
```
