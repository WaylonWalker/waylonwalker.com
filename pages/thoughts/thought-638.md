---
title: '💭 No docs, no bugs'
date: 2025-05-22T19:50:40
template: link
link: https://simonwillison.net/2025/May/22/no-docs-no-bugs/#atom-everything
tags:
  - dev
  - thoughts
  - thought
  - link
published: true

---

![[https://simonwillison.net/2025/May/22/no-docs-no-bugs/#atom-everything]]

> Bugs exist when your test-enforced implementation fails to match the behavior described in your documentation. Without documentation a bug is just undefined behavior.

This is quite an interesting thought, so does this mean that, none of my undocumented side projects have bugs?  no I think there is still some implied behavior that naming things covers.  a function `get_bucket_contents` implies doing something wtih s3, getting stuff from your local filesystem or crashing would be considered a bug.  I think the argument here is that if I start mining bitcoin when you call `get_bucket_contents` and I have not documented it that this is a feature not a bug.  If I were to take this a step further, now do I need to document that this does not also start a bitcoin miner?  maybe this is more of an unwanted feature than a bug, I'm convincing myself more and more.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
