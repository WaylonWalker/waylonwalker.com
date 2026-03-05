---
date: 2026-03-04 20:47:37
templateKey: blog-post
title: I Built A Tmux Session Switcher
tags:
  - cli
published: True

---

I've been thinking about this for awhile now.  For years now, fuzzy pickers and
last session have been my go to.  They have served me well.  I can typically
only keep so much in my head anyways.  I'm often doing a hub and spoke pattern
between main project, notes, and infra repo, maybe two projects.  Don't get me
wrong, I regularly run with a dozen or more sessions running at a time, but
only two to three are in my immediate context at any point anyways.

## The Design
_harpoon for tmux_

SIMPLE, FAST, thats of upmost importance, what I want are sessions that I can
press a hotkey followed by one more keystroke, currently any left hand letter
can be assigned in order of importance from middle row, top row, bottom row.

I added this binding to my tmux config.  Now I can press `c-a a` to go to the
first session, `c-a s` to go to the second session. `c-a` and pause to think
j/k to navigate, space to pick up a session and move it, x to kill it.

``` bash
bind-key -n c-a popup -E '~/go/bin/tgo'
```

## Enter the agents

Now with agents doing more and more work, and cooking for longer periods this
is not cutting it, I'm often swapping through a lot more sessions, I've got
more projects sitting in more phases between research, implementation, fully
orchestrated agents, and sessions that need their hand held to get things
right.

![](https://dropper.waylonwalker.com/file/7c5765a0-126d-430a-ad86-eb83eb440e1b.webp)
Image of the `tgo` tool in action, I'd show you a video, but its not really
that interesting, it just flashes up and goes to the next session as fast as
you can press the key.

## Made with gpt-5.3-codex and gpt-5.1-codex-mini

Idk how much it cost, it barely touched my $20/month weekly token allowance.
I've been thinking about it for awhile and decided today was the day to pull
the trigger on something and get it started, worst case I throw it away.  It
took the agents about 7 minutes to implement a working version with broken ci
that it later fixed.

I've typed far more characters and put more thought into this post than the
tool itself, that where we are these days I guess.

See the session that made `tgo` [[ses-3444b09b1ffexter3elfg5qqtg]]

## Should you use it?

You can its there for anyone to use, go for it, there's an easy to download
binary.

It's all vibe coded slop that you could probably do a better job doing in a
cave with scraps anyways.  Take inspiration and make one that works for you.
