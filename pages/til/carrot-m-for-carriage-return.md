---
date: 2026-07-12 11:02:28
templateKey: til
title: ^M for carriage return
published: true
tags:
  - linux
  - vim
authors:
  - waylon
  - id: gpt-6-luna
    role: copy editor
    details: "Corrected spelling and grammar with GPT-6 Luna."
editorial_history:
- schema_version: 1
  event_id: bed11545-87fe-4d62-851a-71086e431cc1:pages/til/carrot-m-for-carriage-return.md
  author: gpt-6-luna
  role: copy-editor
  action: edited
  recorded_by: gpt-6-codex
  recorded_at: '2026-10-11T15:07:10.744801+00:00'
  base_commit: 5de74ebc0a1023cf815006572f5cb63816ad81db
  commit: d3b1fe7083dbeffea0e28578ec8c1d0b2833e478
  path: pages/til/carrot-m-for-carriage-return.md
  content_digest: sha256:b9e2a6ec8ba787ca916c2207bade4c6e0960ac114bd9177ec603bea0bd20e3e6
  digest_version: editorial-v1
  file_url: https://github.com/waylonwalker/waylonwalker.com/blob/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478/pages/til/carrot-m-for-carriage-return.md
  diff_url: https://github.com/waylonwalker/waylonwalker.com/commit/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478#diff-6053d57b59e5efe80f07ae40847cefe1fbec5d0aa59d54834a212916d5978f2c
  summary: Imported GPT-6 Luna copy edits after the owner confirmed exclusive authorship
    of these post diffs.
---

I don't run into Windows file endings very often, so when I see little `^M`'s
all over your file, I think "shit I know what these are and can't remember"
They represent the Windows carriage return.

## Linux vs Unix Line Endings

The difference here is that Unix uses `\n` and Linux uses `\r\n`, going all the
way back to the typewriter it represents the two keys that a typist would have
to press to get a new line and return the carriage back to the beginning.

## Vim/Neovim

When I open up a file and see this garbage all over, it's not cozy, I want them
gone, I don't want them all over my editor.  I'm not sure what this would look
like on Windows, I haven't been able to afford a Windows machine in years, but
its gross on my machine.

![131d6463-bcbb-4ee8-80aa-bb7355915eb9.webp](https://dropper.waylonwalker.com/file/131d6463-bcbb-4ee8-80aa-bb7355915eb9.webp)

Remove them with a substitution command from normal mode.

``` vim
:%s/\r//g
```

![4c84c556-5d96-4df1-9324-217dfb2f951a.mp4](https://dropper.waylonwalker.com/file/4c84c556-5d96-4df1-9324-217dfb2f951a.mp4)
removing carriage returns with a substitution command

