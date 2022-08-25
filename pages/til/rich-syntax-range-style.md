---
date: 2022-08-24 20:06:34
templateKey: til
title: Highlighting text ranges with Rich | python
tags:
  - python

---

Today I've been playing with
[py-tree-sitter](https://github.com/tree-sitter/py-tree-sitter) a bit and I
wanted to highlight match ranges, but was unable to figure out how to do it
with [rich](https://github.com/Textualize/rich), so I reached out to
[@textualizeio](https://twitter.com/textualizeio) for help.

https://twitter.com/_WaylonWalker/status/1562469770766589952

While waiting for that reply let's show how we got this far.

## imports

Lets import all the classes that we need from [rich](https://github.com/Textualize/rich) and setup a console to print
to.

``` python
from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style

console = Console()
```

## some code

Now we need some code to highlight. I am going to rip my `register_pipeline`
from [another post](https://waylonwalker.com/designing-kedro-router).

``` python
code = '''
from find_kedro import find_kedro

def register_pipelines(self) -> Dict[str, Pipeline]:
    """Register the project's pipeline.
    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return find_kedro()
'''
```

## print

We could simply print out the code we have as a variable, but thats a bit hard
to read.

![print-register-pipelines](https://screenshots.waylonwalker.com/print-register-pipelines.webp)

## console.print

printing with [rich](https://github.com/Textualize/rich)'s console makes it a little better, but not much by default.

![console-print-register-pipelines](https://screenshots.waylonwalker.com/console-print-register-pipelines.webp)

## Syntax

We can pull from [rich](https://github.com/Textualize/rich)'s syntax module to really pretty this up.

``` python
syntax = Syntax(code, 'python', line_numbers=True)
console.print(syntax)
```

![syntax-print-register-pipelines](https://screenshots.waylonwalker.com/syntax-print-register-pipelines.webp)

Now we are getting some really impressive print outs right in the terminal!

> note that I have ipython set to use [rich](https://github.com/Textualize/rich), you will need to console.print() in scripts

## highlight lines

Now we can start highlighting lines right when we initialize our `Syntax`
instance.  It looks ok.  It's not super visible, but more importantly its not
granular enough.  I want to highlight specific ranges like the word
register_pipelines.

``` python
syntax = Syntax(code, 'python', line_numbers=True, highlight_lines=[4])
console.print(syntax)
```

![syntax-print-register-pipelines-highlight-line](https://screenshots.waylonwalker.com/syntax-print-register-pipelines-highlight-line.webp)

This hows the line, but still is not very accurate.

## highlight text

[@textualizeio] got back to me, let's see if What we can do with stylize_range!

https://twitter.com/textualizeio/status/1562487302274043904

``` python
syntax = Syntax(code, 'python', line_numbers=True)
style = Style(bgcolor='deep_pink4')
syntax.stylize_range(style, (4, 4), (4, 22))
console.print(syntax)
```

This gives us the final result we are looking for, we can easily see what is
being targeted here.  In this case the function name `register_pipelines`.

![syntax-highlight-range-register-pipelines](https://screenshots.waylonwalker.com/syntax-highlight-range-register-pipelines.webp)

This turns out to be exacly what I am looking for.  Now I have an easy way to
print out highlighted code wtih my
[py-tree-sitter](https://github.com/tree-sitter/py-tree-sitter) query results.

## Links

* [py-tree-sitter](https://github.com/tree-sitter/py-tree-sitter)
* [rich](https://github.com/Textualize/rich)
* [@textualizeio](https://twitter.com/textualizeio)
* [rich](https://github.com/Textualize/rich)
* [another post](https://waylonwalker.com/designing-kedro-router)
* [print-register-pipelines](https://screenshots.waylonwalker.com/print-register-pipelines.webp)
* [rich](https://github.com/Textualize/rich)
* [console-print-register-pipelines](https://screenshots.waylonwalker.com/console-print-register-pipelines.webp)
* [rich](https://github.com/Textualize/rich)
* [syntax-print-register-pipelines](https://screenshots.waylonwalker.com/syntax-print-register-pipelines.webp)
* [rich](https://github.com/Textualize/rich)
* [syntax-print-register-pipelines-highlight-line](https://screenshots.waylonwalker.com/syntax-print-register-pipelines-highlight-line.webp)
* [py-tree-sitter](https://github.com/tree-sitter/py-tree-sitter)
