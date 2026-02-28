---
title: '💭 We shouldn’t have needed lockfiles @ tonsky.me'
date: 2025-08-06T20:11:31
template: link
link: https://tonsky.me/blog/lockfiles/
tags:
  - dev
  - thoughts
  - thought
  - link
published: true

---

![[https://tonsky.me/blog/lockfiles/]]

I wholeheartedly agree that packaging is broken, semver is broken, expecting much better from a system of oss that is built on top of volunteers, passion projects, nights and weekends is a fools errand.  With that I disagree that we we dont need lockfiles.  Maybe its Nikki's experience in java and my lack that puts us on this opposite spectrum, but without lockfiles the world changes underneath us as we release.  One small change to your source can introduce a whole set of new features/bugs that you did not plan on without a good locking system.  It can also cause you to need to do dependency resolution at application build time and not ahead of time.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
