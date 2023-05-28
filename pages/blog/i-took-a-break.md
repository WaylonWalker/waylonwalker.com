---
date: 2023-05-27 19:45:12
templateKey: blog-post
title: I took a break
tags:
  - personal
status: published
---

Life comes in waves, and sometimes you need to set down some of your projects to
focus on others. For the first part of 2023 I've really had a lot of family
stuff to focus on, we also are pretty new homeowners and are still trying to
get our new to us house cleaned up and modernized.

## Side Projects

You can see in my growing list of
[repos](https://github.com/WaylonWalker?tab=repositories) that I have poked
around on quite a few side projects over the past few months. This has been
quite relaxng to me, mostly things that I use to learn from, but also a
lot that are tools and things I use that bring me joy.

## Pydantic

I haven't wrote about it at all yet, but I have really been starting to lean
into pydantic on all of these side projects. I have really been enjoying the
type system. A good friend [@pypeaday](https://twitter.com/pypeaday) got me
hooked and we have been throwing around this phrase that he learned from a math
professor "Make it So". The idea boils down to leveraging pydantic to
make all the values you want to exist up front, or fail validation, then have
no more checks scattered all over your code.

I've really been deleting a bunch of logic from places within my code and
putting it right in the pydantic models. This gives me one place I will know
to look for it rather than many places some logic might come up. Then when it's
time to do things, the logic is typically a bit simpler.

## Markata

[Markata](https://markata.dev) continues to be my biggest side project.
Currently its it a big refactoring phase to get everything moved into pydantic.
It's been quite awhile since I've had a release, but there has been steady
progress going into the `pydantic` branch.

## AI

Ai is really hot in 2023. I've been trying to keep my finger on the pulse and
play with it. I tried to make a library to interface with openai
[lockhart](https://github.com/waylonwalker/lockhart). It was a cli where you
can store prompt template. I also made a full text adventure game with a new
library from prefect.io, called marvin. [marvin star wars text
adventure](https://github.com/WaylonWalker/marvin-sw-text-adventure).

## I took a break

It's defintitely good to take breaks from big projects, and for me its often
things like family and work that need to come first and I set things aside. I
am not saying that I am back to daily writing, but I am going to give it a go
and see where it takes me. I've got a big backlog of ideas to get out.
