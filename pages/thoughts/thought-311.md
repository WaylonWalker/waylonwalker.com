---
title: '💭 Episode #323 Best practices for Docker in production - [Talk P...'
date: 2024-06-16T00:55:12
template: link
link: https://talkpython.fm/episodes/show/323/best-practices-for-docker-in-production
tags:
  - python
  - docker
  - thoughts
  - thought
  - link
published: true

---

![[https://talkpython.fm/episodes/show/323/best-practices-for-docker-in-production]]

Great listen for anyone interested in productionizing python code with docker.  Itamar brings up some 


Don't trust base images for security, upgrade your packages.  Vulnerabilties become published and solved giving the bad guys istructions how to wreck your day and these fixes wont come to your docker application for up to two weeks due to image build tatency.

For job based containers pre-compile your pyc for faster startup.

Alpine linux is probably not what you want for python.  Many packages such as postgres ship pre-copiled binaries that work for most linux distributions wich use glibc, but alpine uses musl so the binaries will be incompatable requiring you to need to install a bunch of build dependencies.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
