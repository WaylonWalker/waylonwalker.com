---
title: '💭 One Script Tag Just Pwn''d Over 100,000 Websites - YouTube'
date: 2024-06-28T16:08:20
templateKey: link
link: https://www.youtube.com/watch?v=ILvNG1STUZU&t=286s
tags:
  - webdev
published: true

---

> Supply chain attacks are so big these days engineers definitely need to take these into consideration.  It's wild that such a simple attack vector hit some really big applications.  This particular vector is so easy to avoid. You are already hosting web content, just curl the file and self host the script, then you own it.  That eliminates this attack vector all together, but doesn't completely remove supply chain attacks, the js file can still hit external apis internally.

> What I see has happened in this case is that the owner of the domain polyfill.io changed. so anyone who directly linked to them got a malware injected script used.  

I can only imagine the number of applicatons that are not even being maintained anymore getting hit by this.  TLDR, if you are taking something to production, where you are goind to deploy it and let it run, host the js yourself.  these cdns are great for prototyping, but tread with caution.

[Original thought](https://www.youtube.com/watch?v=ILvNG1STUZU&t=286s)
