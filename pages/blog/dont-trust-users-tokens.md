---
date: 2026-01-14 19:49:43
templateKey: blog-post
title: Dont Trust Users Tokens
tags:
  - python
published: True

---

User states: Upon picking up an old project and trying to install pip says
"cannot find a version to satisfy"

I've got this, I've had this a hundred times before it's a python version, a
rogue package, maybe a yank from the pinned deps.  I pop open the project get
us on the same commit.  I get a different error, make a few updates and we are
good, except the user gets the same error from the start.

They never saw the error I did, and my fix did not magically resolve their
error.  We circle all the things it could be for hours.  I consistently wipe my
venv, and recreate with ease, send them the commands I ran to no avail.
Something is up and I can't put my finger on it.  We've checked all the things
and inched as close as we can to running everything exactly the same.

* Os
* python version
* Network vpn
* uv version

Nothing makes any sense.  Finally I throw in the towel, is it the artifact
server.  I forge a token and give him one to borrow.

**BAM** it works, like magic.  The first sign of progress.  Then he mentions.

> Huh that's odd cause I just got mine this morning

Failing to mention this any earlier that getting a new token for a service and
it completely borked it!  I get it though, the error was very oddly presented
and not easy to see why

There it was all along, looking back in the logs I see his redacted token going
to the wrong registry. One that does not include our packages, everything makes
sense now. The reason it couldn't find a version to satisfy was not a python
version, os version, package conflict, it was that it couldn't find a fucking
version of the thing to begin with.

All this to say, don't trust users tokens, save your time and just get fresh
ones with them.

<Redacted> if you read this it's all cool, like I said it's all part of the
job, no harsh feelings, at least we got a good story out of it right!
