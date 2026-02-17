---
title: '💭 Using stderr/stdout correctly - YouTube'
date: 2025-12-22T15:35:30
templateKey: link
link: https://youtu.be/XDAfpzjBYJQ?t=353
tags:
  - dev
  - cli
published: true

---

> > Yeah there's some basics, you know things you might expect like using standard error and standard out correctly. One thing I'll say on that because I think this is commonly misunderstood, standard error is not for errors, it's for any information that isn't part of the normal output. So you know often times that's warnings and errors, but it might just be progress information. You know anytime that you just need to have something go to the user that's what it's there for." (6:15 - 6:42)

I've definitely done this sin in my own tooling before, and it does make things harder to use.  I think I still take err/out at face value.  I really like the translation Jeff gave here, one is for normal output, i.e. what the user asked for and the other is extra information.  So if I wanted to list something and pipe it into something else, stdout only captures the list, thats it.  if you have a bunch of information about config warnings, showing environment, are you sure questions, none of that is captured.

[Original thought](https://youtu.be/XDAfpzjBYJQ?t=353)
