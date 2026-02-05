---
date: 2026-01-19 20:41:14
templateKey: til
title: format markdown with mdformat
published: true
tags:
  - python
---

I really wish I would have got this right a few years ago. Theres a couple of
flags I had to use to get mdformat to do hard wraps at 80 characters and not
wreck tables. This mix of flags and plugins is workign really well for me so
far.

```bash
mdfmt() {
    uvx \
        --with "mdformat-ruff" \
        --with "mdformat-beautysh" \
        --with "mdformat-web" \
        --with "mdformat-config" \
        --with "mdformat-gfm" \
        --with "mdformat-front-matters" \
        mdformat \
        --wrap 80 \
        --end-of-line lf \
        --codeformatters python \
        --codeformatters bash \
        "$@"
}
```

And as pre-commmit.

```yaml
repos
  - repo: https://github.com/hukkin/mdformat
    rev: 1.0.0  # pin to the version you want
    hooks:
      - id: mdformat
        args:
          - --wrap
          - "80"
          - --end-of-line
          - lf
          - --codeformatters
          - python
          - --codeformatters
          - bash
        additional_dependencies:
          - mdformat-ruff
          - mdformat-beautysh
          - mdformat-web
          - mdformat-config
          - mdformat-gfm
          - mdformat-front-matters
```
