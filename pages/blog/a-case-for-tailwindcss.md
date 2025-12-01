---
date: 2023-09-10 19:46:19
templateKey: blog-post
title: A Case For Tailwindcss
published: True
tags:
  - webdev
---

I was watching @theprimeagen recently and I think he sold me on using
tailwindcss. The thing about tailwind is that it is not a big component
library, it's a set of css classes mapped to a few (usually one) style.

> All css classes are shitty, so you might as well use someone else's shitty
> css classes on all your projects rather than thinking you're being smart with a
> new set of classes that you will hate in 6 months when you come back to the
> project. _roughly quoted from memory of @theprimeagen_

## It's tiny

So unlike big component libraries like tailwind, it comes with a cli that that
it uses to create the final css file. It is able to treeshake out all the
tailwind classes that you are not using and only ship the ones that you are
using.

## It's hard to clash

Since the classes are so small and single purpose it's hard to end up with
something like `.card` in two places that mean different things causing you to
duplicate most of that css anyways so that the whole design doesn't break when
you change one or the other.

## the classes make sense

The classes are really clear and easy to understand, they mentally map over
directly to the css that they implement.

Things like margin are easy to grab once you get the grasp of it. `m` for
margin, and a number for how much, and it's really easy to bump just a bit
more.

```css
.m-6 {
  margin: 1.5rem;
}

.m-5 {
  margin: 1.25rem;
}

.m-4 {
  margin: 1rem;
}

.m-3 {
  margin: 0.75rem;
}

.m-2 {
  margin: 0.5rem;
}

.m-1 {
  margin: 0.25rem;
}

.m-0 {
  margin: 0px;
}
```

## Font Sizes are well thought out

Rather than having a bunch of random sizes, tailwind has a really well thought
out design system that does not grow linearly, but with what makes sense. Not
only the font size, but they have given you the appropriate line-height to go
with it.

```css
.text-2xl {
  font-size: 1.5rem;
  line-height: 2rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.text-xs {
  font-size: 0.75rem;
  line-height: 1rem;
}
```

## Colors

This goes for colors too. When I want to do things like make a button look
clickable, all I need to do is bump the color up or down by 100, I don't need
to know deep color theory to understand if it will be noticable, the team has
designed it to work better than I can come up with.

```css
.bg-stone-100 {
  --tw-bg-opacity: 1;
  background-color: rgb(245 245 244 / var(--tw-bg-opacity));
}

.bg-stone-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(231 229 228 / var(--tw-bg-opacity));
}

.bg-stone-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(214 211 209 / var(--tw-bg-opacity));
}

.bg-stone-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(168 162 158 / var(--tw-bg-opacity));
}

.bg-stone-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(250 250 249 / var(--tw-bg-opacity));
}

.bg-stone-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(120 113 108 / var(--tw-bg-opacity));
}

.bg-stone-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(87 83 78 / var(--tw-bg-opacity));
}

.bg-stone-700 {
  --tw-bg-opacity: 1;
  background-color: rgb(68 64 60 / var(--tw-bg-opacity));
}

.bg-stone-900 {
  --tw-bg-opacity: 1;
  background-color: rgb(28 25 23 / var(--tw-bg-opacity));
}
```

## Am I going to start using tailwind?

Right now I am working on some projects that I am going to use tailwind on. I
really see myself liking it. I don't like that I need to install it with
`npm`, but I can get past that. Cli tools seem to work out pretty well, but
anytime I have a project that installs a bagillion node modules they all come
crashing down in 6 month or a year when the project has not been touched and I
just need one small change.

I really like the idea of all these classes being consistent across all my
projects and really being a short hop away from hand writing css vs a heavy
component library. Most of all I like their well thought out design system
that I definitly could not get right myself.
