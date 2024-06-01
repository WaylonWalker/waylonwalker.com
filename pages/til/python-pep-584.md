---
date: 2022-03-22 02:39:53.315809
templateKey: til
title: Python's Dict Union Operator | Pep 584
tags:
  - python
  - python
  - python

---

Today I was watching the python web conf 2022 and saw
[@davidbujic](https://twitter.com/davidvujic) use the new Dict Union Operator
Live on stage during his [Functional
Programming](https://2022.pythonwebconf.com/presentations/functional-python)
talk.  This operator was first introduced into python 3.9 with [pep584](https://peps.python.org/pep-0584/).

## Merge Dicts

I've long updated dicts through the use of unpacking.  Note that the last item
always wins.  It makes it pretty easy to make user overrides to default
configurations.  With pep584 landing in python 3.9 we can now leverage the `|`
operator to achieve the same result.

``` python
default_config = {'url': 'https://example.com', 'assets_dir': 'static' }
user_config = {'url': 'https://waylonwalker.com'}

# **unpacking goes back much further than 3.9

config = {**default_config, **user_config}
print(config)
# {'url': 'https://waylonwalker.com', 'assets_dir': 'static'}


# the same can be achieved through the new to python 3.9 | operator

config = default_config | user_config
print(config)
# {'url': 'https://waylonwalker.com', 'assets_dir': 'static'}
```

[[ python-args-kwargs ]]

> More on unpacking in this post.

## Update Dicts

With the release there is also a new update syntax `|=` that you can use to
update.  I dont often mutate variables for some reason, so I cant think of a
better example for this from my personal use cases. So I will give a similar
example to above, except creating a config, then updating it.

``` python
# old python <3.9 way
config = {'url': 'https://example.com', 'assets_dir': 'static' }
config.update({'url': 'https://waylonwalker.com'})

# new python 3.9+ way
config = {'url': 'https://example.com', 'assets_dir': 'static' }
config |= {'url': 'https://waylonwalker.com'}

print(config)
# {'url': 'https://waylonwalker.com', 'assets_dir': 'static'}
```

## Should you use it?

Are you writing libraries/applications that are only going to be ran on 3.9?
Then ya go for it there is nothing to loose.  If there is any chance someone is
going to run your code on 3.8 or older then just use `**`, or `.update`.

## RTFM

This is what comes first to my mind on how to use this new syntax, read
[pep584](https://peps.python.org/pep-0584/) for all the gritty details on it.

## Links

* [@davidbujic](https://twitter.com/davidvujic)
* [pep584](https://peps.python.org/pep-0584/)
