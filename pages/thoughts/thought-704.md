---
title: '💭 Bug: Pypi metadata is wrong (Requires: Python >=3.6) · Issue #...'
date: 2025-06-18T02:04:41
templateKey: link
link: https://github.com/jmcnamara/XlsxWriter/issues/1131
tags:
  - pypi
published: true

---

> pypi yanks suck, they are rare, this one got me today as it was a pinned dependency in my dependency chain.  The latest release broke python 3.6/3.7 (which 3.6 has  been EOL for 3.5 years btw), and it claimed >=3.6.  In order to allow users to still install xlsxwriter without pinning down it needed yanked.  I'm not sure if there was another way around it as pypi releases are immutable, so you cannot fix  

![image](https://dropper.wayl.one/api/file/2ba70753-5723-4b96-8f2b-8090be07d6ad.webp)

> This now has me wondering what the heck is using it with old pythons.

It appears to have broken builds on Canonical/checkbox for ubuntu 18.04.  Checkbox is a device compatibility testing framework.

https://github.com/canonical/checkbox/actions/runs/14644718138/job/41098549191#step:8:125

![image](https://dropper.wayl.one/api/file/6fe3e01b-e180-4d2a-a00c-6b9fab727626.webp)

[Original thought](https://github.com/jmcnamara/XlsxWriter/issues/1131)
