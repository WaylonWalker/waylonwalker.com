---
templateKey: blog-post
tags: ['kedro', 'python']
title: Just Ask Ipython for help
date: 2021-10-10T21:38:26
status: published

---

## It happens to the best of us

We can't all remember every single function signature out there, it's just not
possible.  If you want to stay productive while coding without the temptation
to hit YouTube or Twitter.  Use the built in help.  Here are 5 ways to get help
without leaving your terminal.

## Docstrings

In any python repl you can access the docstring of a function by calling for `help`.

``` python
help(df.rolling)
```

In Ipython we can even get some syntax highlighting with the `?`.

``` python
df.rolling?
```

## Source Code

Sometimes the docstrings are not good enough, and don't give us the content we
need, and we just need to look at the source.  Without leaving your terminal
there are two ways I often use to get to the source of a function I am trying
to use.

``` python
import inspect
inspect.getsource(df.rolling)
```

The more common way I do it is with the ipython `??`.

```
df.rolling??
```

## Bonus rich.inspect

You thought the syntax highlighting was good with ipython, check out what
`rich.inspect` can do! As far as I know there is no way to get to source code,
but the results are still fantastic.



``` bash
pip install rich
```

> Install rich

``` python
from rich import inspect
inspect(cars.rolling, help=True)
```

> then inspect

## Connect with me

If you liked this one, check out the YouTube Channel, catch me live on twitch,
or connect on twitter, I'd love to hear from you.

twitter:  https://twitter.com/_WaylonWalker
twitch: https://www.twitch.tv/waylonwalker
github: https://github.com/waylonwalker/
twitch: https://www.twitch.tv/waylonwalker
