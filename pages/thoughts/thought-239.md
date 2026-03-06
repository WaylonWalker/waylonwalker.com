---
title: '💭 node.js - How to fix npm throwing error without sudo - Stack O...'
date: 2024-04-09T18:21:02
template: link
link: https://stackoverflow.com/questions/16151018/how-to-fix-npm-throwing-error-without-sudo#answer-41395398
tags:
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://stackoverflow.com/questions/16151018/how-to-fix-npm-throwing-error-without-sudo#answer-41395398]]

Its sad that this is not the accepted answer.


``` bash
mkdir ~/.npm-global
export NPM_CONFIG_PREFIX=~/.npm-global
export PATH=$PATH:~/.npm-global/bin
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
