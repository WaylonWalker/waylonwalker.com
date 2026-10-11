---
title: Stop Making TUIs
date: 2026-08-21T17:15:51Z
published: true
draft: false
tags:
  - cli
  - tui
  - ai
template: link
image: ""
url: "https://simonwillison.net/2026/Aug/21/stop-making-tuis/"
authors:
  - waylon
  - id: gpt-6-luna
    role: copy editor
    details: "Corrected spelling and grammar with GPT-6 Luna."
editorial_history:
- schema_version: 1
  event_id: bed11545-87fe-4d62-851a-71086e431cc1:pages/link/stop-making-tuis.md
  author: gpt-6-luna
  role: copy-editor
  action: edited
  recorded_by: gpt-6-codex
  recorded_at: '2026-10-11T15:07:10.482577+00:00'
  base_commit: 5de74ebc0a1023cf815006572f5cb63816ad81db
  commit: d3b1fe7083dbeffea0e28578ec8c1d0b2833e478
  path: pages/link/stop-making-tuis.md
  content_digest: sha256:4bcb057943926f50dfe9db49a2dd4000cc454a515622e1305a593b20b93bfb7c
  digest_version: editorial-v1
  file_url: https://github.com/waylonwalker/waylonwalker.com/blob/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478/pages/link/stop-making-tuis.md
  diff_url: https://github.com/waylonwalker/waylonwalker.com/commit/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478#diff-438ccbebd605c80668355fa9da0fe41d72f62009386921d20867aa11ddc5e29c
  summary: Imported GPT-6 Luna copy edits after the owner confirmed exclusive authorship
    of these post diffs.
---

Hard to argue this so hard here.  For me it's convenience.  I work from a terminal.  Most things that are real work get done there, so this provides a convenient proximity to real work.  If it's a developer tool for me to use alongside development work I prefer a tui if it can be done in a text interface.

CLIs are different.  CLIs provide a great interface into automation, scripting, agent use, interop from two things no one else uses together.

Alternatively to the argument for agents making ==real== user interfaces _easy_ I'm going to argue if that's the case you should have your backend logic hooked into all the interfaces a user could want, CLI, TUI, HTML, and REST/HTTP API.

I honestly feel like the training data for a good tui just isn't there and agents default to making bad TUIs.