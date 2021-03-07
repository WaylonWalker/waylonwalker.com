---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Do You Hoist
date: 2020-02-25T12:52:00Z
status: published
description: Do you have any use cases that you use hoising?  Why?  It seems like
  a really cool feature in any language that uses it, but I dont really notice it
  in use.
cover: "/static/do-you-hoist.png"

---
I am working through Wes Bos's [beginnerjavascript.com/](https://beginnerjavascript.com/) I just hit module 18 on hoisting.  It's something that I always knew was there, Its not something I typically see used or use myself.

# Do you Hoist?

Do you have any use cases that you use hoising?  Why?  It seems like a really cool feature in any language that uses it, but I dont really notice it in use.

# What is Hoising

There are many articles that cover this in far more depth, but its the idea that variable declarations and functions are defined before they are executed.  This means that it doesnt matter if you call a function before or after it is defined.


# Hoisting

``` javascript

console.log(`Hello ${getUser()}`)

function getUser() {
  return 'Waylon'
}
```

Running this code will log out "Waylon"

# What about variable hoisting

I am most familiar with python which does not variable hoist so this one kinda confused me at first.  It only hoists the variable declaration not the value of the variable.  It defines whether the variable is going to be `var`, `let`, or `const` and sets it to undefined.

> It only hoists the variable declaration not the value of the variable.

``` javascript
console.log('name: ', name)
console.log('firstName: ', firstName)

const name = "Waylon"
```

This code will log out `name: undefined` followed by an `Uncaught ReferenceError: firstName is not defined` since `name` has been decalared and `firstName` has not been decalred.

# I don't Hoist

Really it feels weird to call function definitions before using them.  I really dont have a better reason.  It just feels more natural to do so.

# Is hoisting more readable?

I kinda like the idea of putting the 🥩 meat of the file up at the top so that someone reading it will see the good stuff first, then can optionally dig into the weeds if they need to.

# I started a newsletter

I recently started a newsletter, [join in](https://waylonwalker.com/newsletter) and let me know what you want to hear about.
