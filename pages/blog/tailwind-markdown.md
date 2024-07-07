---
date: 2024-02-01 08:17:03
templateKey: blog-post
title: tailwind and markdown
tags:
  - webdev
published: False

---


This post is a bit of an experiment to see what I can do. Lets start with a
block of pink text.  I build my blog with my own static site generator called [[ markata ]]

[[tailwind-and-jinja]]

[[ still-loving-tailwind ]]

``` markdown
{.text-pink-500}

This text should be pink

This text should be not pink
```

---

{.text-pink-500}

This text should be pink

This text should be not pink

---

Now will it work with bulleted lists

``` markdown
{.text-pink-500}
This block will be pink

{.text-pink-500}

* Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim
* labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi
* anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est

This block will not be pink.

* Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim
* labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi
* anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est

```

---

{.text-pink-500}
This block will be pink

{.text-pink-500}

* Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim
* labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi
* anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est

This block will not be pink.

* Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim
* labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi
* anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est

---

## Inline classes

``` markdown
Now within a [paragraph]{.text-pink-500} can we add [inline classes]{.text-pink-500 .font-bold .underline}.
```

Now within a [paragraph]{.text-pink-500} can we add [inline classes]{.text-pink-500 .font-bold .underline}.

## Pros {.text-green-500 .font-bold .underline}

* lorem
* ipsum
* dolor

## [Cons]{.text-red-500 .font-bold .line-through .decoration-white}

* lorem
* ipsum
* dolor
