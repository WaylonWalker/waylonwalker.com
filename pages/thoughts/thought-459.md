---
title: '💭 Switching from virtualenvwrapper to direnv, Starship, and uv'
date: 2024-12-24T03:30:57
template: link
link: https://treyhunner.com/2024/10/switching-from-virtualenvwrapper-to-direnv-starship-and-uv/
tags:
  - python
  - uv
  - thoughts
  - thought
  - link
published: true

---

![[https://treyhunner.com/2024/10/switching-from-virtualenvwrapper-to-direnv-starship-and-uv/]]

I've kinda fallen out of using direnv now that a lot of my projects use hatch, I generally just hatch shell into them.  I just need to make sure I go through all of them and make my installer uv.  Now I've been thinking about making uv my only needed dependency to run a python project and leaning more to something like `uv run --with . uvicorn myapp --reload`

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
