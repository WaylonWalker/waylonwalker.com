---
title: '💭 4 Tips for Building a Production-Ready FastAPI Backend - YouTube'
date: 2024-12-26T02:42:17
templateKey: link
link: https://www.youtube.com/watch?v=XlnmN4BfCxw
tags:
  - python
  - fastapi
  - webdev
published: true

---

> Great list of 4 tips for running fastapi applications.  

## Keep routes small

Fat routers with all of the logic built in makes them hard to test, hard to refactor, causes lots of duplication, and makes it hard to reuse the business logic code later in something like a cli application.

## Deploy Early

I really like this advice!  He reccommends deploying as early as you can get a healthcheck live in your application.  I've found too many times developers build something that is really hard, or impossible to deploy, when if they had tried to deploy early they would have spotted some easy to fix issues.  This is less important if you are building out of a template that your team commonly deploys from, but very important with new patterns.

https://youtu.be/XlnmN4BfCxw?si=ks1wvmgDyoQLgrv2&t=1093


[Original thought](https://www.youtube.com/watch?v=XlnmN4BfCxw)
