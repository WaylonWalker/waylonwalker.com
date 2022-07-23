--
date: 2022-07-23 12:05:55
templateKey: blog-post
title: The one reason I switched to arch
tags:
  - linux
  - arch
status: published

---

The community, that's it, end of post, roll the credits.

## I'm a tinkerer

I am a tinkerer, I am not going to run a stock desktop manager, mostly becuase
that's just not how my brain works.  I need to tweak everything to fit my
needs.  Grantid I have not spent much time in many full fledged linux desktop
environments.  They are far more customizable than windows ever will be, I
absolutely love that about them.  Inevitibly I end up in a situation where I
hit a wall, it just won't do what I want it to do, or my lack of understanding
what came wtih it holds me back.

## minimal

I love minimal installs.  I love just building up my system from the bottom up
with things that I like, I understand, and that I can script.

## I'm a noob

I spend a lot of my time in the terminal.  I'd like to think I know how to use
a linux command line for software development really well, but there are a lot
of things that I still dont know all that well, mostly because I don't need to.

## The AUR
_Arch's **community** maintained repo_

Now by far this is the thing that really kicked me over the edge and made arch
feel like something that I needed to use.  While on any Debian based distro it
was inevitible that I would stumble accross a bug that was fixed in a newer
version, not available in the standard repos, want new features that are not
available in the standard repos, or want software that is not packaged into one
of the standard repos.

This makes creating scripted installs/updates difficult.  I have to pull
releses from github, or some random website, or clone and build packages
myself.  It's not too hard, but since I am the only one that maintains my
personal install script it's inevitible that something changes in the build
process or release on something and breaks it over time.

PPA's are not the same.  Well maintained ppa's are fine, but many of them are
not.  PPA's are just deb files that someone hosts and their quality can be hit
or miss depending on if the maintainer still uses it or not.  While the AUR is
not completely absent of stale packages it's rolling release nature tends to
keep them always up to date, and when it doesn't the community helps out by
flagging these packages in the AUR and upvoting maintained packages.

## The Arch Wiki

I have underutilized the arch wiki in the past, but dang it has some really
good guides.  For me (at my level) they edge on being to brief, generally I find wiki's
overly versose and hard to find what you are looking for.  The arch wiki gives
you what you need and no more.  The articles and forum really have answered
many of my questions and depened my understanding of linux.

## I am learning

While I am still a noob to a lot of this I am learning, and a combination of
the minimal install with the arch wiki have really helped me learn a lot about
lower level things like partitioning, grub, systemd, xorg.  On most other
systems these were just taken care of out of the box.

## Arch is not hardcore

I think there is an old sentimate that arch is for hardcore users only.  Their
typical install process really gatekeeps it this way, but there are other
installers such as `archinstall`, which I used and now ships with the arch iso,
that make it not much harder than any other distro.

If you are a tinkerer who likes to try different things, likes to set you
machine up just the way you like it, and script it, arch really feels much
easier to do this with.  I'd even stand behind it being a distro for noob
tinkerers.

## Does distro matter??

Idk if it really matters all that much in the end, but the community behind the
aur and arch wiki make setting up an up to date machine so much easier than on
any lts based distro.
