---
title: '💭 python-build-standalone/.github/workflows/release.yml at main ...'
date: 2025-02-17T23:21:05
templateKey: link
link: https://github.com/astral-sh/python-build-standalone/blob/main/.github/workflows/release.yml
tags:
  - just
published: true

---

> Astral uses just in CI, kinda cool to stumble into this setup in the wild.

``` bash
run: just release-run ${{ secrets.GITHUB_TOKEN }} ${{ github.event.inputs.sha }} ${{ github.event.inputs.tag }}
```
And her is the accompanying justfile.  you can see how it accepts arguments, and starts calling out to other just recipes.

``` justfile
release-run token commit tag:
  #!/bin/bash
  set -eo pipefail

  rm -rf dist
  just release-download-distributions {{token}} {{commit}}
  datetime=$(ls dist/cpython-3.10.*-x86_64-unknown-linux-gnu-install_only-*.tar.gz  | awk -F- '{print $8}' | awk -F. '{print $1}')
  just release-upload-distributions {{token}} ${datetime} {{tag}}
  just release-set-latest-release {{tag}}
```

[Original thought](https://github.com/astral-sh/python-build-standalone/blob/main/.github/workflows/release.yml)
