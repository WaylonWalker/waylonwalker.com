---
date: 2026-07-10 14:26:00
templateKey: til
title: unlock a locked gpg key
published: true
tags:
  - python
authors:
  - waylon
  - id: gpt-6-luna
    role: copy editor
    details: "Corrected spelling and grammar with GPT-6 Luna."
editorial_history:
- schema_version: 1
  event_id: bed11545-87fe-4d62-851a-71086e431cc1:pages/til/unlock-a-locked-gpg-key.md
  author: gpt-6-luna
  role: copy-editor
  action: edited
  recorded_by: gpt-6-codex
  recorded_at: '2026-10-11T15:07:10.764044+00:00'
  base_commit: 5de74ebc0a1023cf815006572f5cb63816ad81db
  commit: d3b1fe7083dbeffea0e28578ec8c1d0b2833e478
  path: pages/til/unlock-a-locked-gpg-key.md
  content_digest: sha256:58605376910b31b540f12aa1f56af8ca6a95cda11a4962d8cbd5189cbcd752bf
  digest_version: editorial-v1
  file_url: https://github.com/waylonwalker/waylonwalker.com/blob/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478/pages/til/unlock-a-locked-gpg-key.md
  diff_url: https://github.com/waylonwalker/waylonwalker.com/commit/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478#diff-cbaff2d970dc60e4c668038351dfb0b2fc9116751c4c46234f5bf46ad72ee315
  summary: Imported GPT-6 Luna copy edits after the owner confirmed exclusive authorship
    of these post diffs.
---

I ran into an issue where my `pinentry` was unable to connect, blocking me from
doing commits.  You can use this to continue signing commits.

``` bash
export GPG_TTY=$(tty)
gpg-connect-agent updatestartuptty /bye

printf test | gpg \
  --local-user 9A47900E81415D65C32C630066E2BF2B4190EFE4 \
  --pinentry-mode loopback \
  --sign >/dev/null
```
