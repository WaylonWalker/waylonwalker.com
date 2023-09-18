---
date: 2023-09-17 17:10:32
templateKey: til
title: Setup Tailwind for Jinja
status: published
tags:
  - python
---

I've recently given tailwindcss a second chance and am really liking it. Here
is how I set it up for my python based projects.

https://waylonwalker.com/a-case-for-tailwindcss

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

Now that it's all setup you can run the tailwindcss command. You will get an
output.css with base tailwind plus any of the classes that you used.

```sh
tailwindcss -i ./input.css -o ./output.css --watch
```
