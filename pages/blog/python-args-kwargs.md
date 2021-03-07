---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: understanding python *args and **kwargs
date: 2020-06-10T05:00:00Z
status: published
description: Python `*args` and `**kwargs` are super useful tools, that when
  used properly can make you code much simpler and easier to maintain.  Large
  manual conversions from a dataset to function arguments can be packed and
  unpacked into lists or dictionaries. Beware though, this power **can** lead
  to some really unreadable/unusable code if done wrong.
cover: '/static/python-args-kwargs.png'

---

<style>
/* h2 {display: block;} */
h2>img { margin: auto; width: 100%;}
</style>

Python `*args` and `**kwargs` are super useful tools, that when used properly can make you code much simpler and easier to maintain.  Large manual conversions from a dataset to function arguments can be packed and unpacked into lists or dictionaries. Beware though, this power **can** lead to some really unreadable/unusable code if done wrong.



## *args are for lists

*args are some magical syntax that will collect function arguments into a list, or unpack a list into individual arguments.

## ![recieving *args](https://images.waylonwalker.com/args-kwargs/1.png "sending *args collects all arguments into a list inside of the function")

When recieving variables as a `*<varname>`, commonly `*args`, the arguments get **packed** into an ordered list.

> Never add *args to your function definition (almost never)

Generally I find `*args` poor naming and it only drives confusion to the user looking at your function trying to decide what exactly it does.  Here I have chosen the name `printrows` since we are printing each item as a row.

``` python
def printer(*printrows: str) -> None:
  for i, row in enumerate(printrows):
    print(i, row)
```

``` python
>>> printer('eggs', 'spam', 'ham')
0 eggs
1 spam
2 ham
```

## Be Aware of AntiPatterns

If your `*args` collection is distictly different things, then make them separate variables.  Using `*args` as a crutch can lead to a really confusing api for your users, even yourself.

## ❌

Here `*args` is confusing as we are a bit unsure of what to pass to `get_user_data`, or which order it needs to be in without reading the code.

``` python
def get_user_data(*args):
  "does stuff given a users GitHub and DevTo username"
  github = reuqests.get(f'https://api.github.com/users/{args[0]}')
  devto = requests.get(f'https://dev.to/api/users/by_username?url={args[1]}')
  ...
```

## ✔

Here the function signature makes it clear what `get_user_data` expects.  Users will not have to read your docstring or worse your source code to understand it each time the reference it.

``` python
def get_user_data(github_username, devto_username):
  "does stuff given a users GitHub and DevTo username"
  github = reuqests.get(f'https://api.github.com/users/{github_username}')
  devto = requests.get(f'https://dev.to/api/users/by_username?url={devto_username}')
  ...
```

## ![sending *args](https://images.waylonwalker.com/args-kwargs/2.png "sending *args unpacks a list into individual arguments to be used in the function")

Inversely we can send a list of things as individual arguments by **unpacking** them into the function call.

``` python
>>> things_to_print = ['eggs', 'spam', 'ham']
>>> printer(*things_to_print)
0 eggs
1 spam
2 ham
```

---

## **kwargs are for dictionaries

Just like `*args` being for lists, `**kwargs` are for dictionaries.  When packing them up inside of a function. The argument name passed in becomes the key, then invers happens when unpacking, the key becomes the argument for the function.

## ![recieving **kwargs](https://images.waylonwalker.com/args-kwargs/3.png)

Here is a function accepting `**printrows` as it's only input. Any keyword argument that you pass into the function will get packed into a dictionary.

``` python
def printer(**printrows: str) -> None:
  for key in printrows:
    print(key, printrows[key])
```

``` python
>>> printer(breakfast='eggs', lunch='spam', dinner='ham')
breakfast eggs
lunch spam
dinner ham
```

Any arguments passed in will throw a `TypeError`, since this `printer` does not accept any positional arguments.

``` python
>>>printer('one')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-f03e96cb5e14> in <module>
----> 1 printer("one")

TypeError: printer() takes 0 positional arguments but 1 was given
```

## Avoid Anti-Patterns

Just as above, if your items are clearly separate things, make them separate things and do not use `**kwargs`.  `**kwargs` are great when you have collections of things that all get treated exactly the sam, if they get treated differently, or you are expecting certain keys to always exist it will be very confusing to your users what they need to pass in.

## ![sending **kwargs](https://images.waylonwalker.com/args-kwargs/4.png)

Sending `**kwargs` is quite useful.  Especially when combining various libraries together.  Often times you can coerse objects into a dictionary, often with something like `.to_dict()`, then pass that whole dictionary to another function.  This makes gluing different libraries together a breeze at times.


``` python
>>> things_to_print = {breakfast:'eggs', lunch:'spam', dinner:'ham'}
>>> printer(**things_to_print)
breakfast eggs
lunch spam
dinner ham
```

---

I setup a repl.it with these examples so that you can quickly jump in, run it, break it, fix it, add breakpoints and really get a feel for them yourself. Check it out 👉 [https://repl.it/@WaylonWalker/args#main.py](https://repl.it/@WaylonWalker/args#main.py)

---

I hope this helps you understand `*args` and `**kwargs` just a bit more.  They can be quite handy to greatly simplify repetative code, expecially if we already have the data setup in the right data structure.
