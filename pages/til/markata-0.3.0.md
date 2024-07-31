---
date: 2022-08-21 13:53:20
templateKey: til
title: markata 0.3.0 is 15-20% faster
published: true
tags:
  - python
  - markata
---

![image from Dall-e](https://images.waylonwalker.com/DALL%C2%B7E%202022-08-21%2015.03.04%20-%20An%20expressive%20oil%20painting%20of%20a%20sprinter%20edging%20out%20their%20component%20at%20the%20finish%20line,%20depicted%20as%20an%20explosion%20of%20a%20nebula.png)

> a sprinter edging out his opponent by Dall-e

It's about time to release Markata 0.3.0.  I've had 8 pre-releases since the
last release, but more importantly it has about 3 months of updates.  Many of
which are just cleaning up bad practices that were showing up as hot spots on
my `pyinstrument` reports

Markata started off partly as a python developer frustrated with using nodejs
for everything, and a desire to learn how to make frameworks in pluggy. Little
did I know how flexible pluggy would make it.  It started out just as my blog
generator, but has turned into quite a bit more.

Over time this side project has grown some warts and some of them were now
becoming a big enough issue it was time to cut them out.

## Let's compare

I like to use my tils articles for examples and tests like this as there are
enough articles for a good test, but they are pretty short and quick to render.

``` bash
mkdir ~/git/tils/tils
cp  ~/git/waylonwalker.com/pages/til/ ~/tils/tils -r
cd ~/git/tils/tils
```

## running tils on 0.2.0

At the time of writing this is the current version of markata, so just make a
new venv and run it.

``` bash
python3 -m venv .venv --prompt $(basename $PWD)
pip install markata
markata clean
markata build
```

cold tils: 14.523
warm tils:  1.028

## running tils on 0.3.0b8

``` bash
python3 -m venv .venv --prompt $(basename $PWD)
# --pre installs pre-releases that include a b in their version name
pip install markata --pre
markata clean
markata build
```

cold tils: 11.551 (+20%)
warm tils:  0.860 (+16%)

## pyinstrument

These measurements were taken with pyinstrument mostly out of convenience since
there is already a pyinstrument hook built in, but also because I like
pyinstrument.

![pyinstrument-markata==0.3.0b8-tils-hot](https://screenshots.waylonwalker.com/pyinstrument-markata==0.3.0b8-tils-hot.webp)

Here is the pyinstrument report from the last run.

## My Machine

This comparison was not very exhaustive. It was ran on my pretty new to me
Ryzen 5 3600 machine.

![neofetch-8-21-2022](https://screenshots.waylonwalker.com/neofetch-8-21-2022.webp)

## The changes

Most of these changes revolve in how the lifecycle is ran.  It was trying to be
extra cautious and run previous steps for you if it thought it might be
needes, in reality it was rerunning a few steps multiple times no matter what.

The other thing I turned off by default, but can be opted into, is
beautifulasoup's prettify.  That was one of the slower steps ran on my site.

## 0.3.0

It should be out by the time you see this, I wanted to compare the changes I
had made and make sure that it was still making forward progress and thought I
would share the results.
