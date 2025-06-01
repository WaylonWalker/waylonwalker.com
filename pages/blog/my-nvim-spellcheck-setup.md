---
date: 2025-05-31 20:11:59
templateKey: blog-post
title: my nvim spellcheck setup
tags:
  - nvim
published: True

---

I've gone too long without a proper spellcheck setup in nvim.  I know it's
there, I just don't use it, I don't have the right key binds to make it work,
and its clunky.

## Default keybinds

* z= show spell suggestions
* zg add word to dictionary
* zw remove word from dictionary
* ]s jump to next misspelled word
* [s jump to previous misspelled word

I really struggle with bracketed keybinds, they don't flow for me.  I have to
shift into it and hit two keys, you cant just pop through them with intent, it
always feels clunky to me.

## Custom keybinds

I barely use F-keys in my keymap so that was free game.  On my keyboard I have
F1-F9 in a numpad layout on my right hand, so F4-F6 are home row, these are
super easy to pop through and update.  I really refrain from using such high
real estate keys like this unless it's for something good, and I do a lot of
writing in nvim, so fingers crossed I use the heck out of it.

* <F4> jump to next misspelled word
* <F5> jump to previous misspelled word
* <F6> show spell suggestions

I still use zg and zw, they seem fine to me.

## The Setup

In my keymap.lua file I added these to the end, they are working so far and
hopefully I use spellcheck more on my posts now that I've made it easy.

``` lua
set("n", "<f4>", "]s")
set("n", "<f5>", "[s")
set("n", "<f6>", "<cmd>Telescope spell_suggest<cr>")
```

## One Failure

I went down a long rabbit hole before this trying to populate the quickfix with
spelling errors, I tried looking for existing plugins, tried to get ai to give
me a good prototype to start with, and everything was over complicated.  So far
I'm really liking this setup.
