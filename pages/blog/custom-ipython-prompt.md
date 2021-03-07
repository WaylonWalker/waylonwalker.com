---
templateKey: blog-post
tags: ['python']
title: Custom Ipython Prompt
date: 2020-12-20T00:00:00
status: published
description: ''

---

I've grown tired of the standard ipython prompt as it doesn't do much to give
me any useful information.  The default one gives out a line number that only
seems to add anxiety as I am working on a simple problem and see that number
grow to several hundred.  I start to question my ability 🤦‍♂️.

## Configuration


If you already have an ipython config you can move on otherwise check out this
post on creating an ipython config.

https://waylonwalker.com/ipython-config

## The Dream Prompt

I want something similar to the starship prompt I am using in the
shell.  I want to be able to quickly see my python version,
environment name, and git branch.

* python version
* active environment
* git branch

![my zsh prompt](https://images.waylonwalker.com/my-zsh-prompt.png)

> This is my zsh prompt I am using for inspiration

## Basic Prompt

This is mostly boilerplate that I found from various google
searches, but this gets me a basic green chevron as my prompt.

``` python
from IPython.terminal.prompts import Prompts, Token

class MyPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [ ( Token.Prompt, "❯ ",), ]

    def out_prompt_tokens(self, cli=None):
        return []

ip = get_ipython()
ip.prompts = MyPrompt(ip)

```

> The rest of this post will build off of this boilerplate and add
> to the `in_prompt_tokens` method of MyPrompt

## Colors

I mostly set the colors of my prompt throughout this post by guessing and
trying different attributes under the Token.

## Red If Error

I found that the `Prompts` subclass has many of the same methods as the ipython
object, so I would often use that for inspection.  Looking through the ipython
class I found a boolean under `shell.last_execution_succeeded` that would give
me if the last execution was successful or not.  I did an inline if statemetn
to set the color to a `Token.Generic.Error` if this was false.

``` python
def in_prompt_tokens(self, cli=None):
    return [
        (
            Token.Prompt
            if self.shell.last_execution_succeeded
            else Token.Generic.Error,
            "❯ ",
        ),
    ]
```

## Python Version

Next up to list out the python version that is running.  I grabbed the version
from `platform.python_version`, this seemed to get me the most concise version
that I was looking for to match the starship prompt.

_<small><mark>update imports</mark></small>_
``` python
from platform import python_version
```

_<small><mark>update prompt</mark></small>_
``` python
def in_prompt_tokens(self, cli=None):
    return [
        (
            (Token.Name.Class, "v" + python_version()),
            (Token, " "),
            Token.Prompt
            if self.shell.last_execution_succeeded
            else Token.Generic.Error,
            "❯ ",
        ),
    ]
```

## Python environment

Since I use conda for my environments I chose to pull the name of the
environment from the `CONDA_DEFAULT_ENV` environment variable that is set by
conda when you change your environment.

_<small><mark>update imports</mark></small>_
``` python
from platform import python_version
import os
```

_<small><mark>update prompt</mark></small>_
``` python
def in_prompt_tokens(self, cli=None):
    return [
        (
            (Token.Prompt, "©"),
            (Token.Prompt, os.environ["CONDA_DEFAULT_ENV"]),
            (Token, " "),
            (Token.Name.Class, "v" + python_version()),
            (Token, " "),
            Token.Prompt
            if self.shell.last_execution_succeeded
            else Token.Generic.Error,
            "❯ ",
        ),
    ]
```

## Git Branch

Git branch was a bit tricky.  There might be a better way to get it,
but I was sticking with things I knew, the git cli and python.  I
did need to do a bit of googling to figure out that git has a
`--show-current` option.

_<small><mark>getting the current git branch</mark></small>_
``` python
def get_branch():
    try:
        return (
            subprocess.check_output(
                "git branch --show-current", shell=True, stderr=subprocess.DEVNULL
            )
            .decode("utf-8")
            .replace("\n", "")
        )
    except BaseException:
        return ""
```

**NOTE**  If this is run form a non-git directory you will quickly find git
errors after every command as this function tries to ask for the git branch.
Sending stderr to devnull will avoid this inconvenience.

_<small><mark>add git branch to prompt</mark></small>_
``` python
def in_prompt_tokens(self, cli=None):
    return [
        (
            (Token.Generic.Subheading, "↪"),
            (Token.Generic.Subheading, get_branch()),
            (Token, " "),
            (Token.Prompt, "©"),
            (Token.Prompt, os.environ["CONDA_DEFAULT_ENV"]),
            (Token, " "),
            (Token.Name.Class, "v" + python_version()),
            (Token, " "),
            Token.Prompt
            if self.shell.last_execution_succeeded
            else Token.Generic.Error,
            "❯ ",
        ),
    ]
```

## Add current directory name

I am a big fan of pathlib so that is what I will use to get the path. If I
planned on using python `<3.6` I would probably use something else, but this is
what I know and I can't think of the last time I used `<3.6>` for anything.

_<small><mark>update imports</mark></small>_
``` python
from pathlib import Path
```


_<small><mark>add git branch to prompt</mark></small>_
``` python
def in_prompt_tokens(self, cli=None):
    return [
        (
            (Token, ""),
            (Token.OutPrompt, Path().absolute().stem),
            (Token, ""),
            (Token.Generic.Subheading, "↪"),
            (Token.Generic.Subheading, get_branch()),
            (Token, " "),
            (Token.Prompt, "©"),
            (Token.Prompt, os.environ["CONDA_DEFAULT_ENV"]),
            (Token, " "),
            (Token.Name.Class, "v" + python_version()),
            (Token, " "),
            Token.Prompt
            if self.shell.last_execution_succeeded
            else Token.Generic.Error,
            "❯ ",
        ),
    ]
```

## Final Script

That's it for my prompt at the moment.  I have been using it for about a week.
It seems to have everything I need so far, and skips on things I don't need.


Enjoy the full script.

_<small><mark>my final prompt</mark></small>_
``` python
from IPython.terminal.prompts import Prompts, Token
from pathlib import Path
import os
from platform import python_version
import subprocess

def get_branch():
    try:
        return (
            subprocess.check_output(
                "git branch --show-current", shell=True, stderr=subprocess.DEVNULL
            )
            .decode("utf-8")
            .replace("\n", "")
        )
    except BaseException:
        return ""


class MyPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [
            (Token, ""),
            (Token.OutPrompt, Path().absolute().stem),
            (Token, " "),
            (Token.Generic.Subheading, "↪"),
            (Token.Generic.Subheading, get_branch()),
            (Token, " "),
            (Token.Prompt, "©"),
            (Token.Prompt, os.environ["CONDA_DEFAULT_ENV"]),
            (Token, " "),
            (Token.Name.Class, "v" + python_version()),
            (Token, " "),
            (Token.Name.Entity, "ipython"),
            (Token, "\n"),
            (
                Token.Prompt
                if self.shell.last_execution_succeeded
                else Token.Generic.Error,
                "❯ ",
            ),
        ]

    def out_prompt_tokens(self, cli=None):
        return []


ip = get_ipython()
ip.prompts = MyPrompt(ip)
```
