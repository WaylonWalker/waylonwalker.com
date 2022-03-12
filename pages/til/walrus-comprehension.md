---
date: 2022-03-12 15:01:59.755653
templateKey: til
title: Python Walrus Inside List Comprehension
tags:
  - python

---

Python 3.8 came out two and a half years ago and I have yet to really lean in
on the walrus operator.  Partly because it always seemed like something kinda
silly (my use cases) to require a python version bump for, and partly because I
really didn't understand it the best.  Primarily I have wanted to use it in
comprehensions, but I did not really understand how.

Now that Python 3.6 is end of life, and most folks are using at least `3.8` it
seems time to learn and use it.

## What's a Walrus
_:=_

The assignment operator in python is more commonly referred to as the walrus
operator due to how `:=` looks like a walrus.  It allows you to assign and use
a variable in a single expression.

This example from the docs avoids a second call to the `len` function.

``` python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

## Let's get some data
_without a walrus_

In this example we are going to do a dict comp to generate a map of content
from urls, only if their status code is 200.  When doing this in a dictionary
comprehension we end up needing to hit the url twice for successful urls. Once
for the filter and once for the data going into the dictionary.

``` python
{
    url: requests.get(url).content
    for url in ["https://waylonwalker.com/", "https://waylonwalker.com/broken"]
    if requests.get(url).status_code == 200
}
```

## Gimme some walrus
_using walrus in a dict comp_

Using the walrus operator `:=` list comp allows us to only put things into the
dictionary that we want to keep, and not hit the url twice.

``` python
{
    url: r.content
    for url in ["https://waylonwalker.com/", "https://waylonwalker.com/broken"]
    if (r := requests.get(url)).status_code == 200
}
```

## FIN

The walrus is a nice to have option to save on extra function/network calls, and
micro optimize your code without adding much extra.
