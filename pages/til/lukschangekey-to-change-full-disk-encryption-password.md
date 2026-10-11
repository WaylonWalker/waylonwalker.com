---
date: 2026-09-01T21:51:16Z
templateKey: til
title: "Lukschangekey to change full disk encryption password"
tags:
  - "linux"
published: true
authors:
  - waylon
  - id: gpt-6-luna
    role: copy editor
    details: "Corrected spelling and grammar with GPT-6 Luna."
editorial_history:
- schema_version: 1
  event_id: bed11545-87fe-4d62-851a-71086e431cc1:pages/til/lukschangekey-to-change-full-disk-encryption-password.md
  author: gpt-6-luna
  role: copy-editor
  action: edited
  recorded_by: gpt-6-codex
  recorded_at: '2026-10-11T15:07:10.757241+00:00'
  base_commit: 5de74ebc0a1023cf815006572f5cb63816ad81db
  commit: d3b1fe7083dbeffea0e28578ec8c1d0b2833e478
  path: pages/til/lukschangekey-to-change-full-disk-encryption-password.md
  content_digest: sha256:b5cc854ea1368015bb0775a9d83d1a8b33c9bbce2b4837e5d335743ba178d21f
  digest_version: editorial-v1
  file_url: https://github.com/waylonwalker/waylonwalker.com/blob/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478/pages/til/lukschangekey-to-change-full-disk-encryption-password.md
  diff_url: https://github.com/waylonwalker/waylonwalker.com/commit/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478#diff-c22867127151b674378bcca9f32f4a40963c8206f41415b24e3fbe087ed65c94
  summary: Imported GPT-6 Luna copy edits after the owner confirmed exclusive authorship
    of these post diffs.
---

I'm playing with omarchy on an old laptop and decided I want to share it with my kids without sharing what I also set up as my sudo password.

``` bash
lsblk -f
```

Look for the one labeled crypto_LUKS

``` bash
sudo cryptsetup luksChangeKey /dev/nvme0n1p2
```

Then you will be asked for your sudo password, previous full disk encryption password, then the new one twice.

Now my laptop can be shared without sharing my private `sudo` password.