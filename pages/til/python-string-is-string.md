---
date: 2022-02-12 16:05:55.326541
templateKey: til
title: Python string of letters is a string of letters, but not with special
tags:
  - python

---

In browsing twitter this morning I came accross this tweet, that showed that
you can use `is` accross two strings if they do not contain special characters.

https://twitter.com/bascodes/status/1492147596688871424

I popped open ipython to play with this.  I could confirm on `3.9.7`, short
strings that I typed in worked as expected.

``` python
waylonwalker ↪main v3.9.7 ipython
❯ a = "asdf"

waylonwalker ↪main v3.9.7 ipython
❯ b = "asdf"

waylonwalker ↪main v3.9.7 ipython
❯ a is b
True
```

Using the `upper()` method on these strings does break down.

``` python
waylonwalker ↪main v3.9.7 ipython
❯ a.upper() is b.upper()
False

waylonwalker ↪main v3.9.7 ipython
❯ a = "ASDF"

waylonwalker ↪main v3.9.7 ipython
❯ b = "ASDF"

waylonwalker ↪main v3.9.7 ipython
❯ a is b
True
```

If You can also see this in the id of the objects as well, which is the memmory
address in CPython.

``` python
waylonwalker ↪main v3.9.7 ipython
❯ id(a)
140717359289568

waylonwalker ↪main v3.9.7 ipython
❯ id(b)
140717359289568

waylonwalker ↪main v3.9.7 ipython
❯ id(a.upper())
140717359581824

waylonwalker ↪main v3.9.7 ipython
❯ id(b.upper())
140717360337824
```

Finally just as the post shows if you add a special character in there it also
breaks.

``` python
waylonwalker ↪main v3.9.7 ipython
❯ a = "ASDF!"

waylonwalker ↪main v3.9.7 ipython
❯ b = "ASDF!"

waylonwalker ↪main v3.9.7 ipython
❯ a is b
False
```

## What should you do

First and foremost, these are the exact pitfalls that `flake8` guards you
against.  So the very first things you should take away here is that there is a
lot of wisdom and value in `flake8`.

Second, the `is` comparison should be used for things that you want to compare
to exact memmory addresses.  These include booleans and None.  Don't use `is`
accross two assigned variables.
