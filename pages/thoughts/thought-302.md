---
title: '💭 argoproj/argo-events: Event-driven Automation Framework for Ku...'
date: 2024-06-09T14:30:26
template: link
link: https://github.com/argoproj/argo-events?tab=readme-ov-file
tags:
  - k8s
  - kubernetes
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/argoproj/argo-events?tab=readme-ov-file]]

Argo events is an event driven automation framework for kubernetes that can create kubernetes objects among other things based on events.  I've been using native kubernetes cronjobs to kick off jobs based on a cron trigger.  

For instance I am running reader.waylonwalker.com every hour, to rebuild the site and re-deploy it.  It takes about two minutes to fetch every rss feed, so this is a nice application of a job compared to a web server fetching the feeds live.  Now my posts may be up to an hour stale but they load fast.

Argo events takes event drien architecture to the next level allowing to be triggered by many more things, and do many more things than creating a cron job.  I'm definitely thinking about dropping this in my homelab.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
