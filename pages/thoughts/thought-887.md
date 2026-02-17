---
title: '💭 A quote from Claude'
date: 2025-12-09T13:56:30
templateKey: link
link: https://simonwillison.net/2025/Dec/9/claude/#atom-everything
tags:
  - ai
published: true

---

> damn this is a rough one.  A users entire home directory removed by claude code from an rm command.

``` bash
rm -rf tests/ patches/ plan/ ~/
```

Reading the first half of that command it LGTM.  If you had approved rm, you are hosed.  If  this is inside a larger script its running, you really gotta read close.  This one still feels pretty obvious, but I can imagine some bash doing some nasty things I miss if I read it and understand it let alone glance at it.


I'll take this as a reminder that I really need to be paying full-ass attention to agents, and moving towards a better sandbox for them, something in docker, maybe something like distrobox that is a magic wrapper over podman that just gives you the things you need for what it does.  Something that starts up with access to start web servers, run agentic cli of choice, see project, git commit.  It feels like the right thing has a lot of what distrobox does, but distrobox has too much and would be prone to this using it as I've used it in the past.

[Original thought](https://simonwillison.net/2025/Dec/9/claude/#atom-everything)
