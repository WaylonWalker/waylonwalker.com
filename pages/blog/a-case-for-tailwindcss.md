---
date: 2023-09-10 19:46:19
templateKey: blog-post
title: A Case For Tailwindcss
tags:
  - webdev
published: False
---

I was watching @theprimeagen recently and I think he sold me on using
tailwindcss. The thing about tailwind is that it is not a big component
library, its just a set of css classes mapped to a few (usually one) style.

> All css classes are shitty, so you might as well use someone else's shitty
> css classes on all your projects rather than thinking your being smart with a
> new set of classes that you will hate in 6 months when you come back to the
> project. _roughly quoted from memory of @theprimeagen_

## It's tiny

So unlike big component libraries like tailwind, it comes with a cli that that
it uses to create the final css file. It is able to treeshake out all the
tailwind classes that you are not using and only ship the ones that you are
using.

## It's hard to clash

since the classes are so small and single purpose it's hard to end up with
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

## Installation

`npm` is used to install the cli that you will need to configure and compile tailwindcss.

```sh
npm install -g tailwindcss-cli
```

## Setup

You will need to create a tailwind.config.js file, to get this you can use the cli.

```sh
npx tailwindcss init
```

## Using tailwind with jinja templates

To set up tailwind to work with jinja templates you will need to point the
tailwind config content to your jinja templates directory.

```js
module.exports = {
  content: ["templates/**/*.html"],
};
```

## Setting up the base styles

I like to use the `@tailwind base;`, to do this I set up an input.css file.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

## Compiling

Now that its all setup you can run the tailwindcss command. You will get an
output.css with base tailwind plus any of the classes that you used.

```sh
tailwindcss -i ./input.css -o ./output.css --watch
```